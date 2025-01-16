import pandas as pd
import ast

# Paths to input and output files
item_metadata_path = r"Jsonl2CSV.csv"
output_csv_path = r"json_table_one_hot.csv"

# Read the entire CSV file
df = pd.read_csv(item_metadata_path, low_memory=False)

# Convert the 'categories' column from string representation of lists to actual Python lists
list_of_categories = df['categories'].apply(ast.literal_eval)

# Create One-Hot encoded columns for 'categories'
one_hot_categories = pd.DataFrame(
    [{category: 1 for category in categories} for categories in list_of_categories]
).fillna(0).astype(int)

# Convert the 'details' column from string representation of dictionaries to actual Python dictionaries
list_of_details = df['details'].apply(ast.literal_eval)

# Create One-Hot encoded columns for 'details'
one_hot_details = pd.DataFrame(
    [{detail: 1 for detail in details} for details in list_of_details]
).fillna(0).astype(int)

# Concatenate the original DataFrame with the One-Hot encoded DataFrames
df = pd.concat([df, one_hot_categories, one_hot_details], axis=1)

# Save the resulting DataFrame to a CSV file
df.to_csv(output_csv_path, index=False)

print(f"One-hot encoded DataFrame saved to: {output_csv_path}")
