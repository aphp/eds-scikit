import os
from functools import reduce
from typing import Union

import altair as alt
import pandas as pd
from altair.vegalite.v4.api import VConcatChart as AltChart
from IPython.display import display
from loguru import logger
from pretty_html_table import build_table

from eds_scikit.utils.typing import DataFrame


def plot_concepts_set(
    concepts_set_name: str,
    source_path: str = "Biology_summary",
) -> Union[AltChart, pd.DataFrame]:
    """Plot and save a summary table and 2 interactive dashboards. For more details, have a look on the [visualization section][visualization]

    Parameters
    ----------
    concepts_set_name : str
        Name of the concepts-set to plot
    source_path : str, optional
        Name of the folder with aggregated data where the plots will be saved

    Returns
    -------
    List[AltChart, pd.DataFrame]
        Altair plots describing the volumetric and the distribution properties of your biological data along with a pandas DataFrame with a statistical summary
    """
    if os.path.isdir("{}/{}".format(source_path, concepts_set_name)):
        if os.path.isfile(
            "{}/{}/measurement_stats.pkl".format(source_path, concepts_set_name)
        ):
            measurement_stats = pd.read_pickle(
                "{}/{}/measurement_stats.pkl".format(source_path, concepts_set_name)
            )
            _save_and_display_table(measurement_stats, source_path, concepts_set_name)
        if os.path.isfile(
            "{}/{}/measurement_volumetry.pkl".format(source_path, concepts_set_name)
        ):
            measurement_volumetry = pd.read_pickle(
                "{}/{}/measurement_volumetry.pkl".format(source_path, concepts_set_name)
            )
            interactive_volumetry = plot_interactive_volumetry(
                measurement_volumetry,
            )
            _save_and_display_chart(
                interactive_volumetry,
                source_path,
                concepts_set_name,
                "interactive_volumetry",
            )
        if os.path.isfile(
            "{}/{}/measurement_distribution.pkl".format(source_path, concepts_set_name)
        ):
            measurement_distribution = pd.read_pickle(
                "{}/{}/measurement_distribution.pkl".format(
                    source_path, concepts_set_name
                )
            )
            interactive_distribution = plot_interactive_distribution(
                measurement_distribution,
            )
            _save_and_display_chart(
                interactive_distribution,
                source_path,
                concepts_set_name,
                "interactive_distribution",
            )

    else:
        logger.error(
            "The folder {} has not been found",
            source_path,
        )
        raise FileNotFoundError


def _save_and_display_chart(
    chart: AltChart, source_path: str, concepts_set_name: str, chart_name: str
):
    chart.display()
    chart.save("{}/{}/{}.html".format(source_path, concepts_set_name, chart_name))


def _save_and_display_table(table: DataFrame, source_path: str, concepts_set_name: str):

    display(table)
    html_measurement_stats = build_table(
        table,
        "blue_dark",
        index=True,
        font_size="x-small",
        font_family="Open Sans, sans-serif",
    )

    # Save to html file
    with open(
        "{}/{}/stats_summary.html".format(source_path, concepts_set_name), "w"
    ) as f:
        f.write(html_measurement_stats)

    table.to_csv(
        "{}/{}/stats_summary.csv".format(source_path, concepts_set_name), index=False
    )


