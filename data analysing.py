import pandas as pd 
# user_item_path = "R:\advanced_recommender_systems_data\user_item_rating_train.csv"
item_metadata_path = "C:/Users/dorbar1/PycharmProjects/Recommendation_system/data/json_table.csv"

item_data_df = pd.read_csv(item_metadata_path)

print(item_data_df.columns)