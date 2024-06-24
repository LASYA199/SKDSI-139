import pandas as pd
import numpy as np

# Define date range
date_index = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')

# Generate random data
random_values = np.random.randn(len(date_index))

# Create a time series DataFrame
time_series_data = pd.DataFrame(random_values, index=date_index, columns=['Measurement'])

# Display the first few rows of the DataFrame
print(time_series_data.head())
