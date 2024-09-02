# csv转geojson
import csv
import json
import os


def csv_to_geojson(csv_file, geojson_file):
    # Initialize a GeoJSON feature collection
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    # Open the CSV file
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)

        # Initialize the LineString coordinates
        coordinates = []

        for row in reader:
            # Extract latitude and longitude
            latitude = float(row["latitude"])
            longitude = float(row["longitude"])
            coordinates.append([longitude, latitude])

        # Create a LineString feature
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": coordinates
            },
            "properties": {}  # Add any additional properties if needed
        }

        geojson["features"].append(feature)

    # Save the GeoJSON to a file
    with open(geojson_file, 'w') as geojson_out:
        json.dump(geojson, geojson_out, indent=4)
        print(csv_file+"--->"+geojson_file)


def read_files(dir_path):
    files = os.listdir(dir_path)
    files = [dir_path+"/"+file for file in files if file[-3:] == "csv"]
    for file in files:
        csv_to_geojson(
            file, (file[:-3]+"geojson").replace("/csv", "/geojson", 1))


# # Usage example
# # Replace with your input CSV file
# csv_file = '/users/zj/cx/test/driving_lane2.csv'
# # Replace with your output GeoJSON file
# geojson_file = '/users/zj/ARC/geojson/lane2.geojson'
# csv_to_geojson(csv_file, geojson_file)
read_files("/users/zj/ARC/csv")
