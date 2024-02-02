# Visualization

This library provides visualizations tools that aggregates computed measurements to provide two interactive dashboards and a summary table describing various statistical properties of your biological data.

!!! tip "Those visualizations were designed to facilitate measurement table analysis and identify possible bias."
    Feel free to contribute by suggesting other visualizations.


## Plot biology summary

`plot_biology_summary()` creates a folder for each concepts-set computed through `plot_biology_summary()`. For instance, let us see what you will find in the folder *Glucose_Blood_Quantitative*`.

### Summary table

A statistical summary table as below:


--8<-- "_static/biology/viz/stats_summary.html"


### Volumetry dashboard

An interactive dashboard describing the volumety properties over time.

An example is available [here](../../_static/biology/viz/interactive_volumetry.html).


### Distribution dashboard

An interactive dashboard describing the distribution properties.

An example is available [here](../../_static/biology/viz/interactive_distribution.html).
