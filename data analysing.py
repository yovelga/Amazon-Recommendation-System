import pandas as pd
pd.options.mode.chained_assignment = None
import warnings
warnings.filterwarnings('ignore')
# user_item_path = "R:\advanced_recommender_systems_data\user_item_rating_train.csv"
item_metadata_path = r"C:\Users\dorex\Documents\Amazon-Recommendation-System\json_table_one_hot.csv"
item_data_df = pd.read_csv(item_metadata_path)



# item_data_df = pd.read_csv(item_metadata_path)
print(len(item_data_df))
#

# print(item_data_df['details'])