import matplotlib.pyplot as plt

from Variables import categories, color_mapping, age_measurements
# Filter out "various" entries and convert the ages to a list of tuples for plotting
plot_data = [(k, v) for k, v in age_measurements.items() if isinstance(v, int)]

# Unpack the tuples into two lists and get corresponding colors
organs, ages = zip(*plot_data)
colors = [color_mapping[categories[organ]] for organ in organs]

# Create the plot
plt.figure(figsize=(14, 10))
scatter = plt.scatter(ages, organs, color=colors)
plt.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)
plt.axvline(x=8, color='red', linestyle='--', linewidth=0.5)
plt.axvline(x=120, color='red', linestyle='--', linewidth=0.5)
plt.title('Age measurements of Bryan Johnson, 1. July 2024')
plt.xlabel('Age')
plt.xticks(range(8, 120, 10))
plt.yticks(range(len(organs)), organs)
plt.grid(True, linestyle='--', linewidth=0.5)

# Adjust layout to give more space for y-axis labels
plt.tight_layout(rect=[0, 0, 0.8, 1])  # Adjust the rect parameter to give space for the legend

# Create a custom legend
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=category) for category, color in color_mapping.items()]
plt.legend(handles=handles, title='Categories', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()


