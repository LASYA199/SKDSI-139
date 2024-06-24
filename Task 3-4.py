import pandas as pd

# Define a period with monthly frequency
initial_period = pd.Period('2024-01', freq='M')

# Calculate future and past periods
future_period = initial_period + 3
print("Future Period:", future_period)

past_period = initial_period - 2
print("Past Period:", past_period)

# Construct a range of periods
monthly_periods = pd.period_range(start='2024-01', end='2024-12', freq='M')
print("Periods Range:", monthly_periods)
