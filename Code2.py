import matplotlib.pyplot as plt
import numpy as np

# Define the data
directions = ['E', 'N', 'W', 'S']
distances = ['Inoculum', '1m', '2m', '4m']
inoculum_data = [[10000, 2010, 2010, 3010], [10000, 1410, 2010, 11210], [10000, 1101, 1310, 1701], [10000, 1310, 1150, 1220]]

# Convert the distances to radians for the polar plot
theta = np.linspace(0, 2*np.pi, len(directions), endpoint=False)

# Define the figure and subplot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Plot the inoculum data as bubble plot
for d, direction in enumerate(directions):
    for i, distance in enumerate(distances):
        size = inoculum_data[d][i]/10
        ax.scatter(theta[d], distance, s=size, alpha=0.5)

# Set the axis labels
ax.set_xticks(theta)
ax.set_xticklabels(directions)
ax.set_yticks(distances)

# Set the title and legend
ax.set_title('Inoculum load at different distances and directions', fontsize=16)

# Show the plot
plt.show()
