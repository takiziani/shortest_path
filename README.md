# Shortest Path Finder

A Python-based project that computes and visualizes the shortest path between two geographic locations using **A\* algorithm**, **OSMnx**, and **NetworkX**.

## Features

- Loads a road network from an `.osm` (OpenStreetMap) file
- Finds the nearest graph nodes to given GPS coordinates
- Computes the shortest path using the **A\*** algorithm
- Visualizes the route on a static matplotlib plot
- Generates an interactive **Folium** HTML map with the route highlighted

## Project Structure

```
TP1/
├── README.md
├── shortest_path.html       # Generated interactive map (root level)
└── try1/
    ├── final.py             # Main script
    ├── map.osm              # OpenStreetMap data file
    └── shortest_path.html   # Generated interactive map
```

## Requirements

- Python 3.x
- [osmnx](https://osmnx.readthedocs.io/)
- [networkx](https://networkx.org/)
- [matplotlib](https://matplotlib.org/)
- [folium](https://python-visualization.github.io/folium/)

Install dependencies:

```bash
pip install osmnx networkx matplotlib folium
```

## Usage

1. Place your `map.osm` file in the `try1/` directory.
2. Update the coordinates in `final.py` if needed:

```python
orig_coords = (36.7649707, 8.3603637)  # Origin
dest_coords = (36.7655367, 8.3139141)  # Destination
```

3. Run the script:

```bash
cd try1
python final.py
```

4. A matplotlib window will display the route on the graph.
5. An interactive map will be saved as `shortest_path.html` — open it in a browser to explore the route.

## How It Works

1. The road network is loaded from the `.osm` file using `osmnx`.
2. The graph is converted to undirected.
3. The nearest nodes to the origin and destination coordinates are found.
4. The **A\*** algorithm computes the shortest path by road distance (`weight='length'`).
5. The path is visualized using both `matplotlib` and `folium`.
