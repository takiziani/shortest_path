import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import folium
import os
abspath = os.path.abspath(__file__)
osm_file_path = os.path.join(os.path.dirname(abspath), 'map.osm')

# Load the graph from the .osm file
G = ox.graph_from_xml(osm_file_path)

# Plot the map
# fig, ax = ox.plot_graph(G, show=False, close=False)

G = G.to_undirected()

# Define the coordinates of two cities (replace with real coordinates)
orig_coords = (36.7649707, 8.3603637)
dest_coords = (36.7655367, 8.3139141)


# Find the nearest nodes to the coordinates
orig = ox.distance.nearest_nodes(G, orig_coords[1], orig_coords[0])
dest = ox.distance.nearest_nodes(G, dest_coords[1], dest_coords[0])

# Compute shortest path using A* algorithm
shortest = nx.astar_path(G, orig, dest, weight='length')

# Debugging: Print the shortest path nodes
print("Shortest path nodes:", shortest)

# Plot the graph with the shortest path highlighted
fig, ax = ox.plot_graph_route(G, shortest, route_linewidth=4, node_size=0, bgcolor="w", show=False, close=False)

# Add annotations for the cities
ax.text(orig_coords[1], orig_coords[0], 'City 1', fontsize=12, ha='right')
ax.text(dest_coords[1], dest_coords[0], 'City 2', fontsize=12, ha='right')

plt.show()

# Create a folium map centered around the origin
route_map = folium.Map(location=orig_coords, zoom_start=14)

# Add the route to the folium map
route_nodes = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in shortest]
folium.PolyLine(route_nodes, color="blue", weight=2.5, opacity=1).add_to(route_map)

# Save to an HTML file and view in a browser
route_map.save("shortest_path.html")