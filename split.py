# import pandas as pd

# def split_dataset(input_csv, train_output_csv, test_output_csv):
#     data = pd.read_csv(input_csv)
#     data.columns = data.columns.str.strip()
#     if 'Usage' not in data.columns:
#         raise KeyError("The 'Usage' column is not found in the dataset. Please check the input CSV file.")
#     train_data = data[data['Usage'] == 'Training']
#     test_data = data[data['Usage'] == 'Testing']
#     train_data.to_csv(train_output_csv, index=False)
#     test_data.to_csv(test_output_csv, index=False)
#     print(f"Training data saved to {train_output_csv}")
#     print(f"Testing data saved to {test_output_csv}")

# split_dataset('icml_face_data.csv', 'train.csv', 'test.csv')
import pandas as pd
from sklearn.model_selection import train_test_split

def split_train_test_subsets(train_csv, test_csv, train_subset_csv, test_subset_csv, train_size=0.2, test_size=0.2):
    train_data = pd.read_csv(train_csv)
    test_data = pd.read_csv(test_csv)
    train_subset, _ = train_test_split(train_data, train_size=train_size, random_state=42)
    test_subset, _ = train_test_split(test_data, test_size=test_size, random_state=42)
    train_subset.to_csv(train_subset_csv, index=False)
    test_subset.to_csv(test_subset_csv, index=False)
    print(f"Training subset saved to {train_subset_csv}")
    print(f"Testing subset saved to {test_subset_csv}")

split_train_test_subsets('train.csv', 'test.csv', 'train_subset.csv', 'test_subset.csv', train_size=0.2, test_size=0.2)
