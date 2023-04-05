# Changelog

## v0.1.5 (2023-04-05)

### Added

- BaseData class as a parent class for HiveData, PandasData and PostgresData
- Phentyping class with 4 implemented phenotyes
- Custom logger to display useful information during computation

### Fixed

- Add caching to speedup computations
- Updated method to persist tables as parquet locally, with a support for ORC-stored I2B2 database


## v0.1.4 (2023-02-09)

### Added

- Allow saving DB locally in client or cluster mode
- Add data cleaning function to handle incorrect datetime in spark
- Filter biology config on care site

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
