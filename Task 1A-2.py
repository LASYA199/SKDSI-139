import pandas as pd

# Data setup
values = [10, 20, 30, 40, 50, 60]
multi_index = pd.MultiIndex.from_tuples([('Group1', 1), ('Group1', 2), ('Group2', 1), ('Group2', 2), ('Group3', 1), ('Group3', 2)])
multi_index_series = pd.Series(values, index=multi_index)

print("Series with MultiIndex:")
print(multi_index_series)

# Subset Group1
subset_group1 = multi_index_series.loc['Group1']
print("\nSubset Group1:")
print(subset_group1)

# Subset Group1, Inner 2
subset_group1_inner2 = multi_index_series.loc[('Group1', 2)]
print("\nSubset Group1, Inner 2:")
print(subset_group1_inner2)

# Subset Group2
subset_group2 = multi_index_series.loc['Group2']
print("\nSubset Group2:")
print(subset_group2)

# Subset Group3, Inner 1
subset_group3_inner1 = multi_index_series.loc[('Group3', 1)]
print("\nSubset Group3, Inner 1:")
print(subset_group3_inner1)

# Subset Group2 using xs
subset_group2_xs = multi_index_series.xs('Group2')
print("\nSubset Group2 using xs:")
print(subset_group2_xs)

# Subset Inner Level 2 using xs
subset_inner_level2 = multi_index_series.xs(2, level=1)
print("\nSubset Inner Level 2 using xs:")
print(subset_inner_level2)
