import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Seed for reproducibility
np.random.seed(0)

# Data setup
data_dict = {
    'Group': np.random.choice(['A', 'B', 'C', 'D', 'E'], 100),
    'Measurement': np.random.randn(100)
}
data_frame = pd.DataFrame(data_dict)

# Create a box plot
plt.figure(figsize=(12, 6))
sns.boxplot(x='Group', y='Measurement', data=data_frame)
plt.xlabel('Group')
plt.ylabel('Measurement')
plt.title('Box Plot of Measurement by Group')
plt.grid(True)
plt.show()
