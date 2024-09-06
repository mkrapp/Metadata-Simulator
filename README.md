# Metadata-Simulator

Generate a set of dummy data projects and create a summary report.

# What? Why?

I want run a datamanagement simulation to understand how to get from an uncurated dataset to a curated dataset and what steps one has to take to lift up your data, for example, to make it [FAIR](https://en.wikipedia.org/wiki/FAIR_data).

## Example `datapackage.yaml`

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

## Summary Table of Fields to Check

| **Principle/Action**                        | **Fields to Check**                                                                                       |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **Ensure FAIR Principles**                  | `name`, `title`, `description`, `homepage`, `resources.path`, `resources.format`, `resources.schema.fields`, `licenses`, `schema.primaryKey` |
| **Utilize Cloud or Network Storage**        | `resources.path` (should be accessible and correctly point to cloud or network storage locations)         |
| **Involve Data Manager and Experts**        | Ensure comprehensive metadata; include documentation on contributors or managers if available              |
| **Document Metadata and Provenance**        | `description`, `keywords`, `version`, `licenses`, `schema.fields`, `contributors` (if applicable)         |
| **Review and Validate Data**                | `resources.path`, `resources.format`, `schema.fields`, `primaryKey`, ensure the dataset matches the schema |

By following these guidelines, you can ensure that your dataset’s `datapackage.yaml` is robust, adheres to best practices, and aligns with the principles of FAIR data.

# Simulation

```
python generate_data_projects.py
```

Next, create a summary report
```
python generate_report.py
```

The generated file `summary_report.md`  (`cat data_projects/summary_report.md`) looks like

| Project         | Define the Scope of Data   | Choose Open Data Formats   | Ensure FAIR Principles   | Utilize Cloud or Network Storage   | Involve Data Manager and Experts   | Document Metadata and Provenance   | Review and Validate Data   | Publish and Share Data   | Periodic Review and Updates   | Metadata File Check   |
|:----------------|:---------------------------|:---------------------------|:-------------------------|:-----------------------------------|:-----------------------------------|:-----------------------------------|:---------------------------|:-------------------------|:------------------------------|:----------------------|
| rock_types      | Not Completed              | Not Completed              | Not Completed            | Not Completed                      | Not Completed                      | Not Completed                      | Not Completed              | Not Completed            | Not Completed                 | Failed                |
| pm25_timeseries | Not Completed              | Not Completed              | Not Completed            | Not Completed                      | Not Completed                      | Not Completed                      | Not Completed              | Not Completed            | Not Completed                 | Failed                |
| borehole_data   | Not Completed              | Not Completed              | Not Completed            | Not Completed                      | Not Completed                      | Not Completed                      | Not Completed              | Not Completed            | Not Completed                 | Failed                |
| fossil_records  | Not Completed              | Not Completed              | Not Completed            | Not Completed                      | Not Completed                      | Not Completed                      | Not Completed              | Not Completed            | Not Completed                 | Failed                |

Now, we are "fixing" the `borehole_data` project.

```
python generate_borehole_data.py
```

Re-running

```
python generate_report.py 
```

to generate `summary_report.md`:

| Project         | Define the Scope of Data   | Choose Open Data Formats   | Ensure FAIR Principles   | Utilize Cloud or Network Storage   | Involve Data Manager and Experts   | Document Metadata and Provenance   | Review and Validate Data   | Publish and Share Data   | Periodic Review and Updates   | Metadata File Check   |
|:----------------|:---------------------------|:---------------------------|:-------------------------|:-----------------------------------|:-----------------------------------|:-----------------------------------|:---------------------------|:-------------------------|:------------------------------|:----------------------|
| rock_types      | Not Completed              | Not Completed              | Not Completed            | Not Completed                      | Not Completed                      | Not Completed                      | Not Completed              | Not Completed            | Not Completed                 | Failed                |
| pm25_timeseries | Not Completed              | Not Completed              | Not Completed            | Not Completed                      | Not Completed                      | Not Completed                      | Not Completed              | Not Completed            | Not Completed                 | Failed                |
| borehole_data   | Completed                  | Completed                  | Not Completed            | Not Completed                      | Not Completed                      | Completed                          | Completed                  | Completed                | Completed                     | Success               |
| fossil_records  | Not Completed              | Not Completed              | Not Completed            | Not Completed                      | Not Completed                      | Not Completed                      | Not Completed              | Not Completed            | Not Completed                 | Failed                |


Now, we need to "fix" the FAIR section in our `datapackage.yaml` (`cp borehole_datapackage.yaml data_projects/borehole_data/datapackage.yaml`) and re-run the reporting script:

| Project         | Define the Scope of Data   | Choose Open Data Formats   | Ensure FAIR Principles   | Utilize Cloud or Network Storage   | Involve Data Manager and Experts   | Document Metadata and Provenance   | Review and Validate Data   | Publish and Share Data   | Periodic Review and Updates   | Metadata File Check   |
|:----------------|:---------------------------|:---------------------------|:-------------------------|:-----------------------------------|:-----------------------------------|:-----------------------------------|:---------------------------|:-------------------------|:------------------------------|:----------------------|
| rock_types      | Not Completed              | Not Completed              | Not Completed            | Not Completed                      | Not Completed                      | Not Completed                      | Not Completed              | Not Completed            | Not Completed                 | Failed                |
| pm25_timeseries | Not Completed              | Not Completed              | Not Completed            | Not Completed                      | Not Completed                      | Not Completed                      | Not Completed              | Not Completed            | Not Completed                 | Failed                |
| borehole_data   | Completed                  | Completed                  | Completed                | Not Completed                      | Not Completed                      | Completed                          | Completed                  | Completed                | Completed                     | Success               |
| fossil_records  | Not Completed              | Not Completed              | Not Completed            | Not Completed                      | Not Completed                      | Not Completed                      | Not Completed              | Not Completed            | Not Completed                 | Failed                |
