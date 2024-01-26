from loguru import logger

from eds_scikit.utils.framework import is_koalas, to

from eds_scikit.biology.utils.check_data import check_data_and_select_columns_measurement
from eds_scikit.biology.utils.process_measurement import filter_measurement_valid, filter_measurement_by_date, tag_measurement_anomaly, normalize_unit
from eds_scikit.biology.utils.prepare_relationship import prepare_biology_relationship_table
from eds_scikit.biology.utils.process_units import Units
from eds_scikit.io.settings import mapping

def prepare_measurement_table(data, 
                              start_date, 
                              end_date, 
                              concept_sets,
                              get_all_terminologies,
                              convert_units=False, 
                              outliers_detection=None,):
    
    """Returns filtered measurement table based on validity, date and concept_sets.
    
    The output format is identical to data.measurement but adding following columns :
    - range_high_anomaly, range_low_anomaly
    - {terminology}_code based on concept_sets terminologies
    - concept_sets
    - normalized_units and normalized_values if convert_units==True
    - outlier if outliers_detection not None

    Parameters
    ----------
    data : _type_
        _description_
    start_date : _type_
        _description_
    end_date : _type_
        _description_
    concept_sets : _type_
        _description_
    cohort : _type_, optional
        _description_, by default None
    convert_units : bool, optional
        _description_, by default False
    outliers_detection : _type_, optional
        _description_, by default None

    Returns
    -------
    _type_
        _description_
    """
    
    measurement, _, _ = check_data_and_select_columns_measurement(data)
    
    # measurement preprocessing
    measurement = filter_measurement_valid(measurement)
    measurement = filter_measurement_by_date(measurement, start_date, end_date)
    measurement = normalize_unit(measurement)
    
    # measurement codes mapping
    biology_relationship_table = prepare_biology_relationship_table(data, concept_sets, get_all_terminologies)
    measurement = measurement.merge(biology_relationship_table, left_on="measurement_source_concept_id", right_on=f"{mapping[0][0]}_concept_id")
    
    #measurement anomaly tagging
    measurement = tag_measurement_anomaly(measurement)
    
    if convert_units:
        logger.info(f"Lazy preparation not available if convert_units=True. Computed table will be cached.")
        measurement.cache()
        conversion_table = to("koalas", get_conversion_table(measurement, concept_sets))
        measurement = measurement.merge(conversion_table, on=["concept_set", "unit_source_value"])
        measurement["normalized_value"] = measurement["value_as_number"] * measurement["factor"]
        
    if outliers_detection:
        measurement = measurement
        
    #measurement = measurement.drop(columns="measurement_date") Pourquoi ?
    
    measurement.cache()
    logger.info(f"Done. Once computed, measurement will be cached.") # or not ?
    
    return measurement

def get_conversion_table(measurement, concepts_sets):
    
    conversion_table = measurement.groupby("concept_set")["unit_source_value"].unique().explode().to_frame().reset_index()
    conversion_table = to("pandas", conversion_table) # nécessaire ??
    conversion_table["target_unit"] = conversion_table["unit_source_value"]
    conversion_table["factor"] = conversion_table.apply(lambda x : 1 if x.target_unit else 0, axis=1)

    for concept_set in concepts_sets:
        target_unit = concept_set.units.target_unit
        conversion_table.loc[conversion_table.concept_set == concept_set.name, "target_unit"] = conversion_table.apply(lambda x : target_unit if concept_set.units.can_be_converted(x.unit_source_value, target_unit) else concept_set.units.get_unit_base(x.unit_source_value), axis=1)
        conversion_table.loc[conversion_table.concept_set == concept_set.name, "factor"] = conversion_table.apply(lambda x : concept_set.units.convert_unit(x.unit_source_value, x.target_unit), axis=1)
    
    conversion_table = conversion_table.fillna(1)
    
    return conversion_table