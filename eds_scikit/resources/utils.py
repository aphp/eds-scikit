from typing import Optional


def versionize(algo: str) -> Optional[str]:
    """
    Extract, if found,  the version substring of an algorithm name.

    Parameters
    ----------
    algo : str
        Of the form "<algo_name>" or "<algo_name>.<version>"

    Returns
    -------
    Optional[str]
        The algo version suffix
    """
    splited = algo.split(".")
    if len(splited) == 1:
        return None
    return splited[-1]
