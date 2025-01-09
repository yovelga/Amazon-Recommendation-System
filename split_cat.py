import pandas as pd
import ast

# Paths to input and output files
item_metadata_path = r"C:\Users\yovel\PycharmProjects\recommendation_systems\Jsonl2CSV.csv"
output_csv_path = r"C:\Users\yovel\PycharmProjects\recommendation_systems\json_table_one_hot.csv"

# Parameters
chunksize = 200
first_chunk = True

# Process the CSV file in chunks
for i, chunk in enumerate(pd.read_csv(item_metadata_path, low_memory=False, chunksize=chunksize)):
    print(f"Processing chunk number: {i + 1}")

    # Convert the 'categories' column from string representation of lists to actual Python lists
    list_of_categories = chunk['categories'].apply(ast.literal_eval)

    # Create One-Hot encoded columns for 'categories'
    one_hot_categories = pd.DataFrame(
        [{category: 1 for category in categories} for categories in list_of_categories]
    ).fillna(0).astype(int)

    # Convert the 'details' column from string representation of dictionaries to actual Python dictionaries
    list_of_details = chunk['details'].apply(ast.literal_eval)

    # Create One-Hot encoded columns for 'details'
    one_hot_details = pd.DataFrame(
        [{detail: 1 for detail in details} for details in list_of_details]
    ).fillna(0).astype(int)

    # Concatenate the original chunk with the One-Hot encoded DataFrames
    chunk = pd.concat([chunk, one_hot_categories, one_hot_details], axis=1)

    # Append the chunk to the output CSV file
    chunk.to_csv(output_csv_path, mode='a', index=False, header=first_chunk)

    # After writing the first chunk, disable writing the header for subsequent chunks
    first_chunk = False

print(f"One-hot encoded DataFrame saved incrementally to: {output_csv_path}")
