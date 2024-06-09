#!/usr/bin/env python
# coding: utf-8

# In[6]:


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

# Calculate connected components and their diameters
connected_components = list(nx.connected_components(G))
subgroup_count = len(connected_components)
subgroup_diameters = []

for component in connected_components:
    subgraph = G.subgraph(component)
    try:
        subgraph_diameter = nx.diameter(subgraph)
    except nx.NetworkXError:
        subgraph_diameter = None  # If the subgraph is not connected
    subgroup_diameters.append(subgraph_diameter)

# Output the results
parameters = {
    "Number of Subgroups": subgroup_count,
    "Subgroup Diameters": subgroup_diameters
}

print(parameters)

# Draw the graph with spiral layout
# plt.figure(figsize=(10, 8))
# pos = nx.spiral_layout(G)
# nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10, font_weight='bold')
# plt.title("Nodes and Edges Graph with Spiral Layout")
# plt.show()


# In[5]:


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

# Calculate connected components and their diameters
connected_components = list(nx.connected_components(G))
subgroup_count = len(connected_components)
subgroup_diameters = []

for component in connected_components:
    subgraph = G.subgraph(component)
    try:
        subgraph_diameter = nx.diameter(subgraph)
    except nx.NetworkXError:
        subgraph_diameter = None  # If the subgraph is not connected
    subgroup_diameters.append(subgraph_diameter)

# Output the results
subgroup_analysis = {
    "Number of Subgroups": subgroup_count,
    "Subgroup Diameters": subgroup_diameters
}

print("Total number of subgroups:", subgroup_count)
print("Diameter of each subgroup:", subgroup_diameters)

# Draw the graph with spiral layout
# plt.figure(figsize=(10, 8))
# pos = nx.spiral_layout(G)
# nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10, font_weight='bold')
# # plt.title("Nodes and Edges Graph with Spiral Layout")
# plt.show()

