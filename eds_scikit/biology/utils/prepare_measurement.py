from loguru import logger

from eds_scikit.utils.framework import is_koalas, to

from eds_scikit.biology.utils.check_data import check_data_and_select_columns_measurement
from eds_scikit.biology.utils.process_measurement import filter_measurement_valid, filter_measurement_by_date, tag_measurement_anomaly
from eds_scikit.biology.utils.prepare_relationship import prepare_biology_relationship_table
from eds_scikit.biology.utils.process_units import Units

def prepare_measurement_table(data, 
                              start_date, 
                              end_date, 
                              concept_sets, 
                              cohort=None, 
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
    
    # measurement codes mapping
    logger.info(f"Preparing concept codes relationship table and mapping them to measurement.")
    biology_relationship_table = prepare_biology_relationship_table(data, concept_sets)
    measurement = measurement.merge(biology_relationship_table, left_on="measurement_source_concept_id", right_on="ANALYSES_LABORATOIRE_concept_id")
    
    #measurement anomaly tagging
    measurement = tag_measurement_anomaly(measurement)
    
    if convert_units:
        logger.info(f"Lazy preparation not available if convert_units=True. Computed table will be cached.")
        measurement.cache()
        units_mapping = Units(concept_sets=concept_sets).generate_units_mapping(measurement)
        units_mapping = to("koalas", units_mapping)
        measurement = measurement.merge(units_mapping, on=["concept_set", "unit_source_value"])
        
    if outliers_detection:
        measurement = measurement
        
    #measurement = measurement.drop(columns="measurement_date") Pourquoi ?
    
    measurement.cache()
    logger.info(f"Done. Once computed, measurement will be cached.") # or not ?
    
    return measurement
