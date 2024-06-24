import matplotlib.pyplot as plt
import numpy as np

# Data setup
x_values = np.linspace(0, 10, 100)
sine_values = np.sin(x_values)
cosine_values = np.cos(x_values)

# Creating subplots
fig, (sine_ax, cosine_ax) = plt.subplots(2, 1, figsize=(10, 8))

# Plotting sine function
sine_ax.plot(x_values, sine_values, label='sin(x)', color='blue', linestyle='-')
sine_ax.set_title('Sine Function')
sine_ax.set_xlabel('x-axis')
sine_ax.set_ylabel('sin(x)')
sine_ax.grid(True)
sine_ax.legend(loc='upper right')
sine_ax.set_xticks(np.arange(0, 11, 1))
sine_ax.set_yticks(np.arange(-1, 1.5, 0.5))
sine_ax.set_xticklabels([f'{i}' for i in range(11)])
sine_ax.set_yticklabels([f'{i:.1f}' for i in np.arange(-1, 1.5, 0.5)])
sine_ax.annotate('Max Value', xy=(np.pi/2, 1), xytext=(np.pi/2+1, 0.8),
                 arrowprops=dict(facecolor='black', shrink=0.05))

# Plotting cosine function
cosine_ax.plot(x_values, cosine_values, label='cos(x)', color='red', linestyle='--')
cosine_ax.set_title('Cosine Function')
cosine_ax.set_xlabel('x-axis')
cosine_ax.set_ylabel('cos(x)')
cosine_ax.grid(True)
cosine_ax.legend(loc='upper right')
cosine_ax.set_xticks(np.arange(0, 11, 1))
cosine_ax.set_yticks(np.arange(-1, 1.5, 0.5))
cosine_ax.set_xticklabels([f'{i}' for i in range(11)])
cosine_ax.set_yticklabels([f'{i:.1f}' for i in np.arange(-1, 1.5, 0.5)])
cosine_ax.annotate('Min Value', xy=(np.pi, -1), xytext=(np.pi+1, -0.8),
                   arrowprops=dict(facecolor='black', shrink=0.05))

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('line_plot_with_annotations.png')
plt.show()
