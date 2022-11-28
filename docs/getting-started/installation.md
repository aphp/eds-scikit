# Installation

## From APHP's GitLab

For the moment, `eds-scikit` is available only on AP-HP's GitLab. To install the library, first clone the repo:

```bash
git clone https://gitlab.eds.aphp.fr/datasciencetools/eds-scikit.git
```

Then install the library using pip

```bash
cd eds-scikit
pip install ".[aphp]"
```

## (Coming soon) From pip

To install eds_scikit, run this command in your terminal:

```bash
pip install "eds_scikit[aphp]"
```

This is the preferred method to install eds_scikit, as it will always install the most recent stable release.

If you don't have [pip](https://pip.pypa.io) installed, this [Python installation guide](http://docs.python-guide.org/en/latest/starting/installation/) can guide you through the process.

## Testing

Check the [tests](../contributing.md#Running-tests)
