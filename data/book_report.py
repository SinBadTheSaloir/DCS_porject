from The_Great_Gatsby_data import get_data_full_GG
from Comm_data import get_data_full
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.widgets import Cursor
import json
import os


def find_largest(total_emotions):
    largest = 0
    larg_v = 0
    for i in range (len(total_emotions)):
        value = total_emotions[i]
        if value >larg_v:
            larg_v = value
            largest = i
    return largest,larg_v



def plot_all_chapters_emotional_intensity(chapters_data):
    """
    Sums the total emotional intensity for each chapter and plots a bar chart
    showing the total emotional intensity for all chapters.

    Parameters:
    - chapters_data (list of 3D arrays): List containing emotional intensity matrices for each chapter.
    """
    total_emotions = []

    # Calculate total emotional intensity for each chapter
    for chapter_data in chapters_data:
        total_intensity = 0
        for character_data in chapter_data:
            for relationship in character_data:
                total_intensity += np.sum(relationship)  # Sum all values in the relationship matrix
        total_emotions.append(total_intensity)

    biggest_ = find_largest(total_emotions)
    print(biggest_)
    # Generate chapter names
    chapter_names = [f"Chapter {i+1}" for i in range(len(chapters_data))]

    # Plot the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(chapter_names, total_emotions, color='skyblue')
    plt.xlabel("Chapters")
    plt.ylabel("Total Emotional Intensity")
    plt.title("Total Emotional Intensity per Chapter")
    plt.xticks(rotation=45)  # Rotate x labels for better readability
    plt.tight_layout()
    plt.show()


