import os
import pandas as pd

def load_data(file_path):
    # Load data from a CSV file
    return pd.read_csv(file_path)

def remove_null_rows(df):
    # Remove rows from DF that contain any null values
    cleaned_df = df.dropna()
    return cleaned_df

def convert_date_format(df, column_name):
    # Convert the date format of a specified column
    df[column_name] = pd.to_datetime(df[column_name], errors='coerce')
    return df

def save_data(df, file_path):
    # Save DataFrame to a CSV file
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    # Define the project root directory
    project_root = 'C:/Users/Mtvan/Documents/All Projects/Python/API Traffic Insights'

    # Define file paths using the project root
    raw_data_path = os.path.join(project_root, 'data/raw/MOCK_DATA.csv')
    processed_data_path = os.path.join(project_root, 'data/processed/cleaned_DATA.csv')

    # Load the data
    df = load_data(raw_data_path)

    # Clean the data
    cleaned_df = remove_null_rows(df)

    # Convert the date format
    cleaned_df = convert_date_format(cleaned_df, 'transaction_date')

    # Save the cleaned data
    save_data(cleaned_df, processed_data_path)
    print(f"Processed data saved to {processed_data_path}")