def plot_interactive_distribution(measurement: DataFrame):

    standard_terminologies = _get_standard_terminologies(measurement)

    measurement["over_freq"] = measurement["frequency"].where(
        measurement["over_outlier"], 0
    )
    measurement["under_freq"] = measurement["frequency"].where(
        measurement["under_outlier"], 0
    )
    measurement["inside_freq"] = measurement["frequency"].where(
        ~measurement["over_outlier"] & ~measurement["under_outlier"], 0
    )
    measurement["legend_outlier"] = "Outliers grouped at the thresholds"

    alt.data_transformers.disable_max_rows()
    hospital_selection = alt.selection_multi(fields=["care_site_short_name"])
    value_selection = alt.selection_interval(bind="scales", encodings=["x"])
    color_hospital = alt.condition(
        hospital_selection,
        alt.Color(
            "care_site_short_name:N", legend=None, scale=alt.Scale(scheme="accent")
        ),
        alt.value("lightgray"),
    )

    hospital_hist = (
        alt.Chart(measurement)
        .mark_bar()
        .encode(
            y=alt.Y(
                "sum(frequency):Q",
                axis=alt.Axis(format="s"),
                title="Number of measurements per hospital",
            ),
            x=alt.X(
                "care_site_short_name:N",
                title="Hospital",
                sort={"field": "frequency", "op": "sum", "order": "descending"},
            ),
            color=color_hospital,
            tooltip=alt.Tooltip("sum(frequency):Q", format=","),
        )
        .transform_filter(value_selection)
        .add_selection(hospital_selection)
    ).properties(width=900)

    # Density Chart
    overall_dist_base = (
        alt.Chart(measurement, title="Overall distribution")
    ).properties(height=100)

    overall_density = (
        overall_dist_base.transform_window(
            sort=[{"field": "binned_value"}], cumulative_count="sum(inside_freq)"
        )
        .transform_window(
            sort=[{"field": "cumulative_count"}],
            window=[
                {
                    "field": "cumulative_count",
                    "op": "ntile",
                    "as": "quartile",
                    "param": 4,
                }
            ],
        )
        .mark_bar()
        .encode(
            x=alt.X(
                "binned_value:Q",
                title="Value",
            ),
            y=alt.Y(
                "sum(inside_freq):Q",
                axis=alt.Axis(format="s"),
                title="Overall frequency",
            ),
            color=alt.Color(
                "quartile:O",
                scale=alt.Scale(scheme="pastel1"),
                legend=None,
            ),
            tooltip=[
                alt.Tooltip("binned_value:Q", title="Value", format=","),
                alt.Tooltip("sum(inside_freq):Q", title="Frequency", format=","),
            ],
        )
    )

    overall_outlier_base = (
        overall_dist_base.transform_joinaggregate(
            TotalMeasures="sum(frequency)",
            TotalOver="sum(over_freq)",
            MaxValue="max(binned_value)",
            TotalUnder="sum(under_freq)",
            MinValue="min(binned_value)",
        )
        .mark_bar(color="gray")
        .encode(
            opacity=alt.Opacity(
                "legend_outlier",
                legend=alt.Legend(orient="bottom", title=None),
            )
        )
    )

    overall_overlier = overall_outlier_base.transform_calculate(
        Percentage="datum.TotalOver / datum.TotalMeasures"
    ).encode(
        x=alt.X(
            "MaxValue:Q",
            title="Value",
        ),
        y=alt.Y(
            "TotalOver:Q",
            axis=alt.Axis(format="s"),
            title="Outliers frequency",
        ),
        tooltip=[
            alt.Tooltip(
                "MaxValue:Q",
                title="Maximum threshold (computed with MAD formula)",
                format=",",
            ),
            alt.Tooltip(
                "TotalOver:Q",
                title="Frequency over the maximum",
            ),
            alt.Tooltip(
                "Percentage:Q",
                format=".2%",
            ),
        ],
    )
    overall_underlier = overall_outlier_base.transform_calculate(
        Percentage="datum.TotalUnder / datum.TotalMeasures"
    ).encode(
        x=alt.X(
            "MinValue:Q",
            title="Value",
        ),
        y=alt.Y(
            "TotalUnder:Q",
            axis=alt.Axis(format="s"),
            title="Outliers frequency",
        ),
        tooltip=[
            alt.Tooltip(
                "MinValue:Q",
                title="Minimum threshold (computed with MAD formula)",
                format=",",
            ),
            alt.Tooltip(
                "TotalUnder:Q",
                title="Frequency under the minimum",
            ),
            alt.Tooltip(
                "Percentage:Q",
                format=".2%",
            ),
        ],
    )

    overall_density = (
        alt.layer(
            overall_density,
            alt.layer(overall_underlier, overall_overlier).resolve_scale(y="shared"),
        )
        .resolve_scale(y="independent")
        .add_selection(value_selection)
        .transform_filter(hospital_selection)
    )

    if standard_terminologies:
        terminologies_hist = []
        terminologies_distribution = []
        terminologies_selection = []
        overall_densities = []
        width = 900 / len(standard_terminologies)

        terminology_dist_base = (alt.Chart(measurement)).properties(
            height=100, width=width
        )
        terminology_density = (
            terminology_dist_base.transform_window(
                sort=[{"field": "binned_value"}],
                groupby=[
                    "{}_concept_code".format(terminology)
                    for terminology in standard_terminologies
                ],
                cumulative_count="sum(inside_freq)",
            )
            .transform_window(
                sort=[{"field": "cumulative_count"}],
                groupby=[
                    "{}_concept_code".format(terminology)
                    for terminology in standard_terminologies
                ],
                window=[
                    {
                        "field": "cumulative_count",
                        "op": "ntile",
                        "as": "quartile",
                        "param": 4,
                    }
                ],
            )
            .mark_bar()
            .encode(
                x=alt.X(
                    "binned_value:Q",
                    title="Value",
                ),
                y=alt.Y(
                    "sum(inside_freq):Q",
                    axis=alt.Axis(format="s"),
                    title="Frequency",
                ),
                color=alt.Color(
                    "quartile:O",
                    scale=alt.Scale(domain=[1, 2, 3, 4], scheme="pastel1"),
                    legend=alt.Legend(orient="bottom", title="Quartile"),
                ),
                tooltip=[
                    alt.Tooltip("binned_value:Q", title="Value", format=","),
                    alt.Tooltip("sum(inside_freq):Q", title="Frequency", format=","),
                ],
            )
        )

        terminology_outlier_base = (
            terminology_dist_base.transform_joinaggregate(
                TotalMeasures="sum(frequency)",
                TotalOver="sum(over_freq)",
                MaxValue="max(binned_value)",
                TotalUnder="sum(under_freq)",
                MinValue="min(binned_value)",
                groupby=[
                    "{}_concept_code:N".format(terminology)
                    for terminology in standard_terminologies
                ],
            )
            .mark_bar(color="grey")
            .encode(
                opacity=alt.Opacity(
                    "legend_outlier",
                    legend=alt.Legend(orient="bottom", title=None),
                )
            )
        )

        terminology_overlier = terminology_outlier_base.transform_calculate(
            Percentage="datum.TotalOver / datum.TotalMeasures"
        ).encode(
            x=alt.X(
                "MaxValue:Q",
                title="Value",
            ),
            y=alt.Y(
                "TotalOver:Q",
                axis=alt.Axis(format="s"),
                title="Outliers frequency",
            ),
            tooltip=[
                alt.Tooltip(
                    "MaxValue:Q",
                    title="Maximum threshold (computed with MAD formula)",
                    format=",",
                ),
                alt.Tooltip(
                    "TotalOver:Q",
                    title="Frequency over the maximum",
                ),
                alt.Tooltip(
                    "Percentage:Q",
                    format=".2%",
                ),
            ],
        )

        terminology_underlier = terminology_outlier_base.transform_calculate(
            Percentage="datum.TotalUnder / datum.TotalMeasures"
        ).encode(
            x=alt.X(
                "MinValue:Q",
                title="Value",
            ),
            y=alt.Y(
                "TotalUnder:Q",
                axis=alt.Axis(format="s"),
                title="Outliers frequency",
            ),
            tooltip=[
                alt.Tooltip(
                    "MinValue:Q",
                    title="Minimum threshold (computed with MAD formula)",
                    format=",",
                ),
                alt.Tooltip(
                    "TotalUnder:Q",
                    title="Frequency under the minimum",
                ),
                alt.Tooltip(
                    "Percentage:Q",
                    format=".2%",
                ),
            ],
        )

        terminology_distribution_base = (
            alt.layer(
                terminology_density,
                alt.layer(terminology_underlier, terminology_overlier).resolve_scale(
                    y="shared"
                ),
            )
            .transform_filter(hospital_selection)
            .add_selection(value_selection)
        ).resolve_scale(y="independent")
        for terminology in standard_terminologies:

            terminology_selection = alt.selection_multi(
                fields=["{}_concept_code".format(terminology)],
            )
            terminologies_selection.append(terminology_selection)

            terminology_color = alt.condition(
                terminology_selection,
                alt.Color(
                    "{}_concept_code:N".format(terminology),
                    legend=None,
                    scale=alt.Scale(scheme="pastel2"),
                ),
                alt.value("lightgray"),
            )

            terminology_hist = (
                alt.Chart(measurement)
                .mark_bar()
                .encode(
                    y=alt.Y(
                        "sum(frequency):Q",
                        axis=alt.Axis(format="s"),
                        title="Number of measurements per {} code".format(terminology),
                    ),
                    x=alt.X(
                        "{}_concept_code:N".format(terminology),
                        title="{} code".format(terminology),
                        sort={
                            "field": "frequency",
                            "op": "sum",
                            "order": "descending",
                        },
                    ),
                    color=terminology_color,
                    tooltip=alt.Tooltip("sum(frequency):Q", format=","),
                )
                .add_selection(terminology_selection)
                .transform_filter(value_selection)
                .transform_filter(hospital_selection)
            )

            terminologies_hist.append(terminology_hist.properties(width=width))

            terminology_distribution = (
                (
                    terminology_distribution_base.facet(
                        row=alt.Row(
                            "{}_concept_code:N".format(terminology),
                            sort={
                                "field": "frequency",
                                "op": "sum",
                                "order": "descending",
                            },
                        )
                    )
                )
                .resolve_scale(y="independent")
                .properties(
                    title=alt.TitleParams(
                        text="Distribution per {} code".format(terminology),
                        anchor="middle",
                        align="center",
                    )
                )
            )
            terminologies_distribution.append(terminology_distribution)
            overall_densities.append(overall_density.properties(width=width))

        for terminology_selection in terminologies_selection:
            hospital_hist = hospital_hist.transform_filter(terminology_selection)
            for idx in range(len(standard_terminologies)):
                if idx != terminologies_selection.index(terminology_selection):
                    terminologies_hist[idx] = terminologies_hist[idx].transform_filter(
                        terminology_selection
                    )
                terminologies_distribution[idx] = terminologies_distribution[
                    idx
                ].transform_filter(terminology_selection)

        terminologies_hist = reduce(
            lambda terminology_hist_1, terminology_hist_2: terminology_hist_1
            | terminology_hist_2,
            terminologies_hist,
        )
        terminologies_distribution = reduce(
            lambda terminology_distribution_1, terminology_distribution_2: terminology_distribution_1
            | terminology_distribution_2,
            terminologies_distribution,
        )
        overall_densities = reduce(
            lambda overall_density_1, overall_density_2: alt.hconcat(
                overall_density_1, overall_density_2, spacing=75
            ),
            overall_densities,
        )

    else:
        terminologies_hist = alt.Chart().mark_text()
        terminologies_distribution = alt.Chart().mark_text()
        overall_densities = (
            overall_density.encode(
                color=alt.Color(
                    "quartile:O",
                    scale=alt.Scale(domain=[1, 2, 3, 4], scheme="pastel1"),
                    legend=alt.Legend(orient="bottom", title="Quartile"),
                ),
            )
            .transform_filter(hospital_selection)
            .properties(width=900)
        )

    chart = (
        hospital_hist
        & terminologies_hist
        & overall_densities
        & terminologies_distribution
    ).resolve_scale(color="independent")

    return chart


