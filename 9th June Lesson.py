#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'example2.csv'
data = pd.read_csv(file_path)

# Create a graph object
G = nx.Graph()

# Add edges to the graph based on the data
for index, row in data.iterrows():
    G.add_edge(row['Your Name'], row['Friends'])

# Calculate vertices
vertices = G.number_of_nodes()

# Calculate degree (min and max)
degrees = [degree for node, degree in G.degree()]
degree_min = min(degrees)
degree_max = max(degrees)

# Calculate density
density = nx.density(G)

# Calculate shortest path length (average shortest path length)
try:
    shortest_path_length = nx.average_shortest_path_length(G)
except nx.NetworkXError:
    shortest_path_length = None  # If the graph is not connected

# Calculate diameter
try:
    diameter = nx.diameter(G)
except nx.NetworkXError:
    diameter = None  # If the graph is not connected

# Output the results
print(f"Vertices: {vertices}")
print(f"Degree (min): {degree_min}")
print(f"Degree (max): {degree_max}")
print(f"Density: {density}")
print(f"Shortest Path Length: {shortest_path_length}")
print(f"Diameter: {diameter}")

# Draw the graph with spiral layout
plt.figure(figsize=(10, 8))
pos = nx.spiral_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10, font_weight='bold')
plt.title("Nodes and Edges Graph with Spiral Layout")
plt.show()


# In[ ]:




