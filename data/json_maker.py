import json
import networkx as nx
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
from Library import get_dic_data
import os

# Relationship Mapping and Colors
relationship_classes = {'PR': [0, 1, 2, 3], 'SC': [4, 5, 6], 'BA': [7, 8, 9], 'PE': [10, 11], 'FA': [12, 13]}
default_color = "#1f77b4"
Library_of_books = get_dic_data()

# Helper Functions
def generate_character_colors(chapter_names):
    """Generate unique colors for each character."""
    unique_characters = sorted(set(name for chapter in chapter_names for name in chapter))
    colors = plt.cm.tab20(np.linspace(0, 1, len(unique_characters)))
    return {char: mcolors.to_hex(colors[i]) for i, char in enumerate(unique_characters)}

def compute_node_locations_per_chapter(chapter_names, relationships_data):
    """Compute node positions for each chapter independently using spring layout."""
    positions = []

    for chapter_idx, chapter in enumerate(chapter_names):
        G = nx.Graph()

        # Add nodes to the graph
        for i, name in enumerate(chapter):
            G.add_node(i, label=name)

        # Add edges based on relationships
        for i, rels in enumerate(relationships_data[chapter_idx]):
            for j, relation in enumerate(rels):
                if i != j and sum(relation) > 0:
                    G.add_edge(i, j, weight=sum(relation))

        # Compute spring layout positions for this chapter
        pos = nx.spring_layout(G, dim=2, scale=1)

        # Save positions for this layer
        layer_positions = [(chapter[i], pos[i]) for i in range(len(chapter))]
        positions.append(layer_positions)

    return positions

def convert_to_threejs_coordinates(node_positions, chapter_names, relationships_data, layer_gap=5, scale_factor=5):
    """Convert positions to Three.js-compatible format with relationship data."""
    json_data = {"title": "Generated Story Data", "layers": []}

    for layer_idx, (layer_nodes, relationships) in enumerate(zip(node_positions, relationships_data)):
        layer = {"layer_number": layer_idx + 1, "nodes": []}

        for i, (name, (x, y)) in enumerate(layer_nodes):
            # Create node data
            node_data = {
                "name": name,
                "x": x * scale_factor,
                "y": layer_idx * layer_gap,
                "z": y * scale_factor,
                "color": default_color,
                "relationships": []
            }

            # Add relationships to the node
            for j, rel_vector in enumerate(relationships[i]):
                if i != j and sum(rel_vector) > 0:  # Only include non-self relationships with positive emotion
                    target_name = chapter_names[layer_idx][j]
                    node_data["relationships"].append({
                        "target": target_name,
                        "emotions": rel_vector
                    })

            layer["nodes"].append(node_data)

        json_data["layers"].append(layer)
    return json_data

def save_to_json(data, file_name):
    """Save JSON data to a file."""
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {file_name}")

# Main Function
def process_story_data(chapter_names, relationships_data, output_file):
    """Process and save a book's chapter and relationship data as JSON."""
    colors = generate_character_colors(chapter_names)
    raw_positions = compute_node_locations_per_chapter(chapter_names, relationships_data)
    
    # Convert positions and embed relationship data
    threejs_data = convert_to_threejs_coordinates(raw_positions, chapter_names, relationships_data)
    for layer in threejs_data["layers"]:
        for node in layer["nodes"]:
            node["color"] = colors[node["name"]]
    
    save_to_json(threejs_data, output_file)

def get_book_names():
    """Get the list of book names."""
    return list(Library_of_books.keys())

# Process all books and save JSON files
def generate_all_books_json():
    """Generate JSON files for all books."""
    output_dir = "book_json_files"
    os.makedirs(output_dir, exist_ok=True)

    for book_name, (chapter_data, relationships_data) in Library_of_books.items():
        print(f"Processing book: {book_name}")
        output_file = os.path.join(output_dir, f"{book_name.replace(' ', '_').replace('\\', '')}.json")
        process_story_data(chapter_data, relationships_data, output_file)

if __name__ == "__main__":
    generate_all_books_json()

    # Output global JS code for books
    print("\n// Global variables")
    print("const books = [")
    for book in get_book_names():
        file_name = book.replace(" ", "_").replace("'", "") + ".json"
        print(f'  new Book("{book}", "{file_name}"),')
    print("];")