def plot_interactive_volumetry(
    measurement: DataFrame,
):
    measurement = _filter_zeros(measurement)
    standard_terminologies = _get_standard_terminologies(measurement)

    alt.data_transformers.disable_max_rows()
    hospital_selection = alt.selection_multi(fields=["care_site_short_name"])
    time_selection = alt.selection_interval(encodings=["x"])
    color_hospital = alt.condition(
        hospital_selection,
        alt.Color("care_site_short_name:N", legend=None),
        alt.value("lightgray"),
    )

    hospital_hist = (
        alt.Chart(measurement)
        .mark_bar()
        .encode(
            y=alt.Y(
                "sum(# measurements):Q",
                axis=alt.Axis(format="s"),
                title="Number of measurements per hospital",
            ),
            x=alt.X(
                "care_site_short_name:N",
                title="Hospital",
                sort={"field": "# measurements", "op": "sum", "order": "descending"},
            ),
            color=color_hospital,
            tooltip=alt.Tooltip("sum(# measurements):Q", format=","),
        )
        .add_selection(hospital_selection)
        .transform_filter(time_selection)
    ).properties(width=900, height=300)

    time_line = (
        alt.Chart(measurement)
        .mark_line()
        .encode(
            x=alt.X(
                "yearmonth(measurement_month):T",
                title="Time (Month Year)",
                axis=alt.Axis(tickCount="month", labelAngle=-90),
            ),
            y=alt.Y(
                "sum(# measurements):Q",
                impute=alt.ImputeParams(value=0),
                axis=alt.Axis(format="s"),
                title="Total number of measurements",
            ),
        )
        .add_selection(time_selection)
        .transform_filter(hospital_selection)
    ).properties(width=900, height=50)

    ratio_missing_hist = (
        alt.Chart(measurement)
        .transform_joinaggregate(
            TotalMeasures="sum(# measurements)",
            Missing="sum(# missing_values)",
            groupby=["care_site_short_name"],
        )
        .transform_calculate(
            Percentage="datum.Missing / (datum.TotalMeasures + datum.Missing)"
        )
        .mark_bar()
        .encode(
            y=alt.Y(
                "Percentage:Q",
                axis=alt.Axis(format="%"),
                title="Percentage of missing values per hospital",
            ),
            x=alt.X(
                "care_site_short_name:N",
                title="Hospital",
                sort={"field": "Percentage", "order": "descending"},
            ),
            color=color_hospital,
            tooltip=[alt.Tooltip("Percentage:Q", format=".2%"), "Missing:Q"],
        )
        .transform_filter(time_selection)
        .transform_filter(hospital_selection)
    ).properties(width=900, height=300)

    if standard_terminologies:
        terminologies_hist = []
        terminologies_time_series = []
        terminologies_selection = []

        width = 900 / len(standard_terminologies)

        for terminology in standard_terminologies:
            terminology_selection = alt.selection_multi(
                fields=["{}_concept_code".format(terminology)]
            )
            terminologies_selection.append(terminology_selection)

            terminology_color = alt.condition(
                terminology_selection,
                alt.Color("{}_concept_code:N".format(terminology), legend=None),
                alt.value("lightgray"),
            )

            terminology_hist = (
                alt.Chart(measurement)
                .mark_bar()
                .encode(
                    y=alt.Y(
                        "sum(# measurements):Q",
                        axis=alt.Axis(format="s"),
                        title="Number of measurements per {} code".format(terminology),
                    ),
                    x=alt.X(
                        "{}_concept_code:N".format(terminology),
                        sort={
                            "field": "# measurements",
                            "op": "sum",
                            "order": "descending",
                        },
                        title="{} code".format(terminology),
                    ),
                    color=terminology_color,
                    tooltip=alt.Tooltip("sum(# measurements):Q", format=","),
                )
                .add_selection(terminology_selection)
                .transform_filter(hospital_selection)
                .transform_filter(time_selection)
            ).properties(height=300, width=width)
            terminologies_hist.append(terminology_hist)

            terminology_time_series = (
                alt.Chart(measurement)
                .mark_line()
                .encode(
                    x=alt.X(
                        "yearmonth(measurement_month):T",
                        title="Time (Month Year)",
                        axis=alt.Axis(tickCount="month", labelAngle=-90),
                    ),
                    y=alt.Y(
                        "sum(# measurements):Q",
                        axis=alt.Axis(format="s"),
                        impute=alt.ImputeParams(value=0),
                        title="Number of measurements",
                    ),
                    color=alt.Color(
                        "{}_concept_code:N".format(terminology),
                        legend=None,
                    ),
                )
                .transform_filter(time_selection)
                .transform_filter(hospital_selection)
            ).properties(height=300, width=width)
            terminologies_time_series.append(terminology_time_series)

        for terminology_filter in terminologies_selection:
            hospital_hist = hospital_hist.transform_filter(terminology_filter)
            time_line = time_line.transform_filter(terminology_filter)
            ratio_missing_hist = ratio_missing_hist.transform_filter(terminology_filter)
            for idx in range(len(standard_terminologies)):
                if idx != terminologies_selection.index(terminology_filter):
                    terminologies_hist[idx] = terminologies_hist[idx].transform_filter(
                        terminology_filter
                    )
                terminologies_time_series[idx] = terminologies_time_series[
                    idx
                ].transform_filter(terminology_filter)

        terminologies_hist = reduce(
            lambda terminology_hist_1, terminology_hist_2: terminology_hist_1
            | terminology_hist_2,
            terminologies_hist,
        )
        terminologies_time_series = reduce(
            lambda terminology_time_series_1, terminology_time_series_2: terminology_time_series_1
            | terminology_time_series_2,
            terminologies_time_series,
        )

    else:
        terminologies_hist = alt.Chart().mark_text()
        terminologies_time_series = (
            alt.Chart(measurement)
            .mark_line()
            .encode(
                x=alt.X(
                    "yearmonth(measurement_month):T",
                    title="Time (Month Year)",
                    impute=alt.ImputeParams(value=0),
                    axis=alt.Axis(tickCount="month", labelAngle=-90),
                ),
                y=alt.Y(
                    "sum(# measurements):Q",
                    axis=alt.Axis(format="s"),
                    title="Number of measurements",
                ),
            )
            .transform_filter(time_selection)
            .transform_filter(hospital_selection)
        ).properties(height=300, width=900)

    chart = (
        hospital_hist
        & time_line
        & terminologies_hist
        & terminologies_time_series
        & ratio_missing_hist
    )

    return chart


