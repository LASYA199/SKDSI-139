
import pandas as pd
import numpy as np

# Data setup
data_dict = {
    'Col1': [1, 2, np.nan, 4, 5, np.nan, 7],
    'Col2': [np.nan, 2, 3, 4, np.nan, 6, 7],
    'Col3': ['foo', 'bar', 'baz', np.nan, 'qux', 'quux', 'corge'],
    'Col4': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
}
data_frame = pd.DataFrame(data_dict)
print("Original DataFrame:")
print(data_frame)

# Finding missing data
missing_data_df = data_frame.isna()
print("\nMissing Data in DataFrame:")
print(missing_data_df)

# Dropping rows with any missing data
dropped_rows_df = data_frame.dropna()
print("\nDataFrame after dropping rows with any missing data:")
print(dropped_rows_df)

# Dropping columns with any missing data
dropped_cols_df = data_frame.dropna(axis=1)
print("\nDataFrame after dropping columns with any missing data:")
print(dropped_cols_df)

# Filling missing data
filled_data_df = data_frame.fillna(value={
    'Col1': data_frame['Col1'].mean(), 
    'Col2': data_frame['Col2'].mean(), 
    'Col3': 'missing', 
    'Col4': 0
})
print("\nDataFrame after filling missing data:")
print(filled_data_df)

# Adding a duplicate row
data_with_duplicates = data_frame.append(data_frame.iloc[2], ignore_index=True)
print("\nDataFrame with Duplicates:")
print(data_with_duplicates)

# Finding duplicates
duplicates_df = data_with_duplicates.duplicated()
print("\nDuplicates in DataFrame:")
print(duplicates_df)

# Removing duplicates
no_duplicates_df = data_with_duplicates.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(no_duplicates_df)
