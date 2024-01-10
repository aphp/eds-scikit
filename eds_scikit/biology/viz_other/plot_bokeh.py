from eds_scikit.biology.viz_other.aggregate_measurement_table import compute_df_category_statistics, compute_df_value_statistics, compute_df_value_statistics

from loguru import logger

from bokeh.models import ColumnDataSource, Whisker, Panel, Tabs
from bokeh.plotting import figure, show, output_notebook
from bokeh.sampledata.autompg2 import autompg2
from bokeh.transform import factor_cmap
from bokeh.palettes import Category10, Category20
from bokeh.layouts import layout
from bokeh.models.widgets import DataTable, TableColumn
from bokeh.io import curdoc

def plot_measurement_summary(measurement, value_column="normalized_value"):
    
    """
    
    Proposing measurement table preparation + extras
    NB : measurement must have ...
    NB : viz numéro 2 (numéro 1 : altair)
    
    """
    
    logger.info(f"Aggregating measurement before visualization.")
    
    stats_categories = compute_df_category_statistics(measurement, pivot_columns=["concept_set", "care_site_short_name"], category_column="GLIMS_ANABIO_concept_code")
    by_care_site_values = compute_df_value_statistics(measurement, pivot_columns=["concept_set", "care_site_short_name"], value_column=value_column)
    by_concept_codes_values = compute_df_value_statistics(measurement, pivot_columns=["concept_set", "GLIMS_ANABIO_concept_code"], value_column=value_column)
    
    concept_sets = stats_categories.index.get_level_values(0)
    
    biology_tables = {}
    for concept_set in concept_sets:
        biology_table = {
            "Code usage" : bokeh_plot_categories(stats_categories.loc[concept_set]),
            "Value distribution" : {"By care site" : bokeh_plot_values(by_care_site_values.loc[concept_set]),
                                    "By concept code" : bokeh_plot_values(by_concept_codes_values.loc[concept_set]),}
        }
        biology_tables.update({concept_set : biology_table})
    
    biology_tables_bokeh = create_tpanel_structure(biology_tables)

    return biology_tables_bokeh


def create_tpanel_structure(data_structure):
    tabs = []
    
    for level_key, level_value in data_structure.items():
        if isinstance(level_value, dict):
            # Recursively create TPanel structure
            subtabs = create_tpanel_structure(level_value)
            panel = Panel(child=subtabs, title=level_key)
            tabs.append(panel)
        else:
            panel = Panel(child=level_value, title=level_key)
            tabs.append(panel)

    return Tabs(tabs=tabs)

def create_data_table(data):
    # Convert the Pandas DataFrame to a Bokeh ColumnDataSource
    source = ColumnDataSource(data)
    
    # Create a simple DataTable with one column
    columns = [TableColumn(field="data", title="Data")]
    data_table = DataTable(columns=columns, source=source, width=400, height=280)
    return data_table

def bokeh_plot_values(stats_table):
    
    pivot_column = stats_table.index.name
    stats_table = stats_table.reset_index()
    
    iqr = stats_table.q75 - stats_table.q25
    stats_table["upper"] = stats_table.q75 + 1.5*iqr
    stats_table["lower"] = stats_table.q25 - 1.5*iqr
    
    source = ColumnDataSource(stats_table)
    
    p = figure(x_range=stats_table[pivot_column], tools="", toolbar_location=None, plot_width=800, plot_height=300,
               title="",
               background_fill_color="#eaefef", y_axis_label="value")
    
    whisker = Whisker(base=pivot_column, upper="upper", lower="lower", source=source)
    p.add_layout(whisker)
    
    p.vbar(pivot_column, 0.7, "q50", "q75", source=source, line_color="black")
    p.vbar(pivot_column, 0.7, "q25", "q50", source=source, line_color="black")
    
    # outliers
    #outliers = df[~df[value_column].between(df.lower, df.upper)]
    #p.scatter(pivot_column, value_column, source=outliers, size=6, color="black", alpha=0.3)
    
    p.xgrid.grid_line_color = None
    length = (stats_table['upper'].max() - stats_table['lower'].min()) / 100
    p.y_range.start = stats_table['lower'].min() - length
    p.y_range.end = stats_table['upper'].max() + length
    
    return p

def bokeh_plot_categories(stats_category):
        
    stats_category = stats_category.set_index("category", append=True).unstack().fillna(0)
    stats_category.columns = stats_category.columns.get_level_values(1) # Set column names to the first level

    p = figure(x_range=stats_category.index.tolist(), plot_height=350, title="Stacked Bar Plot",
               toolbar_location=None, tools="")
    
    # Create a ColumnDataSource from the DataFrame
    source = ColumnDataSource(stats_category)
    
    # Use Category20 palette for different colors
    colors = Category20[len(stats_category.columns)] if len(stats_category.columns) > 2 else Category10[3][:len(stats_category.columns)]
    
    # Plot stacked bars
    p.vbar_stack(stats_category.columns.tolist(), x=stats_category.index.name, width=0.9, color=colors, source=source, legend_label=stats_category.columns.tolist())

    # Customize plot
    p.y_range.start = 0
    p.xgrid.grid_line_color = None
    p.axis.minor_tick_line_color = None
    p.outline_line_color = None
    #p.legend.location = "top_left"
    p.legend.orientation = "vertical"
    p.add_layout(p.legend[0], 'right')
    
    return p