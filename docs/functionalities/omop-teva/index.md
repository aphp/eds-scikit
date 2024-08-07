# OMOP Teva

The OMOP Teva module of [eds-scikit](https://github.com/aphp/eds-scikit) supports data scientists working on OMOP data.
OMOP Teva generates an interactive dashboard for each OMOP table, allowing __timely visualization of the volumes__ associated with each combination of values. This provides a general overview of the possible values, their relative importance and allows to __detect quickly possible bias__.

!!! warning "This module is an eds-scikit transposition of [EDS-Teva](https://github.com/aphp/edsteva)"
    [EDS-Teva](https://github.com/aphp/edsteva) is a more complete library designed to handle temporal bias in EHR data. See [Adjusting for the progressive digitization of health records](https://www.medrxiv.org/content/10.1101/2023.08.17.23294220v1) for a better understanding about those bias.

```vegalite
{
    "$schema": "https://vega.github.io/schema/vega-lite/v5.8.0.json",
    "config": {
      "view": {
        "continuousHeight": 300,
        "continuousWidth": 300
      }
    },
    "data": {
      "name": "data-54870d255b2c7e93f9c75f03839955f2"
    },
    "datasets": {
      "data-54870d255b2c7e93f9c75f03839955f2": [
        {
          "care_site_short_name": "care site 1",
          "count": 17,
          "datetime": "2021-01-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 14,
          "datetime": "2021-01-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 12,
          "datetime": "2021-01-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 6,
          "datetime": "2021-01-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 2,
          "datetime": "2021-01-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 1,
          "datetime": "2021-01-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 6,
          "datetime": "2021-01-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 10,
          "datetime": "2021-01-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 12,
          "datetime": "2021-01-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 24,
          "datetime": "2021-02-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 21,
          "datetime": "2021-02-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 17,
          "datetime": "2021-02-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 4,
          "datetime": "2021-02-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 2,
          "datetime": "2021-02-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 8,
          "datetime": "2021-02-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 5,
          "datetime": "2021-02-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 8,
          "datetime": "2021-02-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 14,
          "datetime": "2021-03-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 13,
          "datetime": "2021-03-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 17,
          "datetime": "2021-03-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 6,
          "datetime": "2021-03-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 4,
          "datetime": "2021-03-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 9,
          "datetime": "2021-03-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 5,
          "datetime": "2021-03-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 6,
          "datetime": "2021-03-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 14,
          "datetime": "2021-04-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 15,
          "datetime": "2021-04-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 8,
          "datetime": "2021-04-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 5,
          "datetime": "2021-04-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 5,
          "datetime": "2021-04-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 2,
          "datetime": "2021-04-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 12,
          "datetime": "2021-04-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 9,
          "datetime": "2021-04-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 4,
          "datetime": "2021-04-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 25,
          "datetime": "2021-05-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 12,
          "datetime": "2021-05-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 15,
          "datetime": "2021-05-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 1,
          "datetime": "2021-05-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 2,
          "datetime": "2021-05-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 2,
          "datetime": "2021-05-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 10,
          "datetime": "2021-05-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 9,
          "datetime": "2021-05-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 8,
          "datetime": "2021-05-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 18,
          "datetime": "2021-06-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 13,
          "datetime": "2021-06-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 14,
          "datetime": "2021-06-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 1,
          "datetime": "2021-06-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 1,
          "datetime": "2021-06-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 4,
          "datetime": "2021-06-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 5,
          "datetime": "2021-06-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 10,
          "datetime": "2021-06-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 6,
          "datetime": "2021-06-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 23,
          "datetime": "2021-07-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 23,
          "datetime": "2021-07-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 11,
          "datetime": "2021-07-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 6,
          "datetime": "2021-07-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 2,
          "datetime": "2021-07-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 3,
          "datetime": "2021-07-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 13,
          "datetime": "2021-07-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 10,
          "datetime": "2021-07-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 5,
          "datetime": "2021-07-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 24,
          "datetime": "2021-08-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 22,
          "datetime": "2021-08-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 10,
          "datetime": "2021-08-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 1,
          "datetime": "2021-08-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 5,
          "datetime": "2021-08-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 3,
          "datetime": "2021-08-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 8,
          "datetime": "2021-08-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 11,
          "datetime": "2021-08-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 9,
          "datetime": "2021-08-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 20,
          "datetime": "2021-09-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 17,
          "datetime": "2021-09-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 21,
          "datetime": "2021-09-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 3,
          "datetime": "2021-09-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 2,
          "datetime": "2021-09-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 2,
          "datetime": "2021-09-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 12,
          "datetime": "2021-09-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 9,
          "datetime": "2021-09-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 6,
          "datetime": "2021-09-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 23,
          "datetime": "2021-10-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 21,
          "datetime": "2021-10-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 19,
          "datetime": "2021-10-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 4,
          "datetime": "2021-10-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 3,
          "datetime": "2021-10-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 3,
          "datetime": "2021-10-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 7,
          "datetime": "2021-10-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 8,
          "datetime": "2021-10-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 8,
          "datetime": "2021-10-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 27,
          "datetime": "2021-11-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 14,
          "datetime": "2021-11-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 10,
          "datetime": "2021-11-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 3,
          "datetime": "2021-11-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 4,
          "datetime": "2021-11-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 2",
          "count": 1,
          "datetime": "2021-11-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 8,
          "datetime": "2021-11-01T00:00:00",
          "stay_source_value": "MCO"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 6,
          "datetime": "2021-11-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 3",
          "count": 4,
          "datetime": "2021-11-01T00:00:00",
          "stay_source_value": "PSY"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 1,
          "datetime": "2021-12-01T00:00:00",
          "stay_source_value": "Other"
        },
        {
          "care_site_short_name": "care site 1",
          "count": 1,
          "datetime": "2021-12-01T00:00:00",
          "stay_source_value": "PSY"
        }
      ]
    },
    "params": [
      {
        "bind": "legend",
        "name": "param_7",
        "select": {
          "clear": "dblclick",
          "fields": [
            "care_site_short_name"
          ],
          "on": "click",
          "type": "point"
        },
        "views": [
          "view_7"
        ]
      },
      {
        "bind": "legend",
        "name": "param_8",
        "select": {
          "clear": "dblclick",
          "fields": [
            "stay_source_value"
          ],
          "on": "click",
          "type": "point"
        },
        "views": [
          "view_8"
        ]
      }
    ],
    "resolve": {
      "scale": {
        "color": "independent"
      }
    },
    "vconcat": [
      {
        "hconcat": [
          {
            "encoding": {
              "color": {
                "field": "care_site_short_name",
                "scale": {
                  "domain": [
                    "care site 1",
                    "care site 2",
                    "care site 3"
                  ],
                  "range": [
                    "#1f77b4",
                    "#ff7f0e",
                    "#2ca02c"
                  ]
                },
                "type": "nominal"
              },
              "opacity": {
                "condition": {
                  "param": "param_7",
                  "value": 1
                },
                "value": 0.3
              },
              "tooltip": [
                {
                  "field": "care_site_short_name",
                  "type": "nominal"
                }
              ],
              "x": {
                "aggregate": "sum",
                "field": "count",
                "type": "quantitative"
              }
            },
            "mark": {
              "type": "bar"
            },
            "name": "view_7",
            "transform": [
              {
                "filter": {
                  "param": "param_8"
                }
              }
            ]
          },
          {
            "encoding": {
              "color": {
                "field": "care_site_short_name",
                "scale": {
                  "domain": [
                    "care site 1",
                    "care site 2",
                    "care site 3"
                  ],
                  "range": [
                    "#1f77b4",
                    "#ff7f0e",
                    "#2ca02c"
                  ]
                },
                "type": "nominal"
              },
              "opacity": {
                "condition": {
                  "param": "param_7",
                  "value": 1
                },
                "value": 0.3
              },
              "x": {
                "field": "datetime",
                "timeUnit": "yearmonth",
                "type": "temporal"
              },
              "y": {
                "aggregate": "sum",
                "axis": {
                  "format": "s"
                },
                "field": "count",
                "type": "quantitative"
              }
            },
            "height": 50,
            "mark": {
              "type": "line"
            },
            "transform": [
              {
                "filter": {
                  "param": "param_8"
                }
              }
            ],
            "width": 300
          }
        ],
        "title": "care_site_short_name"
      },
      {
        "hconcat": [
          {
            "encoding": {
              "color": {
                "field": "stay_source_value",
                "scale": {
                  "domain": [
                    "MCO",
                    "Other",
                    "PSY"
                  ],
                  "range": [
                    "#1f77b4",
                    "#ff7f0e",
                    "#2ca02c"
                  ]
                },
                "type": "nominal"
              },
              "opacity": {
                "condition": {
                  "param": "param_8",
                  "value": 1
                },
                "value": 0.3
              },
              "tooltip": [
                {
                  "field": "stay_source_value",
                  "type": "nominal"
                }
              ],
              "x": {
                "aggregate": "sum",
                "field": "count",
                "type": "quantitative"
              }
            },
            "mark": {
              "type": "bar"
            },
            "name": "view_8",
            "transform": [
              {
                "filter": {
                  "param": "param_7"
                }
              }
            ]
          },
          {
            "encoding": {
              "color": {
                "field": "stay_source_value",
                "scale": {
                  "domain": [
                    "MCO",
                    "Other",
                    "PSY"
                  ],
                  "range": [
                    "#1f77b4",
                    "#ff7f0e",
                    "#2ca02c"
                  ]
                },
                "type": "nominal"
              },
              "opacity": {
                "condition": {
                  "param": "param_8",
                  "value": 1
                },
                "value": 0.3
              },
              "x": {
                "field": "datetime",
                "timeUnit": "yearmonth",
                "type": "temporal"
              },
              "y": {
                "aggregate": "sum",
                "axis": {
                  "format": "s"
                },
                "field": "count",
                "type": "quantitative"
              }
            },
            "height": 50,
            "mark": {
              "type": "line"
            },
            "transform": [
              {
                "filter": {
                  "param": "param_7"
                }
              }
            ],
            "width": 300
          }
        ],
        "title": "stay_source_value"
      }
    ]
  }
```

<!-- --8<-- [start:omop-teva] -->

=== card {: href=/functionalities/omop-teva/quick-use-omop }

    :fontawesome-solid-file-medical:
    **OMOP Teva - Quick use**

    ---

    Quick use for OMOP dataset exploration.

=== card {: href=/functionalities/omop-teva/configuration-omop }

    :fontawesome-solid-gears:
    **OMOP Teva - Config**

    ---

    See how your can configurate your own OMOP dashboards .

=== card {: href=/functionalities/omop-teva/custom-teva }

    :fontawesome-solid-file:
    **Custom Teva**

    ---

    For any dataframe exploration.

=== card {: href=/functionalities/omop-teva/omop-teva-example }

    :fontawesome-solid-chart-line:
    **OMOP Teva - Example**

    ---

    A toy example of what can be obtained with this module.



<!-- --8<-- [end:omop-teva] -->