def _get_standard_terminologies(measurement):

    standard_terminologies = list(
        set(
            col_name.split("_concept_code")[0]
            for col_name in measurement.columns
            if col_name.endswith("_concept_code")
        )
    )

    # Remove terminology if empty
    for standard_terminology in standard_terminologies.copy():
        if all(
            concept_code == "Non renseigné"
            for concept_code in measurement[
                "{}_concept_code".format(standard_terminology)
            ].unique()
        ):
            standard_terminologies.remove(standard_terminology)
            logger.info(
                "The terminology {} has been deleted because there is no measurement associated",
                standard_terminology,
            )

    return standard_terminologies


def _filter_zeros(measurement):

    count_cols = ["# measurements", "# missing_values"]

    # Remove rows with all 0
    measurement[count_cols] = measurement[measurement[count_cols] > 0][count_cols]
    measurement = measurement.dropna(how="all", subset=count_cols)

    return measurement


# def plot_interactive_distribution_with_time(
#     measurement: DataFrame,
# ):

#     standard_terminologies = _get_standard_terminologies(measurement)

#     measurement["over_freq"] = measurement["frequency"].where(
#         measurement["over_outlier"], 0
#     )
#     measurement["under_freq"] = measurement["frequency"].where(
#         measurement["under_outlier"], 0
#     )
#     measurement["inside_freq"] = measurement["frequency"].where(
#         ~measurement["over_outlier"] & ~measurement["under_outlier"], 0
#     )
#     measurement["legend_outlier"] = "Outliers grouped at the thresholds"

