import os
import pandas as pd
import yaml

# Define file paths
base_path = 'data_projects/borehole_data'
csv_path = os.path.join(base_path, 'raw-data', 'borehole_data.csv')
metadata_path = os.path.join(base_path, 'datapackage.yaml')

# Ensure directories exist
os.makedirs(os.path.dirname(csv_path), exist_ok=True)
os.makedirs(os.path.dirname(metadata_path), exist_ok=True)

# Generate sample data for borehole dataset
data = {
        'BoreholeID': ['BH001', 'BH002', 'BH003', 'BH004', 'BH005'],
        'Location': ['SiteA', 'SiteB', 'SiteC', 'SiteD', 'SiteE'],
        'Depth': [150, 200, 180, 220, 160],
        'DateDrilled': ['2024-01-15', '2024-02-20', '2024-03-10', '2024-04-05', '2024-05-12'],
        'Driller': ['John Doe', 'Jane Smith', 'Emily Jones', 'Michael Brown', 'Sarah Wilson']
        }

df = pd.DataFrame(data)

# Save the dataframe to a CSV file
df.to_csv(csv_path, index=False)

# Define a comprehensive datapackage.yaml content
datapackage = {
        'name': 'borehole_data',
        'title': 'Borehole Data',
        'description': 'A dataset containing information about boreholes, including their ID, location, depth, date drilled, and driller.',
        'version': '1.0',
        'keywords': ['borehole', 'geology', 'drilling'],
        'homepage': 'https://example.com/borehole-data',
        'licenses': [
            {
                'name': 'Open Data Commons Public Domain Dedication and License (PDDL)',
                'path': 'https://opendatacommons.org/licenses/pddl/'
                }
            ],
        'resources': [
            {
                'name': 'boreholes',
                'path': 'raw-data/borehole_data.csv',
                'format': 'csv',
                'profile': 'tabular-data-resource',
                'schema': {
                    'fields': [
                        {'name': 'BoreholeID', 'type': 'string', 'description': 'Unique identifier for the borehole'},
                        {'name': 'Location', 'type': 'string', 'description': 'Geographic location of the borehole'},
                        {'name': 'Depth', 'type': 'number', 'description': 'Depth of the borehole in meters'},
                        {'name': 'DateDrilled', 'type': 'date', 'description': 'Date when the borehole was drilled'},
                        {'name': 'Driller', 'type': 'string', 'description': 'Name of the person who drilled the borehole'}
                        ],
                    'primaryKey': 'BoreholeID'
                    }
                }
            ]
        }

# Save the datapackage.yaml file
with open(metadata_path, 'w') as f:
    yaml.dump(datapackage, f, default_flow_style=False)

print(f"Generated CSV file at {csv_path}")
print(f"Generated datapackage.yaml file at {metadata_path}")
