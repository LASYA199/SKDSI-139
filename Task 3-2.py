# Using Start date and End date
import pandas as pd

# Define start and end dates
start_dt = '2024-01-01'
end_dt = '2024-12-31'

# Create date range
daily_dates = pd.date_range(start=start_dt, end=end_dt)
print(daily_dates)

# Using Start date and Periods
# Define start date and number of periods
start_dt = '2024-01-01'
num_periods = 365  # for a full year

# Create date range
daily_dates = pd.date_range(start=start_dt, periods=num_periods)
print(daily_dates)

# Using End date and Periods
# Define end date and number of periods
end_dt = '2024-12-31'
num_periods = 365  # for a full year

# Create date range
daily_dates = pd.date_range(end=end_dt, periods=num_periods)
print(daily_dates)

# Using Frequency
# Define start and end dates
start_dt = '2024-01-01'
end_dt = '2024-12-31'

# Create date range with daily frequency
daily_dates = pd.date_range(start=start_dt, end=end_dt, freq='D') # 'D' generates dates on a daily basis
print(daily_dates)