#     delta_time = (
#         measurement["measurement_month"]
#         .astype("datetime64")
#         .dt.to_period("M")
#         .view(dtype="int64")
#         .drop_duplicates()
#         .sort_values()
#         .diff()
#         .min()
#     )

#     if delta_time == 1:
#         time_axis = alt.Axis(tickCount="month", labelAngle=-90, format="%b %Y")
#     elif delta_time == 3:
#         time_axis = alt.Axis(tickCount="month", labelAngle=-90, format="%YQ%q")
#     else:
#         time_axis = alt.Axis(tickCount="year", labelAngle=-90, format="%Y")

#     alt.data_transformers.disable_max_rows()
#     hospital_selection = alt.selection_multi(fields=["care_site_short_name"])
#     time_selection = alt.selection_interval(encodings=["x"])
#     value_selection = alt.selection_interval(bind="scales", encodings=["x"])
#     color_hospital = alt.condition(
#         hospital_selection,
#         alt.Color(
#             "care_site_short_name:N", legend=None, scale=alt.Scale(scheme="accent")
#         ),
#         alt.value("lightgray"),
#     )

#     time_line = (
#         alt.Chart(measurement)
#         .mark_line()
#         .encode(
#             x=alt.X(
#                 "measurement_month:T",
#                 title="Time",
#                 axis=time_axis,
#             ),
#             y=alt.Y(
#                 "sum(frequency):Q",
#                 axis=alt.Axis(format="s"),
#                 impute=alt.ImputeParams(value=0),
#                 title="Total number of measurements",
#             ),
#         )
#         .add_selection(time_selection)
#         .transform_filter(value_selection)
#         .transform_filter(hospital_selection)
#     ).properties(width=900, height=50)

