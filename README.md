<div align="center">

<p align="center">
  <a href="https://aphp.github.io/eds-scikit/">
    <img src="https://github.com/aphp/eds-scikit/raw/main/docs/_static/scikit_logo_text.png" width="30%" onerror="this.style.display='none'">
  </a>
</p>

#

<p align="center">

![Tests](https://img.shields.io/github/actions/workflow/status/aphp/eds-scikit/testing.yml?branch=main&label=tests&style=flat-square)
[![Documentation](https://img.shields.io/github/actions/workflow/status/aphp/eds-scikit/publish_doc.yml?branch=main&label=docs&style=flat-square)](https://aphp.github.io/eds-scikit/latest/)
[![PyPI](https://img.shields.io/pypi/v/eds-scikit?color=blue&style=flat-square)](https://pypi.org/project/eds-scikit/)
[![Supported Python](https://img.shields.io/badge/python-%3E%3D%203.7.1%20%7C%20%3C%203.8-brightgreen?style=flat-square)](https://www.python.org/)
[![Black](https://img.shields.io/badge/code%20style-black-black?style=flat-square)]([https://www.python.org/](https://github.com/psf/black))
[![Coverage](https://raw.githubusercontent.com/aphp/eds-scikit/coverage/coverage.svg)](https://raw.githubusercontent.com/aphp/eds-scikit/coverage/coverage.txt)
[![DOI](https://zenodo.org/badge/571584236.svg)](https://zenodo.org/badge/latestdoi/571584236&style=flat-square)

</p>
</div>


eds-scikit is a tool to assist data scientists working on the AP-HP's Clinical Data Warehouse. It is specifically targeted for OMOP-standardized data. It main goals are to:

- Ease access and analysis of data
- Allow a better transfer of knowledge between projects
- Improve research reproducibility

## Development

This library is developed and maintained by the core team of AP-HP’s Clinical Data Warehouse (EDS) with the strong support of [Inria's SODA team](https://team.inria.fr/soda/).

## How to use

Please check the [online documentation](https://aphp.github.io/eds-scikit/) for more informations. You will find
- Detailed explanation of the project goal and working principles
- A complete API documentation
- Various Jupyter Notebooks describing how to use various functionnalities of eds-scikit
- And more !
## Requirements
eds-scikit stands on the shoulders of [Spark 2.4](https://spark.apache.org/docs/2.4.8/index.html) which requires:

- Python ~3.7.1
- Java 8
## Installation

You can install eds-scikit via `pip`:

```bash
pip install "eds-scikit[aphp]"
```

:warning: If you get an an error during installation, please try downgrading pip via `pip install -U "pip<23" before install `eds-scikit`

:warning: If you don't work in AP-HP's ecosystem (EDS), please install via:

```bash
pip install eds-scikit
```

You can now import the library via

```python
import eds_scikit
```
### Contributing

- You want to help on the project ?
- You developped an interesting feature and you think it could benefit other by being integrated in the library ?
- You found a bug ?
- You have a question about the library ?
- ...

Please check our [contributing guidelines](https://aphp.github.io/eds-scikit/contributing/).

### Citation

If you use `eds-scikit`, please cite us as below.

```bibtex
@misc{eds-scikit,
    author = {Petit-Jean, Thomas and Remaki, Adam and Maladière, Vincent and Varoquaux, Gaël and Bey, Romain},
    doi = {10.5281/zenodo.7401549},
    title = {eds-scikit: data analysis on OMOP databases},
    url = {https://github.com/aphp/eds-scikit}
}
```

### Acknowledgment

We would like to thank the following funders:
- [Assistance Publique – Hôpitaux de Paris](https://www.aphp.fr/)
- [AP-HP Foundation](https://fondationrechercheaphp.fr/)
- [Inria](https://www.inria.fr)
