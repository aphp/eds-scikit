from eds_scikit.utils.checks import concept_checker
from eds_scikit.utils.typing import DataFrame, Series


@concept_checker(concepts=["DESCRIPTION"])
def add_care_site_description(care_site: DataFrame) -> DataFrame:
    """Add column ``DESCRIPTION`` to care_site dataframe.

    This algo applies simple regular expression to simplify the care site name.
    This can be useful for post-processing the description, such as detecting
    the care_site characteristic from the description (is it an emergency care site ?)

    Parameters
    ----------
    care_site : DataFrame
        with column ``care_site_name``


    Returns
    -------
    care_site : DataFrame
        contains additional column ``DESCRIPTION``

    """
    care_site = care_site.assign(
        DESCRIPTION=description_from_care_site_name(care_site["care_site_name"])
    )
    return care_site


def description_from_care_site_name(names: Series) -> Series:
    # Ce qui ne marche pas encore très bien:
    # - "O.R.L" devient "O R L", "ORL" serait mieux
    # - "SURV CONT MED-C" devient "SURV CONT MED C"
    description = (
        names.pipe(ensure_upper)
        .pipe(only_letters)
        .pipe(remove_hospital_trigram)
        .pipe(remove_hierarchy_litteral)
        .pipe(simplify_spaces)
    )
    return description


def ensure_upper(name_series: Series) -> Series:
    return name_series.str.upper()


def only_letters(name_series: Series) -> Series:
    return name_series.str.replace(r"([^A-Z])", " ", regex=True)


def remove_hospital_trigram(name_series: Series) -> Series:
    return name_series.str.replace(r"^([A-Z]{3}\W)", "", regex=True)


def remove_hierarchy_litteral(name_series: Series) -> Series:
    return name_series.str.replace(r"\bUF\b|\bUMA\b", "", regex=True)


def simplify_spaces(name_series: Series) -> Series:
    return name_series.str.replace(r"\s+", " ", regex=True).str.strip()