#     hospital_hist = (
#         alt.Chart(measurement)
#         .mark_bar()
#         .encode(
#             y=alt.Y(
#                 "sum(frequency):Q",
#                 axis=alt.Axis(format="s"),
#                 title="Number of measurements per hospital",
#             ),
#             x=alt.X(
#                 "care_site_short_name:N",
#                 title="Hospital",
#                 sort={"field": "frequency", "op": "sum", "order": "descending"},
#             ),
#             color=color_hospital,
#             tooltip=alt.Tooltip("sum(frequency):Q", format=","),
#         )
#         .add_selection(hospital_selection)
#         .transform_filter(value_selection)
#         .transform_filter(time_selection)
#     ).properties(width=900)

#     # Density Chart
#     overall_dist_base = (
#         alt.Chart(measurement, title="Overall distribution")
#     ).properties(height=100)

#     overall_density = (
#         overall_dist_base.transform_window(
#             sort=[{"field": "binned_value"}], cumulative_count="sum(inside_freq)"
#         )
#         .transform_window(
#             sort=[{"field": "cumulative_count"}],
#             window=[
#                 {
#                     "field": "cumulative_count",
#                     "op": "ntile",
#                     "as": "quartile",
#                     "param": 4,
#                 }
#             ],
#         )
#         .mark_bar()
#         .encode(
#             x=alt.X(
#                 "binned_value:Q",
#                 title="Value",
#             ),
#             y=alt.Y(
#                 "sum(inside_freq):Q",
#                 axis=alt.Axis(format="s"),
#                 title="Overall frequency",
#             ),
#             color=alt.Color(
#                 "quartile:O",
#                 scale=alt.Scale(scheme="pastel1"),
#                 legend=None,
#             ),
#             tooltip=[
#                 alt.Tooltip("binned_value:Q", title="Value", format=","),
#                 alt.Tooltip("sum(inside_freq):Q", title="Frequency", format=","),
#             ],
#         )
#     )

#     overall_outlier_base = (
#         overall_dist_base.transform_joinaggregate(
#             TotalMeasures="sum(frequency)",
#             TotalOver="sum(over_freq)",
#             MaxValue="max(binned_value)",
#             TotalUnder="sum(under_freq)",
#             MinValue="min(binned_value)",
#         )
#         .mark_bar(color="grey")
#         .encode(
#             opacity=alt.Opacity(
#                 "legend_outlier",
#                 legend=alt.Legend(orient="bottom", title=None),
#             )
#         )
#     )

#     overall_overlier = overall_outlier_base.transform_calculate(
#         Percentage="datum.TotalOver / datum.TotalMeasures"
#     ).encode(
#         x=alt.X(
#             "MaxValue:Q",
#             title="Value",
#         ),
#         y=alt.Y(
#             "TotalOver:Q",
#             axis=alt.Axis(format="s"),
#             title="Outliers frequency",
#         ),
#         tooltip=[
#             alt.Tooltip(
#                 "MaxValue:Q",
#                 title="Maximum threshold (computed with MAD formula)",
#                 format=",",
#             ),
#             alt.Tooltip(
#                 "TotalOver:Q",
#                 title="Frequency over the maximum",
#             ),
#             alt.Tooltip(
#                 "Percentage:Q",
#                 format=".2%",
#             ),
#         ],
#     )
#     overall_underlier = overall_outlier_base.transform_calculate(
#         Percentage="datum.TotalUnder / datum.TotalMeasures"
#     ).encode(
#         x=alt.X(
#             "MinValue:Q",
#             title="Value",
#         ),
#         y=alt.Y(
#             "TotalUnder:Q",
#             axis=alt.Axis(format="s"),
#             title="Outliers frequency",
#         ),
#         tooltip=[
#             alt.Tooltip(
#                 "MinValue:Q",
#                 title="Minimum threshold (computed with MAD formula)",
#                 format=",",
#             ),
#             alt.Tooltip(
#                 "TotalUnder:Q",
#                 title="Frequency under the minimum",
#             ),
#             alt.Tooltip(
#                 "Percentage:Q",
#                 format=".2%",
#             ),
#         ],
#     )