def plot_character_centrality_over_time(relationships_data, character_names):
    # Iterate through each chapter's data and plot centrality
    for chapter_index, (chapter_data, names) in enumerate(zip(relationships_data, character_names)):
        # Create a graph for each chapter
        G = nx.Graph()

        # Add nodes
        for name in names:
            G.add_node(name)

        # Add edges with weights from the relationships data
        for i in range(len(names)):
            for j in range(len(names)):
                if i != j:  # Ignore self-relations
                    weight = sum(chapter_data[i][j])
                    if weight > 0:
                        G.add_edge(names[i], names[j], weight=weight)

        # Calculate centrality (using degree centrality as an example)
        centrality = nx.degree_centrality(G)

        # Sort characters by name
        sorted_names = sorted(centrality.keys())
        sorted_centrality = [centrality[name] for name in sorted_names]

        # Plot the centrality for this chapter
        plt.figure(figsize=(10, 5))
        plt.bar(sorted_names, sorted_centrality, color='skyblue')
        plt.title(f"Character Centrality in Chapter {chapter_index + 1}")
        plt.xlabel("Characters")
        plt.ylabel("Centrality (Degree)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def plot_all_chapters_emotional_intensity2(relationships_data, character_names):
    chapter_intensities = []

    for chapter_index, chapter_data in enumerate(relationships_data):
        chapter_total_intensity = 0
        number_of_people = len(character_names[chapter_index])

        # Iterate over each character's relationships in the chapter
        for character_relationships in chapter_data:
            for relationship in character_relationships:
                chapter_total_intensity += sum(relationship)

        # Adjust intensity by the number of people
        if number_of_people > 0:
            average_intensity = chapter_total_intensity / number_of_people
        else:
            average_intensity = 0

        chapter_intensities.append(average_intensity)

    # Plot the adjusted emotional intensity for all chapters
    plt.figure(figsize=(12, 6))
    plt.bar(range(1, len(chapter_intensities) + 1), chapter_intensities, color='skyblue')
    plt.xlabel('Chapters')
    plt.ylabel('Average Emotional Intensity')
    plt.title('Average Emotional Intensity per Chapter (Adjusted for Number of People)')
    plt.xticks(range(1, len(chapter_intensities) + 1))
    plt.show()


def plot_normalized_chapter_intensity3(relationships_data, character_names):
    chapter_intensities = []

    for chapter_index, chapter_data in enumerate(relationships_data):
        chapter_total_intensity = 0
        number_of_people = len(character_names[chapter_index])

        # Calculate the total intensity for the chapter
        for character_relationships in chapter_data:
            for relationship in character_relationships:
                chapter_total_intensity += sum(relationship)

        # Calculate the number of potential interactions: n * (n - 1)
        if number_of_people > 1:
            potential_interactions = number_of_people * (number_of_people - 1)
            normalized_intensity = chapter_total_intensity / potential_interactions
        else:
            normalized_intensity = 0  # No interactions if there are fewer than 2 people

        chapter_intensities.append(normalized_intensity)

    # Plot the normalized emotional intensity for all chapters
    plt.figure(figsize=(12, 6))
    plt.bar(range(1, len(chapter_intensities) + 1), chapter_intensities, color='lightcoral')
    plt.xlabel('Chapters')
    plt.ylabel('Normalized Emotional Intensity')
    plt.title('Normalized Emotional Intensity per Chapter (Adjusted for Potential Interactions)')
    plt.xticks(range(1, len(chapter_intensities) + 1))
    plt.show()

def plot_normalized_chapter_intensity4(relationships_data, character_names):
    chapter_intensities = []
    chapter_info = []

    for chapter_index, chapter_data in enumerate(relationships_data):
        chapter_total_intensity = 0
        number_of_people = len(character_names[chapter_index])

        # Calculate the total intensity for the chapter
        for character_relationships in chapter_data:
            for relationship in character_relationships:
                chapter_total_intensity += sum(relationship)

        # Calculate the number of potential interactions: n * (n - 1)
        if number_of_people > 1:
            potential_interactions = number_of_people * (number_of_people - 1)
            normalized_intensity = chapter_total_intensity / potential_interactions
        else:
            normalized_intensity = 0  # No interactions if there are fewer than 2 people

        chapter_intensities.append(normalized_intensity)
        chapter_info.append(f"Chapter {chapter_index + 1}: {character_names[chapter_index]}")

    # Set up color gradient
    norm = mcolors.Normalize(vmin=min(chapter_intensities), vmax=max(chapter_intensities))
    colors = plt.cm.Reds(norm(chapter_intensities))

    # Plot the normalized emotional intensity for all chapters
    fig, ax = plt.subplots(figsize=(14, 7))
    bars = ax.bar(range(1, len(chapter_intensities) + 1), chapter_intensities, color=colors)
    ax.set_xlabel('Chapters', fontsize=12)
    ax.set_ylabel('Normalized Emotional Intensity', fontsize=12)
    ax.set_title('Normalized Emotional Intensity per Chapter (Adjusted for Potential Interactions)', fontsize=14)
    ax.set_xticks(range(1, len(chapter_intensities) + 1))
    ax.set_xticklabels(range(1, len(chapter_intensities) + 1), rotation=45, ha='right')

    # Add interactivity with a cursor
    cursor = Cursor(ax, useblit=True, color='gray', linewidth=1)

    # Function to display chapter information on hover
    def on_hover(event):
        if event.inaxes == ax:
            for bar, info in zip(bars, chapter_info):
                if bar.contains(event)[0]:
                    plt.gca().set_title(f"{info} - Intensity: {bar.get_height():.2f}", fontsize=14)
                    break
            else:
                plt.gca().set_title('Normalized Emotional Intensity per Chapter (Adjusted for Potential Interactions)', fontsize=14)
        plt.draw()

    # Connect the hover event
    fig.canvas.mpl_connect("motion_notify_event", on_hover)

    plt.tight_layout()
    plt.show()


def write_full_json(data, chapter_names, file_name):
    """
    Creates a new JSON file, stores the provided data and chapter names,
    and saves it in the required format for the JavaScript function.

    Parameters:
    data (list): The data to be written to the JSON file.
    chapter_names (list): The chapter names to be included in the JSON structure.
    file_name (str): The name of the JSON file to create and write the data to.
    """
    try:
        # Ensure the file is created as new by removing any existing file
        if os.path.exists(file_name):
            os.remove(file_name)

        # Construct the full JSON structure
        json_structure = {
            "chapters": chapter_names,
            "data": data
        }

        # Write to the new JSON file
        with open(file_name, 'w') as json_file:
            json.dump(json_structure, json_file, indent=4)
        
        print(f"Data successfully written to {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")


def create_chapters_json(chapter_names, relationships_data, output_file="new_story_data.json"):
    data = {"chapters": []}
    for i, (names, relationships) in enumerate(zip(chapter_names, relationships_data)):
        chapter = {
            "chapter_number": i + 1,
            "names": names,
            "relationships": relationships
        }
        data["chapters"].append(chapter)

    with open(output_file, "w") as f:
        json.dump(data, f, indent=4)

    print(f"JSON saved to {output_file}")

chapter_names, relationships_data = get_data_full_GG()
file_name = "book_data_gg.json"

create_chapters_json(chapter_names, relationships_data,file_name)
#plot_all_chapters_emotional_intensity(relationships_data)
#plot_all_chapters_emotional_intensity2(relationships_data,chapter_names)
#plot_normalized_chapter_intensity3(relationships_data, chapter_names)
#plot_normalized_chapter_intensity4(relationships_data, chapter_names)

