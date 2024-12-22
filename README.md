README for Narrative Nexus Project

Project Goal and Scope

The Narrative Nexus project aims to revolutionize how narratives are visualized by creating a dynamic 3D visualization engine. The system focuses on representing characters (nodes) and their emotional interactions (edges) within stories such as The Count of Monte Cristo. Using tools like Three.js for 3D rendering and Python for backend calculations, the project provides:

Character Dynamics: Nodes represent characters, placed on Z-levels corresponding to chapters.

Emotional Relationships: Edges represent emotional interactions, color-coded and weighted based on their strength.

Interactive Visualization: Users can explore narratives dynamically, viewing relationships and progression.

The ultimate goal is to analyze and visualize stories to uncover deeper narrative patterns and dynamics.

Required Non-Default Libraries

The project utilizes the following Python libraries:

networkx

numpy

matplotlib

plotly

itertools

json

Additionally, the frontend uses:

Three.js (JavaScript library for 3D rendering).

Installation Instructions

Python Libraries

To install the required Python libraries, use the following command:

pip install networkx numpy matplotlib plotly

Three.js

Download the latest build of Three.js from the official website, or include it via a CDN:

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/0.154.0/three.min.js"></script>
<script src="https://threejs.org/examples/js/controls/OrbitControls.js"></script>

Execution Instructions

Backend Setup

Data Preparation:

Place your chapter and relationship data as JSON files in the data directory.

Generate JSON files for nodes and edges using the json_prep.py script:

python json_prep.py

Run Graph Plotting:

Use the Graph_plotter_functions.py to prepare visualizations:

python Graph_plotter_functions.py

Frontend Setup

File Structure:

Ensure your directory contains the following files:

3d_image.js

JSON files generated in the backend (data_*.json)

Include these in an HTML file to initialize the Three.js scene.

Run the Visualization:

Open your HTML file in a browser. The visualization will render interactively.

Use dropdown menus to select books and characters.

Example Workflow

Prepare narrative data in matrix form.

Generate node and edge data using backend scripts.

Visualize the results using Three.js by loading the generated JSON files.

Key Features

Dropdown Menus: Select books and explore their emotional graphs.

Node-Edge Interactivity: Visualize relationships dynamically.

Snapshot Functionality: Capture 2D projections of the 3D graph.