#     overall_density = (
#         alt.layer(
#             overall_density,
#             alt.layer(overall_underlier, overall_overlier).resolve_scale(y="shared"),
#         )
#         .resolve_scale(y="independent")
#         .transform_filter(hospital_selection)
#         .add_selection(value_selection)
#     )
#     if standard_terminologies:
#         terminologies_hist = []
#         terminologies_distribution = []
#         terminologies_selection = []
#         overall_densities = []
#         width = 900 / len(standard_terminologies)

#         terminology_dist_base = (alt.Chart(measurement)).properties(
#             height=100, width=width
#         )
#         terminology_density = (
#             terminology_dist_base.transform_window(
#                 sort=[{"field": "binned_value"}],
#                 groupby=[
#                     "{}_concept_code".format(terminology)
#                     for terminology in standard_terminologies
#                 ],
#                 cumulative_count="sum(inside_freq)",
#             )
#             .transform_window(
#                 sort=[{"field": "cumulative_count"}],
#                 groupby=[
#                     "{}_concept_code".format(terminology)
#                     for terminology in standard_terminologies
#                 ],
#                 window=[
#                     {
#                         "field": "cumulative_count",
#                         "op": "ntile",
#                         "as": "quartile",
#                         "param": 4,
#                     }
#                 ],
#             )
#             .mark_bar()
#             .encode(
#                 x=alt.X(
#                     "binned_value:Q",
#                     title="Value",
#                 ),
#                 y=alt.Y(
#                     "sum(inside_freq):Q",
#                     axis=alt.Axis(format="s"),
#                     title="Frequency",
#                 ),
#                 color=alt.Color(
#                     "quartile:O",
#                     scale=alt.Scale(domain=[1, 2, 3, 4], scheme="pastel1"),
#                     legend=alt.Legend(orient="bottom", title="Quartile"),
#                 ),
#                 tooltip=[
#                     alt.Tooltip("binned_value:Q", title="Value", format=","),
#                     alt.Tooltip("sum(inside_freq):Q", title="Frequency", format=","),
#                 ],
#             )
#         )

#         terminology_outlier_base = (
#             terminology_dist_base.transform_joinaggregate(
#                 TotalMeasures="sum(frequency)",
#                 TotalOver="sum(over_freq)",
#                 MaxValue="max(binned_value)",
#                 TotalUnder="sum(under_freq)",
#                 MinValue="min(binned_value)",
#                 groupby=[
#                     "{}_concept_code:N".format(terminology)
#                     for terminology in standard_terminologies
#                 ],
#             )
#             .mark_bar(color="gray")
#             .encode(
#                 opacity=alt.Opacity(
#                     "legend_outlier",
#                     legend=alt.Legend(orient="bottom", title=None),
#                 )
#             )
#         )

#         terminology_overlier = terminology_outlier_base.transform_calculate(
#             Percentage="datum.TotalOver / datum.TotalMeasures"
#         ).encode(
#             x=alt.X(
#                 "MaxValue:Q",
#                 title="Value",
#             ),
#             y=alt.Y(
#                 "TotalOver:Q",
#                 axis=alt.Axis(format="s"),
#                 title="Outliers frequency",
#             ),
#             tooltip=[
#                 alt.Tooltip(
#                     "MaxValue:Q",
#                     title="Maximum threshold (computed with MAD formula)",
#                     format=",",
#                 ),
#                 alt.Tooltip(
#                     "TotalOver:Q",
#                     title="Frequency over the maximum",
#                 ),
#                 alt.Tooltip(
#                     "Percentage:Q",
#                     format=".2%",
#                 ),
#             ],
#         )

