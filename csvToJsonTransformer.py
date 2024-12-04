import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    try:
        # Read the CSV file
        with open(csv_file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            # Convert rows to a list of dictionaries
            data = [row for row in csv_reader]

        # Write the JSON file
        with open(json_file_path, mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"CSV data successfully converted to JSON and saved to {json_file_path}")
    except Exception as e:
        print(f"Error: {e}")

# Usage
csv_to_json('data.csv', 'data.json')
