import os
import pandas as pd
import yaml
from frictionless import Package, validate

# Define paths for each project
projects = {
        'rock_types': 'data_projects/rock_types',
        'pm25_timeseries': 'data_projects/pm25_timeseries',
        'borehole_data': 'data_projects/borehole_data',
        'fossil_records': 'data_projects/fossil_records'
        }

# Define checklist of actions
checklist = [
        'Define the Scope of Data',
        'Choose Open Data Formats',
        'Ensure FAIR Principles',
        'Document Metadata and Provenance',
        'Review and Validate Data',
        'Publish and Share Data',
        'Periodic Review and Updates'
        ]

def check_action_items(project_name, project_path):
    metadata_file = os.path.join(project_path, 'datapackage.yaml')
    raw_data_folder = os.path.join(project_path, 'raw-data')

    # Initialize results
    results = {action: 'Not Completed' for action in checklist}

    if os.path.exists(metadata_file):
        # Load Data Package metadata
        with open(metadata_file, 'r') as file:
            metadata = yaml.safe_load(file)

        # Check if the dataset is defined and open formats are used
        results['Define the Scope of Data'] = 'Completed' if metadata.get('resources') else 'Not Completed'
        results['Choose Open Data Formats'] = 'Completed' if all(resource.get('format') in ['csv', 'geojson'] for resource in metadata.get('resources', [])) else 'Not Completed'

        # Ensure FAIR Principles
        results['Ensure FAIR Principles'] = 'Completed' if validate_fair_principles(metadata) else 'Not Completed'

        # Document Metadata and Provenance
        results['Document Metadata and Provenance'] = 'Completed' if 'description' in metadata and 'schema' in metadata.get('resources', [{}])[0] else 'Not Completed'

        # Review and Validate Data
        results['Review and Validate Data'] = 'Completed' if validate_data(raw_data_folder) else 'Not Completed'

        # Publish and Share Data
        results['Publish and Share Data'] = 'Completed'  # Assumed always completed for this example

        # Periodic Review and Updates
        results['Periodic Review and Updates'] = 'Completed'  # Assumed always completed for this example

        results['Metadata File Check'] = 'Passed'
    else:
        results['Metadata File Check'] = 'Failed'

    return results


def validate_fair_principles(metadata):
    """
    Validate the FAIR principles based on the given metadata.

    Args:
        metadata (dict): The metadata dictionary loaded from the datapackage.yaml file.

    Returns:
        bool: True if the metadata meets the FAIR principles, False otherwise.
    """
    # Initialize validation results
    valid = True
    messages = []

    # Findable: Check if metadata contains a unique identifier and description
    if not metadata.get('name'):
        valid = False
        messages.append("Missing 'name' field in metadata. Data should have a unique identifier.")
    if not metadata.get('description'):
        valid = False
        messages.append("Missing 'description' field in metadata. Description is required for findability.")

    # Accessible: Check if metadata provides a path to the data
    resources = metadata.get('resources', [])
    for resource in resources:
        if not resource.get('path'):
            valid = False
            messages.append(f"Resource '{resource.get('name')}' missing 'path'. Data access path is required.")

    # Interoperable: Check if metadata includes schema and format information
    for resource in resources:
        if not resource.get('format'):
            valid = False
            messages.append(f"Resource '{resource.get('name')}' missing 'format'. Format information is required for interoperability.")
        if not resource.get('schema'):
            valid = False
            messages.append(f"Resource '{resource.get('name')}' missing 'schema'. Schema information is required for interoperability.")

    # Reusable: Check for licensing and provenance information
    if not metadata.get('licenses'):
        valid = False
        messages.append("Missing 'licenses' field in metadata. Licensing information is necessary for data reuse.")

    # Print validation messages
    for message in messages:
        print(message)

    return valid

def validate_data(raw_data_folder):
    try:
        csv_files = [os.path.join(raw_data_folder, file) for file in os.listdir(raw_data_folder) if file.endswith('.csv')]
        for csv_file in csv_files:
            df = pd.read_csv(csv_file)
            if df.isnull().sum().sum() > 0:
                return False
        return True
    except Exception as e:
        print(f"Error validating data: {e}")
        return False

# Collect results for all projects
summary_results = []
for project_name, project_path in projects.items():
    results = check_action_items(project_name, project_path)
    results['Project'] = project_name
    summary_results.append(results)

# Convert results to DataFrame
df_summary = pd.DataFrame(summary_results)
df_summary = df_summary.set_index('Project')

# Save the summary report as Markdown
summary_report_file = 'data_projects/summary_report.md'
df_summary.to_markdown(summary_report_file)
print(f"Summary report generated: {summary_report_file}")
