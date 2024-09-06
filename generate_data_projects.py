import os
import geopandas as gpd
import pandas as pd
import numpy as np
from shapely.geometry import Point

# Create a unified folder structure
def create_project_structure(base_dir):
    folders = [
        'rock_types/raw-data', 'rock_types/processed-data', 'rock_types/scripts', 'rock_types/reports',
        'pm25_timeseries/raw-data', 'pm25_timeseries/processed-data', 'pm25_timeseries/scripts', 'pm25_timeseries/reports',
        'borehole_data/raw-data', 'borehole_data/processed-data', 'borehole_data/scripts', 'borehole_data/reports',
        'fossil_records/raw-data', 'fossil_records/processed-data', 'fossil_records/scripts', 'fossil_records/reports'
    ]
    
    for folder in folders:
        os.makedirs(os.path.join(base_dir, folder), exist_ok=True)

# 1. Rock types as a single GIS layer (GeoJSON)
def generate_rock_types_geojson(file_path):
    data = {
        'rock_type': ['Sandstone', 'Limestone', 'Granite', 'Shale', 'Basalt'],
        'geometry': [Point(-101.17, 47.64), Point(-101.25, 47.68), Point(-101.30, 47.70), Point(-101.35, 47.74), Point(-101.40, 47.78)]
    }
    gdf = gpd.GeoDataFrame(data, crs="EPSG:4326")
    gdf.to_file(file_path, driver='GeoJSON')
    print(f"Rock types GIS layer saved to {file_path}")

# 2. PM2.5 as a multi-year time series for different locations with gaps (CSV)
def generate_pm25_timeseries(file_path):
    dates = pd.date_range(start='2020-01-01', end='2023-12-31', freq='D')
    locations = ['Location1', 'Location2', 'Location3', 'Location4', 'Location5']
    data = []

    for location in locations:
        pm25_values = np.random.rand(len(dates)) * 100
        pm25_values[np.random.choice(len(dates), size=100, replace=False)] = np.nan  # Introduce gaps
        data.append(pd.DataFrame({'Date': dates, 'Location': location, 'PM2.5': pm25_values}))

    df = pd.concat(data)
    df.to_csv(file_path, index=False)
    print(f"PM2.5 time series saved to {file_path}")

# 3. Borehole data for 5 wells (CSV)
def generate_borehole_data(file_path):
    data = {
        'WellID': ['Well1', 'Well2', 'Well3', 'Well4', 'Well5'],
        'Depth': [100, 200, 150, 120, 180],
        'Lithology': ['Sandstone', 'Limestone', 'Granite', 'Shale', 'Basalt']
    }
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f"Borehole data saved to {file_path}")

# 4. Fossil records with ID, location, and description (CSV)
def generate_fossil_records(file_path):
    data = {
        'FossilID': ['Fossil1', 'Fossil2', 'Fossil3', 'Fossil4', 'Fossil5'],
        'Latitude': [47.64, 47.68, 47.70, 47.74, 47.78],
        'Longitude': [-101.17, -101.25, -101.30, -101.35, -101.40],
        'Description': ['Ancient fish', 'Dinosaur bone', 'Ammonite', 'Trilobite', 'Plant fossil']
    }
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f"Fossil records saved to {file_path}")

# Main function to create structure and generate data
def main(base_dir):
    create_project_structure(base_dir)
    
    # Generate datasets
    generate_rock_types_geojson(os.path.join(base_dir, 'rock_types/raw-data/rock_types.geojson'))
    generate_pm25_timeseries(os.path.join(base_dir, 'pm25_timeseries/raw-data/pm25_timeseries.csv'))
    generate_borehole_data(os.path.join(base_dir, 'borehole_data/raw-data/borehole_data.csv'))
    generate_fossil_records(os.path.join(base_dir, 'fossil_records/raw-data/fossil_records.csv'))

# Specify the base directory for the project structure
base_directory = 'data_projects'
main(base_directory)
