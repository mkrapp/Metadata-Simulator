# RDM-Simulator

RDM (Research Data Management) simulator generates a set of dummy data projects and create a summary report.

# What? Why?

I want run a datamanagement simulation to understand how to get from an uncurated dataset to a curated dataset and what steps one has to take to lift up your data, for example, to make it [FAIR](https://en.wikipedia.org/wiki/FAIR_data).

# Requirements

Before we can do anything, we have to create a `conda` environment with the required packages

```
conda env create --file environment.yml
```

# Simulation


We want to simulte what we have to do to create a datasets that complies with certain good data management principles.
For example, we can check if certain files, such as the actual data and some supporting metadata exist and how they relate to our principles and actions.

| **Principle/Action**                        | **Fields to Check**                                                                                       |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **Ensure FAIR Principles**                  | `name`, `title`, `description`, `homepage`, `resources.path`, `resources.format`, `resources.schema.fields`, `licenses`, `schema.primaryKey` |
| **Document Metadata and Provenance**        | `description`, `keywords`, `version`, `licenses`, `schema.fields`, `contributors` (if applicable)         |
| **Review and Validate Data**                | `resources.path`, `resources.format`, `schema.fields`, `primaryKey`, ensure the dataset matches the schema |


## Generate project datasets

First, let's generate some data projects, `rock_types`, `pm25_timeseries`, `borehole_data`, and `fossil_records`:

```
python generate_data_projects.py
```

Next, create a summary report from all projects
```
python generate_report.py
```

Here's how the Markdown table from the generated file `summary_report.md` (`cat data_projects/summary_report.md`) looks like

| Project         | Define the Scope of Data   | Choose Open Data Formats   | Ensure FAIR Principles   | Document Metadata and Provenance   | Review and Validate Data   | Publish and Share Data   | Periodic Review and Updates   | Metadata File Check   |
|:----------------|:---------------------------|:---------------------------|:-------------------------|:-----------------------------------|:---------------------------|:-------------------------|:------------------------------|:----------------------|
| rock_types      | ✘                          | ✘                          | ✘                        | ✘                                  | ✘                          | ✘                        | ✘                             | Failed                |
| pm25_timeseries | ✘                          | ✘                          | ✘                        | ✘                                  | ✘                          | ✘                        | ✘                             | Failed                |
| borehole_data   | ✘                          | ✘                          | ✘                        | ✘                                  | ✘                          | ✘                        | ✘                             | Failed                |
| fossil_records  | ✘                          | ✘                          | ✘                        | ✘                                  | ✘                          | ✘                        | ✘                             | Failed                |


## Update the `borehole_data` project

Now, we are "fixing" the data for `borehole_data` project.

```
python generate_borehole_data.py
```

Re-running the report

```
python generate_report.py
```

to generate `summary_report.md`:

| Project         | Define the Scope of Data   | Choose Open Data Formats   | Ensure FAIR Principles   | Document Metadata and Provenance   | Review and Validate Data   | Publish and Share Data   | Periodic Review and Updates   | Metadata File Check   |
|:----------------|:---------------------------|:---------------------------|:-------------------------|:-----------------------------------|:---------------------------|:-------------------------|:------------------------------|:----------------------|
| rock_types      | ✘                          | ✘                          | ✘                        | ✘                                  | ✘                          | ✘                        | ✘                             | Failed                |
| pm25_timeseries | ✘                          | ✘                          | ✘                        | ✘                                  | ✘                          | ✘                        | ✘                             | Failed                |
| borehole_data   | ✔                          | ✔                          | ✔                        | ✔                                  | ✔                          | ✔                        | ✔                             | Passed                |
| fossil_records  | ✘                          | ✘                          | ✘                        | ✘                                  | ✘                          | ✘                        | ✘                             | Failed                |

## Add missing metadata for the `bore_data` project


There is still some metadata missing. We need to "fix" the FAIR section in our `datapackage.yaml`. Let's copy a complete metadata version into the right place

```
cp borehole_datapackage.yaml data_projects/borehole_data/datapackage.yaml
```

Here's how that file looks like:

```yaml
name: borehole_data
title: Borehole Data
description: A dataset containing information about boreholes, including their ID, location, depth, date drilled, and driller.
version: '1.0'
keywords:
  - borehole
  - geology
  - drilling
homepage: https://example.com/borehole-data
licenses:
  - name: Open Data Commons Public Domain Dedication and License (PDDL)
    path: https://opendatacommons.org/licenses/pddl/
resources:
  - name: boreholes
    path: raw-data/borehole_data.csv
    format: csv
    profile: tabular-data-resource
    schema:
      fields:
        - name: BoreholeID
          type: string
          description: Unique identifier for the borehole
        - name: Location
          type: string
          description: Geographic location of the borehole
        - name: Depth
          type: number
          description: Depth of the borehole in meters
        - name: DateDrilled
          type: date
          description: Date when the borehole was drilled
        - name: Driller
          type: string
          description: Name of the person who drilled the borehole
      primaryKey: BoreholeID
```

Let's re-generate the report

```
python generate_report.py
```

to generate `summary_report.md`:


| Project         | Define the Scope of Data   | Choose Open Data Formats   | Ensure FAIR Principles   | Document Metadata and Provenance   | Review and Validate Data   | Publish and Share Data   | Periodic Review and Updates   | Metadata File Check   |
|:----------------|:---------------------------|:---------------------------|:-------------------------|:-----------------------------------|:---------------------------|:-------------------------|:------------------------------|:----------------------|
| rock_types      | ✘                          | ✘                          | ✘                        | ✘                                  | ✘                          | ✘                        | ✘                             | Failed                |
| pm25_timeseries | ✘                          | ✘                          | ✘                        | ✘                                  | ✘                          | ✘                        | ✘                             | Failed                |
| borehole_data   | ✔                          | ✔                          | ✔                        | ✔                                  | ✔                          | ✔                        | ✔                             | Passed                |
| fossil_records  | ✘                          | ✘                          | ✘                        | ✘                                  | ✘                          | ✘                        | ✘                             | Failed                |

All entries are now complete for the `borehole_data` project. Mission accomplished.

At this stage, our project folders are looking like this:

```
data_projects/
├── borehole_data
│   ├── datapackage.yaml
│   ├── processed-data
│   ├── raw-data
│   │   └── borehole_data.csv
│   ├── reports
│   └── scripts
├── fossil_records
│   ├── processed-data
│   ├── raw-data
│   │   └── fossil_records.csv
│   ├── reports
│   └── scripts
├── pm25_timeseries
│   ├── processed-data
│   ├── raw-data
│   │   └── pm25_timeseries.csv
│   ├── reports
│   └── scripts
├── rock_types
│   ├── processed-data
│   ├── raw-data
│   │   └── rock_types.geojson
│   ├── reports
│   └── scripts
└── summary_report.md
```
