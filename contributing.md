# Contributing

Contributions are welcome and are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

## Types of contributions

Contributions are centralized around a dedicated [Collaboration board](https://gitlab.eds.aphp.fr/datasciencetools/eds-scikit/-/boards/304).
Three categories are available:


### ![alt text](./_static/bug_report.png) You found a bug

The library being still in development, bugs might still be around. Feel free to report them to the dev team using the dedicated issue label.

### ![alt text](./_static/question.png) You have a question about an implementation in the library

The source code of each functionality is available in the documentation (check `Code Reference`). However, if you have a question about the content of a function from this library, please leave an issue there.

### ![alt text](./_static/suggestion.png) You have a suggestion for implementing a new functionnality to the library

We are highly interested in contributions to enhance EDS-Scikit. If you believe that some developments you made could benefit the rest of the community by being implemented in the library, leave an issue here to open a discussion.
If you feel like it, you can also directly contribute to the library by following the contribution guidelines just below.

## Guidelines

### Creating a development environment
Ready to contribute? Here's how to set up `eds_scikit` for local development.

!!! warning
     If you're developping locally, ie outside AP-HP's Jupyter servers, you may need to [install Java 8](https://docs.oracle.com/javase/8/docs/technotes/guides/install/install_overview.html) in order for Koalas to work properly.


1. Fork the `eds_scikit` repo.
2. Clone your fork locally:

    ```bash
    git clone git@github.com:your_name_here/eds_scikit.git
    ```

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development:

    ```bash
    mkvirtualenv eds_scikit
    cd eds_scikit/
    python setup.py develop
    ```

4. Install dev-specific requirements:

    ```bash
    pip install -r requirements_dev.txt
    ```

5. Create a branch for local development:

    ```bash
    git checkout -b name-of-your-bugfix-or-feature
    ```

6. When you're done making changes, format your code using black,
   check that your changes pass flake8 and the tests, including testing other Python versions with tox:

    ```bash
    black eds_scikit
    flake8 eds_scikit tests
    python setup.py test or pytest
    tox
    ```

7. Commit your changes and push your branch

    ```bash
    git add .
    git commit -m "Your detailed description of your changes."
    git push origin name-of-your-bugfix-or-feature
    ```
8. Submit a pull request.


### Running tests

To run the tests:

```bash
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
python -m pytest ./tests/my_file.py #Will run all tests found in this file
python -m pytest ./tests/my_file.py:my_test_function #Will only run "my_test_function"
```

!!! info "Running tests locally in a Docker image"

    - If you want to use **Docker** to run tests locally in a way that matches what GitLab-CI runs:
        - Build the docker image :`docker-compose -f tests/automation/docker-compose.yml build`
        - Run tests in the docker image: `docker-compose -f tests/automation/docker-compose.yml run python-tests`
    - You may need to run the command ``pyclean eds_scikit tests`` to erase binary files produced by python/pytest. They contain path to python files that are different in docker and on your local machine. (Error is ``py._path.local.LocalPath.ImportMismatchError``)
