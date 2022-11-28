<div align="center">

<p align="center">
  <a href="https://datasciencetools-pages.eds.aphp.fr/eds-scikit"><img src="docs/_static/scikit_logo_text.svg" width="30%"></a>
</p>

#

<p align="center">
<a href="https://datasciencetools-pages.eds.aphp.fr/eds-scikit/" target="_blank">
    <img src="https://img.shields.io/badge/docs-passed-brightgreen" alt="Documentation">
</a>
<a href="https://gitlab.eds.aphp.fr/datasciencetools/eds-scikit/-/commits/master" target="_blank">
    <img src="https://gitlab.eds.aphp.fr/datasciencetools/eds-scikit/badges/master/pipeline.svg" alt="Pipeline Status">
</a>
<a href="https://gitlab.eds.aphp.fr/datasciencetools/eds-scikit/-/jobs/artifacts/master/file/htmlcov/index.html?job=run%20pytest" target="_blank">
    <img src="https://gitlab.eds.aphp.fr/datasciencetools/eds-scikit/badges/master/coverage.svg" alt="Coverage">
</a>
<a href="https://github.com/psf/black" target="_blank">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Black">
</a>
<!-- <a href="https://python-poetry.org/" target="_blank">
    <img src="https://img.shields.io/badge/reproducibility-poetry-blue" alt="Poetry">
</a> -->
<a href="https://www.python.org/" target="_blank">
    <img src="https://img.shields.io/badge/python-%3E%3D%203.7.1%20%7C%20%3C%203.8-brightgreen" alt="Supported Python versions">
</a>
<a href="https://chat.eds.aphp.fr/#narrow/stream/154-SciKit-EDS" target="_blank">
    <img src="https://gitlab.eds.aphp.fr/datasciencetools/eds-scikit/-/raw/master/docs/_static/chat_badge.svg" alt="Chat">
</a>
</p>
</div>


SciKit-EDS has been initiated as a tool to assist datascientists working on the AP-HP's Clinical Data Warehouse. It is specifically targeted for OMOP-standardized data. It main goals are to:

- Ease access and analysis of data
- Allow a better transfer of knowledge between projects
- Improve research reproduciblity

## Development

This library is developed and maintained
by the core team of AP-HP’s Clinical Data Warehouse (EDS) with the strong support of Inria Parietal team.

## How to use

Please check the [online documentation](https://datasciencetools-pages.eds.aphp.fr/eds-scikit/documentation/) for more informations. You will find
- Detailed explanation of the project goal and working principles
- A complete API documentation
- Various Jupyter Notebooks describing how to use various functionnalities of SciKit-EDS
- And more !
## Requirements
EDS-Scikit stands on the shoulders of [Spark 2.4](https://spark.apache.org/docs/2.4.8/index.html) which requires:

- Python ~3.7.1
- Java 8
## Installation

To install the library, first clone the repo:

```bash
git clone https://gitlab.eds.aphp.fr/datasciencetools/eds-scikit.git
```

Then install the library using pip

```bash
cd eds-scikit
pip install ".[aphp]"
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

Please check our [contributing guidelines](https://datasciencetools-pages.eds.aphp.fr/eds-scikit/documentation/contributing.html).

For AP-HP users, also feel free to use the dedicated [Zulip channel](https://chat.eds.aphp.fr/#narrow/stream/154-SciKit-EDS). (If you need a permission to join the channel, simply [message one of the developper](https://chat.eds.aphp.fr/#narrow/pm-with/351-thomas.petitjean-ext))

### Acknowledgment

We would like to thank the following funders:
- Assistance Publique – Hôpitaux de Paris
- AP-HP Foundation
