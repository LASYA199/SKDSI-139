import pandas as pd
import matplotlib.pyplot as plt

# Data setup
data_dict = {
    'Category_A': [4, 7, 1, 8, 5],
    'Category_B': [5, 2, 8, 3, 6],
    'Category_C': [7, 5, 3, 4, 9]
}
item_index = ['Item_1', 'Item_2', 'Item_3', 'Item_4', 'Item_5']
data_frame = pd.DataFrame(data_dict, index=item_index)

# Side-by-side bar plot
side_by_side_ax = data_frame.plot(kind='bar', figsize=(10, 6))
side_by_side_ax.set_xlabel('Items')
side_by_side_ax.set_ylabel('Values')
side_by_side_ax.set_title('Side-by-Side Bar Plot')
plt.xticks(rotation=0)
plt.show()

# Stacked bar plot
stacked_ax = data_frame.plot(kind='bar', stacked=True, figsize=(10, 6))
stacked_ax.set_xlabel('Items')
stacked_ax.set_ylabel('Values')
stacked_ax.set_title('Stacked Bar Plot')
plt.xticks(rotation=0)
plt.show()
