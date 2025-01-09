import pandas as pd
import json
import os
# Define the file path
Home_dir =  os.getcwd()
file_path = os.path.join(Home_dir, 'recsys_data_and_test_files','items_metadata.jsonl')
print(file_path)
# file_path = r"R:\\advanced_recommender_systems_data\\items_metadata.jsonl"

# Initialize an empty list to store data
data = []

# Read the JSONL file
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                # Parse each line as JSON and append to the data list
                data.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)

    # Display the DataFrame
    print(df)

    # Save the DataFrame to a CSV file
    output_csv_path = os.path.join(Home_dir, 'Jsonl2CSV.csv')


    df.to_csv(output_csv_path, index=False)
    print(f"DataFrame saved to CSV at {output_csv_path}")


except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

