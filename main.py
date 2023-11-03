import numpy as np
import matplotlib.pyplot as plt

# Define the data
oscarb2_scores = [97, 96, 94, 94, 95]
minivlm_scores = [89, 94, 94, 95, 95]

# Define the x-axis labels
x_labels = ["VQA", "TR", "OSCARB", "MiniVLM (ours)", "IR"]

# Create a bar chart
plt.bar(x_labels, oscarb2_scores, color='blue')
plt.bar(x_labels, minivlm_scores, color='green')

# Set the y-axis limits
plt.ylim(0, 100)

# Add a title and labels
plt.title("Performance of OSCARB2 and MiniVLM on different tasks")
plt.xlabel("Task")
plt.ylabel("Accuracy (%)")

# Show the plot
plt.show()