#         terminology_underlier = terminology_outlier_base.transform_calculate(
#             Percentage="datum.TotalUnder / datum.TotalMeasures"
#         ).encode(
#             x=alt.X(
#                 "MinValue:Q",
#                 title="Value",
#             ),
#             y=alt.Y(
#                 "TotalUnder:Q",
#                 axis=alt.Axis(format="s"),
#                 title="Outliers frequency",
#             ),
#             tooltip=[
#                 alt.Tooltip(
#                     "MinValue:Q",
#                     title="Minimum threshold (computed with MAD formula)",
#                     format=",",
#                 ),
#                 alt.Tooltip(
#                     "TotalUnder:Q",
#                     title="Frequency under the minimum",
#                 ),
#                 alt.Tooltip(
#                     "Percentage:Q",
#                     format=".2%",
#                 ),
#             ],
#         )
#         terminology_distribution_base = (
#             alt.layer(
#                 terminology_density,
#                 alt.layer(terminology_underlier, terminology_overlier).resolve_scale(
#                     y="shared"
#                 ),
#             )
#             .transform_filter(time_selection)
#             .transform_filter(hospital_selection)
#             .add_selection(value_selection)
#         ).resolve_scale(y="independent")

#         for terminology in standard_terminologies:
#             terminology_selection = alt.selection_multi(
#                 fields=["{}_concept_code".format(terminology)],
#             )
#             terminologies_selection.append(terminology_selection)

#             terminology_color = alt.condition(
#                 terminology_selection,
#                 alt.Color(
#                     "{}_concept_code:N".format(terminology),
#                     legend=None,
#                     scale=alt.Scale(scheme="pastel2"),
#                 ),
#                 alt.value("lightgray"),
#             )

#             terminology_hist = (
#                 alt.Chart(measurement)
#                 .mark_bar()
#                 .encode(
#                     y=alt.Y(
#                         "sum(frequency):Q",
#                         axis=alt.Axis(format="s"),
#                         title="Number of measurements per {} code".format(terminology),
#                     ),
#                     x=alt.X(
#                         "{}_concept_code:N".format(terminology),
#                         title="{} code".format(terminology),
#                         sort={
#                             "field": "frequency",
#                             "op": "sum",
#                             "order": "descending",
#                         },
#                     ),
#                     color=terminology_color,
#                     tooltip=alt.Tooltip("sum(frequency):Q", format=","),
#                 )
#                 .add_selection(terminology_selection)
#                 .transform_filter(hospital_selection)
#                 .transform_filter(value_selection)
#                 .transform_filter(time_selection)
#             )

#             terminology_distribution = (
#                 (
#                     terminology_distribution_base.facet(
#                         row=alt.Row(
#                             "{}_concept_code:N".format(terminology),
#                             sort={
#                                 "field": "frequency",
#                                 "op": "sum",
#                                 "order": "descending",
#                             },
#                         )
#                     )
#                 )
#                 .resolve_scale(y="independent")
#                 .properties(
#                     title=alt.TitleParams(
#                         text="Distribution per {} code".format(terminology),
#                         anchor="middle",
#                         align="center",
#                     )
#                 )
#             )

#             terminologies_hist.append(terminology_hist.properties(width=width))

#             terminologies_distribution.append(terminology_distribution)
#             overall_densities.append(overall_density.properties(width=width))

#         for terminology_selection in terminologies_selection:
#             hospital_hist = hospital_hist.transform_filter(terminology_selection)
#             time_line = time_line.transform_filter(terminology_selection)
#             for idx in range(len(standard_terminologies)):
#                 if idx != terminologies_selection.index(terminology_selection):
#                     terminologies_hist[idx] = terminologies_hist[idx].transform_filter(
#                         terminology_selection
#                     )
#                 terminologies_distribution[idx] = terminologies_distribution[
#                     idx
#                 ].transform_filter(terminology_selection)

#         terminologies_hist = reduce(
#             lambda terminology_hist_1, terminology_hist_2: terminology_hist_1
#             | terminology_hist_2,
#             terminologies_hist,
#         )
#         terminologies_distribution = reduce(
#             lambda terminology_distribution_1, terminology_distribution_2: terminology_distribution_1
#             | terminology_distribution_2,
#             terminologies_distribution,
#         )
#         overall_densities = reduce(
#             lambda overall_density_1, overall_density_2: alt.hconcat(
#                 overall_density_1, overall_density_2, spacing=75
#             ),
#             overall_densities,
#         )

#     else:
#         terminologies_hist = alt.Chart().mark_text()
#         terminologies_distribution = alt.Chart().mark_text()
#         overall_densities = (
#             overall_density.encode(
#                 color=alt.Color(
#                     "quartile:O",
#                     scale=alt.Scale(domain=[1, 2, 3, 4], scheme="pastel1"),
#                     legend=alt.Legend(orient="bottom", title="Quartile"),
#                 ),
#             )
#             .transform_filter(hospital_selection)
#             .properties(width=900)
#         )

#     chart = (
#         hospital_hist
#         & time_line
#         & terminologies_hist
#         & overall_densities
#         & terminologies_distribution
#     ).resolve_scale(color="independent")

#     return chart
