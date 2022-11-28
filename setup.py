"""The setup script."""

from setuptools import find_packages, setup

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.readlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def get_version(path):
    with open(path, "r") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split('"')[1]
    raise RuntimeError("Unable to find version string.")


setup(
    name="eds_scikit",
    author="DSN AP-HP (Data Science Team), Inria (SODE Team)",
    author_email="thomas.petitjean@aphp.fr",
    version=get_version("eds_scikit/__init__.py"),
    description="Simplify data analysis of OMOP data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.7, <3.8",
    install_requires=requirements,
    extras_require={"aphp": ["eds-scikit-aphp"]},
    license="BSD license",
    packages=find_packages(include=["eds_scikit", "eds_scikit.*"]),
    package_dir={"": "."},
    package_data={"": ["*.csv"]},
)
