import matplotlib.pyplot as plt

# Create a list of data points for each bar
data = [
    [100, 97],
    [120, 100],
    [80, 89],
    [60, 100],
    [40, 96],
    [20, 94],
]

# Create a list of labels for each bar
labels = ["Caption", "VQA", "TR", "IR", "NLVR2", "OSCAR"]

# Create a figure and axes
fig, ax = plt.subplots()

# Create a bar chart for each data point
ax.bar(labels, data)

# Add a title to the figure
ax.set_title("Model Performance on Visual Reasoning Tasks")

# Add labels to the x-axis and y-axis
ax.set_xlabel("Task")
ax.set_ylabel("Accuracy (%)")

# Set the y-axis limits
ax.set_ylim(0, 100)

# Add a legend to the figure
ax.legend(loc="best")

# Show the figure
plt.show()