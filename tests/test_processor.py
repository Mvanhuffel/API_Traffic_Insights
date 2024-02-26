import pandas as pd
from src.data_processing.processor import remove_null_rows, convert_date_format

def test_remove_null_rows():
    data = {'A': [1, None, 3], 'B': [4, 5, None]}
    df = pd.DataFrame(data)
    cleaned_df = remove_null_rows(df)
    assert cleaned_df.isnull().sum().sum() == 0
    assert len(cleaned_df) == 1  # Expecting 1 row after removing rows with null values

def test_convert_date_format():
    data = {'date': ['2020-01-01', '2021-02-30', 'not a date']}
    df = pd.DataFrame(data)
    df = convert_date_format(df, 'date')
    assert pd.isnull(df['date'][1])  # Invalid date should be converted to NaT
    assert pd.isnull(df['date'][2])  # Non-date string should be converted to NaT
    assert df['date'][0] == pd.Timestamp('2020-01-01')  # Valid date should be properly converted

# If you want to run tests directly without using pytest command
if __name__ == "__main__":
    test_remove_null_rows()
    test_convert_date_format()
    print("All tests passed!")

