# Changelog

## Unreleased

### Fixed
- Fix merge_visits sort_values.groupby.first

## v0.1.8 (2024-06-13)

### Fixed
- Pyarrow fix now work on spark executors.
- Fix OMOP _date columns issue

### Added
- omop teva module

## v0.1.7 (2024-04-12)
### Changed
- Support for pyarrow > 0.17.0

### Added
- biology module refacto
- load_koalas() not by default in __init__.py but called in the improve_performance function
- adding app_name in improve_performances to facilitate app monitoring

### Fixed
- Generation of an inclusion/exclusion flowchart in plotting
- improve_performance moved from __init__.py to io/improve_performance.py file
- Caching in spark instead of koalas to improve speed

## v0.1.6 (2023-09-27)

### Added
- Module ``event_sequences`` to visualize individual sequences of events.
- Module ``age_pyramid`` to quickly visualize the age and gender distributions in a cohort.
### Fixed
- Compatibility with [EDS-TeVa](https://github.com/aphp/edsteva) and [EDSNLP](https://github.com/aphp/edsnlp).

## v0.1.5 (2023-04-05)

### Added

- BaseData class as a parent class for HiveData, PandasData and PostgresData.
- Phentyping class with 4 implemented phenotyes.
- Custom logger to display useful information during computation.

### Fixed

- Add caching to speedup computations.
- Updated method to persist tables as parquet locally, with a support for ORC-stored I2B2 database.


## v0.1.4 (2023-02-09)

### Added

- Allow saving DB locally in client or cluster mode.
- Add data cleaning function to handle incorrect datetime in spark.
- Filter biology config on care site.
- Adding person-dependent `datetime_ref` to `plot_age_pyramid`.

### Fixed

- Consultations date for OMOP & I2B2


## v0.1.3 (2023-02-02)

### Added

- New BackendDispatcher to handle framework-specific functions
- I2B2 to OMOP connector

## v0.1.2 (2022-12-05)

### Added

- Adding CITATION.cff
- Using `mike` as a documentation provider

### Fixed

- Correct build to PyPI
- Renaming from `EDS-Scikit` to `eds-scikit`

## v0.1.1 (2022-12-02)

### Added
- Various project metadata
- Full CI pipeline
- License checker in CI
- BackendDispatcher object to help with pandas / koalas manipulation

### Fixed

- Broken links in documentation and badges

## v0.1.0 (2022-12-01)

### Added

- Initial commit to GitHub
