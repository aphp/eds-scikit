# Contributing

We welcome contributions! There are many ways to help. For example, you can:

1. Help us track bugs by filing issues
2. Suggest and help prioritise new functionalities
3. Develop a new functionality!
4. Help us make the library as straightforward as possible, by simply asking questions on whatever does not seem clear to you.

Please do not hesitate to suggest functionalities you have developed and want to incorporate into eds-scikit. We will be glad to help!
Also, any non-technical contribution (e.g. lists of ICD-10 codes curated for a research project) is also welcome.

## Development installation

To be able to run the test suite, run the example notebooks and develop your own functionalities, you should clone the repo and install it locally.

!!! warning "Spark and Java"
    To run tests locally, you need to have Spark and Java. Whereas Spark will be installed as a dependency of PySpark, you may need to install Java yourself. Please check to [installation][installation] procedure.

<div class="termy">

```console
# Clone the repository and change directory
$ git clone https://github.com/aphp/eds-scikit.git
---> 100%
$ cd eds-scikit

# Create a virtual environment
$ python -m venv venv
$ source venv/bin/activate

# Install dependencies and build resources
$ pip install -r requirements.txt

# Install development dependencies
$ pip install -r requirements_dev.txt
$ pip install -r requirements_docs.txt

# Finally, install the package in editable mode...
$ pip install -e .

# And switch to a new branch to begin developping
$ git switch -c "name_of_my_new_branch"
```

</div>

To make sure the pipeline will not fail because of formatting errors, we added pre-commit hooks using the `pre-commit` Python library. To use it, simply install it:

<div class="termy">

```console
$ pre-commit install
```

</div>

The pre-commit hooks defined in the [configuration](https://github.com/aphp/eds-scikit/blob/master/.pre-commit-config.yaml) will automatically run when you commit your changes, letting you know if something went wrong.

The hooks only run on staged changes. To force-run it on all files, run:

<div class="termy">

```console
$ pre-commit run --all-files
---> 100%
color:green All good !
```

</div>

## Proposing a merge request

At the very least, your changes should :

- Be well-documented ;
- Pass every tests, and preferably implement its own ;
- Follow the style guide.

### Testing your code

We use the Pytest test suite.

The following command will run the test suite. Writing your own tests is encouraged!

```shell
python -m pytest ./tests
```

Most tests are designed to run both with Pandas as Koalas DataFrames as input. However, to gain time, by default only Pandas testing is done. The above line of code is equivalent to

```bash
python -m pytest ./tests -m "not koalas"
```

However, you can also run tests using only Koalas input:

```bash
python -m pytest ./tests -m "koalas"
```

or using both inputs:

```bash
python -m pytest ./tests -m ""
```

Finally when developing, you might be interested to run tests for a single file, or even a single function. To do so:

```bash
python -m pytest ./tests/my_file.py #(1)
python -m pytest ./tests/my_file.py:my_test_function #(2)
```
1. Will run all tests found in this file
2. Will only run "my_test_function"

### Style Guide

We use [Black](https://github.com/psf/black) to reformat the code. While other formatter only enforce PEP8 compliance, Black also makes the code uniform. In short :

> Black reformats entire files in place. It is not configurable.

Moreover, the CI/CD pipeline enforces a number of checks on the "quality" of the code. To wit, non black-formatted code will make the test pipeline fail. We use `pre-commit` to keep our codebase clean.

Refer to the [development install tutorial](#development-installation) for tips on how to format your files automatically.
Most modern editors propose extensions that will format files on save.

!!! tip "On *conventional commits*"
    We try to use [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/#summary) guidelines as much as possible. In short, prepend each commit message with one of the following prefix:

    - `fix:` when patching a bug
    - `feat:` when introducing a new feature
    - If needed, you can also use one of the following: `build:, chore:, ci:, docs:, style:, refactor:, perf:, test`

### Documentation

Make sure to document your improvements, both within the code with comprehensive docstrings,
as well as in the documentation itself if need be.

We use `MkDocs` for eds-scikit's documentation. You can checkout the changes you make with:

<div class="termy">

```console
# Install the requirements
$ pip install ".[doc]"
---> 100%
color:green Installation successful

# Run the documentation
$ mkdocs serve
```

</div>

Go to [`localhost:8000`](http://localhost:8000) to see your changes. MkDocs watches for changes in the documentation folder
and automatically reloads the page.

!!! warning
    MkDocs will automaticaly build code documentation by going through every `.py` file located in the `eds_scikit` directory (and sub-arborescence). It expects to find a `__init__.py` file in each directory, so make sure to create one if needed.
