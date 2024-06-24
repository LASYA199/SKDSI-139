import pandas as pd

# Define start and end dates
start_dt = '2024-01-01'
end_dt = '2024-01-05'

# Create date range with daily frequency
date_range = pd.date_range(start=start_dt, end=end_dt, freq='D')
print(date_range)

# Setting TimeZone
utc_dates = pd.date_range(start=start_dt, end=end_dt, freq='D', tz='UTC')
print(utc_dates)

# Localizing TimeZone
localized_dates = pd.date_range(start=start_dt, end=end_dt, freq='D')
localized_dates = localized_dates.tz_localize('America/New_York')
print(localized_dates)

# Converting TimeZone
converted_dates = localized_dates.tz_convert('Europe/London')
print(converted_dates)

# Combining two different TimeZones
utc_dates_short = pd.date_range(start=start_dt, periods=3, freq='D', tz='UTC')
ny_dates_short = pd.date_range(start=start_dt, periods=3, freq='D', tz='America/New_York')
combined_dates = utc_dates_short.union(ny_dates_short)
print(combined_dates)
