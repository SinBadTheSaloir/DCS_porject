// Global variables
let scene, camera, renderer, controls;
const nodes = []; // To store all node objects
const nodeMeshes = {}; // To store node meshes for quick lookup by name

// Node Class Definition with Relationship Data

let currentBook; // Global Book object to store nodes and their layers

// Updated Book class to store nodes by layer

class Node {
  constructor(name, radius, color, relationships = [], metadata = {}) {
    this.name = name; // Node name
    this.radius = radius; // Node size
    this.color = color; // Node color
    this.relationships = relationships; // Array of relationships to other nodes
    this.metadata = metadata; // Additional metadata

    // Geometry and material
    this.geometry = new THREE.SphereGeometry(this.radius, 32, 32);
    this.material = new THREE.MeshBasicMaterial({
      color: this.color, // Solid color
    });
  }

  // Function to add a relationship
  addRelationship(targetNodeName, emotionArray) {
    if (emotionArray.length === 14) {
      this.relationships.push({
        target: targetNodeName,
        emotions: emotionArray,
      });
    } else {
      console.error("Emotion array must have exactly 14 elements.");
    }
  }

  // Function to display node relationships (for debugging)
  displayRelationships() {
    console.log(`Relationships for ${this.name}:`);
    this.relationships.forEach((rel) => {
      console.log(`- Target: ${rel.target}, Emotions: ${rel.emotions}`);
    });
  }
}

// Function to initialize the scene
function setScene() {
  scene = new THREE.Scene();
  console.log("Scene initialized");
}

// Function to set the renderer
function setRenderer() {
  renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  document.body.appendChild(renderer.domElement);
  console.log("Renderer set and added to DOM");
}

// Function to set the camera
function setCamera() {
  camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
  camera.position.set(0, 5, 10);
  console.log("Camera positioned at (0, 5, 10)");
}

// Function to add a grid helper
function setGridHelper() {
  const gridHelper = new THREE.GridHelper(50, 50);
  scene.add(gridHelper);
  console.log("Grid helper added to the scene");
}

// Function to set OrbitControls
function setControls() {
  controls = new THREE.OrbitControls(camera, renderer.domElement);
  controls.update();
  console.log("Orbit controls added to the scene");
}

function placeNode(nodeObject, x, y, z) {
  const nodeMesh = new THREE.Mesh(nodeObject.geometry, nodeObject.material);
  nodeMesh.position.set(x, y, z);
  nodeMesh.name = `${nodeObject.name}_Z${nodeObject.metadata.layer}`; // Unique per Z-level

  nodeMeshes[nodeMesh.name] = nodeMesh; // Store in global mesh tracker
  nodes.push({ object: nodeObject, mesh: nodeMesh }); // Add to global nodes array

  scene.add(nodeMesh);
  console.log(`Node "${nodeMesh.name}" placed at (${x}, ${y}, ${z})`);
}



// Function to create a wavy friendship edge
// Updated plotAllEdgesFromBook function to process layers and edges
function plotAllEdgesFromBook(book) {
  console.log(`Plotting edges for book: ${book.title}`);

  Object.entries(book.layers).forEach(([layerNumber, nodesInLayer]) => {
    console.log(`Processing Layer ${layerNumber}...`);

    // For each source node in the current layer
    nodesInLayer.forEach((sourceNode) => {
      const sourceMesh = nodeMeshes[`${sourceNode.name}_Z${layerNumber}`];
      if (!sourceMesh) return;

      // Process all relationships of the current node
      sourceNode.relationships.forEach((rel) => {
        const targetMesh = nodeMeshes[`${rel.target}_Z${layerNumber}`]; // Same layer target
        if (!targetMesh) return;

        // Plot edges based on emotion indices
        rel.emotions.forEach((weight, index) => {
          if (weight > 0) {
            const edgeKey = `${sourceMesh.name}-${targetMesh.name}-${index}`;
            if (plottedEdges.has(edgeKey)) return; // Avoid duplicates

            if (index === 0) {
              plotFriendshipEdge(sourceMesh, targetMesh);
            } else if (index === 3) {
              plotEnemiesEdge(sourceMesh, targetMesh);
            }
            plottedEdges.add(edgeKey);
          }
        });
      });
    });
  });
}


// Function to plot Friendship edges using a Bézier curve
function plotFriendshipEdge(sourceMesh, targetMesh) {
  const amplitude = 1.5;
  const points = [];
  const numPoints = 50;

  const sourcePos = sourceMesh.position;
  const targetPos = targetMesh.position;

  for (let t = 0; t <= 1; t += 1 / numPoints) {
    const x = THREE.MathUtils.lerp(sourcePos.x, targetPos.x, t);
    const z = THREE.MathUtils.lerp(sourcePos.z, targetPos.z, t);
    const y = sourcePos.y + amplitude * Math.sin(2 * Math.PI * t);
    points.push(new THREE.Vector3(x, y, z));
  }

  const curve = new THREE.CatmullRomCurve3(points);
  const geometry = new THREE.TubeGeometry(curve, 64, 0.05, 8, false);
  const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 }); // Bright Green
  const mesh = new THREE.Mesh(geometry, material);
  scene.add(mesh);
}

function plotEnemiesEdge(sourceMesh, targetMesh) {
  const points = [];
  const segments = 20;

  const sourcePos = sourceMesh.position;
  const targetPos = targetMesh.position;

  for (let i = 0; i <= segments; i++) {
    const t = i / segments;
    const x = THREE.MathUtils.lerp(sourcePos.x, targetPos.x, t);
    const y = sourcePos.y + (i % 2 === 0 ? 0.2 : -0.2); // Jagged
    const z = THREE.MathUtils.lerp(sourcePos.z, targetPos.z, t);
    points.push(new THREE.Vector3(x, y, z));
  }

  const geometry = new THREE.BufferGeometry().setFromPoints(points);
  const material = new THREE.LineBasicMaterial({ color: 0xff0000 }); // Red
  const line = new THREE.Line(geometry, material);
  scene.add(line);
}

// Function to plot Enemies edges using a wiggly line
function plotEnemiesEdge(sourceMesh, targetMesh) {
  const points = [];
  const numSegments = 50;

  const sourcePos = sourceMesh.position;
  const targetPos = targetMesh.position;

  for (let i = 0; i <= numSegments; i++) {
    const t = i / numSegments;
    const x = THREE.MathUtils.lerp(sourcePos.x, targetPos.x, t);
    const y = sourcePos.y + (i % 2 === 0 ? 0.2 : -0.2); // Alternating jagged Y
    const z = THREE.MathUtils.lerp(sourcePos.z, targetPos.z, t);
    points.push(new THREE.Vector3(x, y, z));
  }

  const geometry = new THREE.BufferGeometry().setFromPoints(points);
  const material = new THREE.LineBasicMaterial({ color: 0xff0000 }); // Red
  const line = new THREE.Line(geometry, material);
  scene.add(line);
}

// Placeholder for Family edges
function plotFamilyEdgePlaceholder(sourceMesh, targetMesh) {
  console.log(`Family edge placeholder between ${sourceMesh.name} and ${targetMesh.name}`);
}

// Placeholder for Romantic edges
function plotRomanticEdgePlaceholder(sourceMesh, targetMesh) {
  console.log(`Romantic edge placeholder between ${sourceMesh.name} and ${targetMesh.name}`);
}

// Master function to initialize the plotting process after loading nodes
function plotAllEdges() {
  if (currentBook) {
    plotAllEdgesFromBook(currentBook);
  } else {
    console.error("No book data loaded to plot edges.");
  }
}




// Function to load and parse JSON, then plot nodes and friendship edges
// Function to load and parse JSON, then plot nodes and edges
async function loadAndPlotNodes(jsonFile) {
  try {
    const response = await fetch(jsonFile);

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    if (!data.layers) {
      throw new Error("Invalid JSON structure: Missing 'layers' property.");
    }

    console.log(`Loaded JSON: ${data.title}`);

    clearScene(); // Safely clear the scene
    nodes.length = 0; // Reset nodes array
    Object.keys(nodeMeshes).forEach((key) => delete nodeMeshes[key]);
    plottedEdges.clear();

    // Process nodes and layers
    currentBook = new Book(data.title);
    data.layers.forEach((layer) => {
      if (!layer.nodes) return; // Ensure nodes exist
      layer.nodes.forEach((nodeData) => {
        const node = new Node(
          nodeData.name,
          0.5,
          nodeData.color,
          nodeData.relationships || [],
          { layer: layer.layer_number }
        );
        placeNode(node, nodeData.x, nodeData.y, nodeData.z);
        currentBook.addNodeToLayer(layer.layer_number, node);
      });
    });

    plotAllEdges();
    currentBook.displayNodes();

  } catch (error) {
    console.error("Error loading or parsing JSON:", error);
  }
}


// Function to clear the existing scene

// **1. Friendship Edge** - Bright Green Sine Wave
function drawFriendshipEdge(sourceMesh, targetMesh, invert = false) {
  const amplitude = 2;
  const points = [];
  const numPoints = 50;

  const sourcePos = sourceMesh.position;
  const targetPos = targetMesh.position;

  for (let t = 0; t <= 1; t += 1 / numPoints) {
    const x = THREE.MathUtils.lerp(sourcePos.x, targetPos.x, t);
    const z = THREE.MathUtils.lerp(sourcePos.z, targetPos.z, t);
    const y =
      THREE.MathUtils.lerp(sourcePos.y, targetPos.y, t) +
      amplitude * Math.sin(2 * Math.PI * t) * (invert ? -1 : 1);

    points.push(new THREE.Vector3(x, y, z));
  }

  const curve = new THREE.CatmullRomCurve3(points);
  const geometry = new THREE.TubeGeometry(curve, 50, 0.05, 8, false);
  const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 }); // Bright Green
  const edgeMesh = new THREE.Mesh(geometry, material);
  scene.add(edgeMesh);
}

function drawFamilyEdge(sourceMesh, targetMesh) {
  const sourcePos = sourceMesh.position;
  const targetPos = targetMesh.position;

  const points = [
    new THREE.Vector3(sourcePos.x, sourcePos.y, sourcePos.z),
    new THREE.Vector3(targetPos.x, targetPos.y, targetPos.z),
  ];

  const geometry = new THREE.BufferGeometry().setFromPoints(points);

  const material = new THREE.LineBasicMaterial({
    color: 0x000000, // Black
    linewidth: 2,
    opacity: 0.5,
    transparent: true,
  });

  const line = new THREE.Line(geometry, material);
  scene.add(line);
}

function drawRomanticInterestEdge(sourceMesh, targetMesh) {
  const sourcePos = sourceMesh.position;
  const targetPos = targetMesh.position;

  const points = [
    new THREE.Vector3(sourcePos.x, sourcePos.y, sourcePos.z),
    new THREE.Vector3(targetPos.x, targetPos.y, targetPos.z),
  ];

  const geometry = new THREE.BufferGeometry().setFromPoints(points);

  const material = new THREE.LineDashedMaterial({
    color: 0xffc0cb, // Soft Pink
    dashSize: 0.5,
    gapSize: 0.2,
    linewidth: 2,
  });

  const line = new THREE.Line(geometry, material);
  line.computeLineDistances();
  scene.add(line);

  // Particles moving along the line
  const particleMaterial = new THREE.PointsMaterial({ color: 0xffc0cb, size: 0.1 });
  const particleGeometry = new THREE.BufferGeometry().setFromPoints(points);
  const particles = new THREE.Points(particleGeometry, particleMaterial);
  scene.add(particles);
}
function drawEnemiesEdge(sourceMesh, targetMesh) {
  const sourcePos = sourceMesh.position;
  const targetPos = targetMesh.position;

  const points = [];
  const numSegments = 20;

  for (let i = 0; i <= numSegments; i++) {
    const t = i / numSegments;
    const x = THREE.MathUtils.lerp(sourcePos.x, targetPos.x, t);
    const y =
      sourcePos.y +
      (i % 2 === 0 ? 0.2 : -0.2); // Jagged effect
    const z = THREE.MathUtils.lerp(sourcePos.z, targetPos.z, t);

    points.push(new THREE.Vector3(x, y, z));
  }

  const geometry = new THREE.BufferGeometry().setFromPoints(points);
  const material = new THREE.LineBasicMaterial({
    color: 0xff0000, // Deep Red
    linewidth: 2,
    opacity: 0.8,
    transparent: true,
  });

  const line = new THREE.Line(geometry, material);
  scene.add(line);

  // Flicker animation
  function flicker() {
    material.opacity = Math.random() * 0.6 + 0.4;
    requestAnimationFrame(flicker);
  }
  flicker();
}




// Global Edge Tracker
const plottedEdges = new Set(); // To track edges and avoid duplicates

// Emotion Colors
const emotionColors = {
  0: 0x00ff00, // Friendship: Bright Green
  1: 0x000000, // Family: Black
  2: 0xffc0cb, // Love: Soft Pink
  3: 0xff0000, // Enemies: Red
};

// Bézier Quadratic Curve Function
function plotBezierQuadratic(source, target, color, flip = false, offset = 0.5) {
  const sourcePos = source.position;
  const targetPos = target.position;

  // Midpoint as control point
  const controlX = (sourcePos.x + targetPos.x) / 2;
  const controlY = (sourcePos.y + targetPos.y) / 2 + (flip ? offset : -offset);
  const controlPoint = new THREE.Vector3(controlX, controlY, sourcePos.z);

  // Create a Bézier Curve
  const curve = new THREE.QuadraticBezierCurve3(
    new THREE.Vector3(sourcePos.x, sourcePos.y, sourcePos.z), // Start
    controlPoint, // Control Point
    new THREE.Vector3(targetPos.x, targetPos.y, targetPos.z) // End
  );

  const points = curve.getPoints(50);
  const geometry = new THREE.BufferGeometry().setFromPoints(points);
  const material = new THREE.LineBasicMaterial({ color });
  const bezierLine = new THREE.Line(geometry, material);
  scene.add(bezierLine);
}

// Straight Line Function
function plotStraightLine(source, target, color, offset = 0.3, flip = false) {
  const sourcePos = source.position;
  const targetPos = target.position;

  // Offset perpendicular direction
  const direction = new THREE.Vector3()
    .subVectors(targetPos, sourcePos)
    .normalize();
  const offsetVector = new THREE.Vector3(-direction.y, direction.x, 0).multiplyScalar(offset);

  const start = new THREE.Vector3(
    sourcePos.x + (flip ? -offsetVector.x : offsetVector.x),
    sourcePos.y + (flip ? -offsetVector.y : offsetVector.y),
    sourcePos.z
  );

  const end = new THREE.Vector3(
    targetPos.x + (flip ? -offsetVector.x : offsetVector.x),
    targetPos.y + (flip ? -offsetVector.y : offsetVector.y),
    targetPos.z
  );

  const points = [start, end];
  const geometry = new THREE.BufferGeometry().setFromPoints(points);
  const material = new THREE.LineBasicMaterial({ color });
  const line = new THREE.Line(geometry, material);
  scene.add(line);
}

// Wiggly Line Function
function plotWigglyLine(source, target, color, amplitude = 0.3, frequency = 4, flip = false) {
  const sourcePos = source.position;
  const targetPos = target.position;
  const points = [];
  const segments = 50;

  for (let i = 0; i <= segments; i++) {
    const t = i / segments;
    const x = THREE.MathUtils.lerp(sourcePos.x, targetPos.x, t);
    const y =
      THREE.MathUtils.lerp(sourcePos.y, targetPos.y, t) +
      amplitude * Math.sin(frequency * Math.PI * t) * (flip ? -1 : 1);
    const z = sourcePos.z;
    points.push(new THREE.Vector3(x, y, z));
  }

  const geometry = new THREE.BufferGeometry().setFromPoints(points);
  const material = new THREE.LineBasicMaterial({ color });
  const wigglyLine = new THREE.Line(geometry, material);
  scene.add(wigglyLine);
}

// Edge Plotting Function
function plotEdge(sourceMesh, targetMesh, emotions, sourceZ, targetZ) {
  if (sourceZ !== targetZ) return; // Ensure nodes are on the same Z-level

  emotions.forEach((weight, index) => {
    if (weight > 0) {
      const edgeKey = `${sourceMesh.name}-${targetMesh.name}-${index}`;
      const reverseKey = `${targetMesh.name}-${sourceMesh.name}-${index}`;

      if (plottedEdges.has(edgeKey) || plottedEdges.has(reverseKey)) return;

      // Plot edge based on emotion type
      if (index === 0) plotBezierQuadratic(sourceMesh, targetMesh, emotionColors[0]); // Friendship
      else if (index === 1) plotStraightLine(sourceMesh, targetMesh, emotionColors[1]); // Family
      else if (index === 2) plotStraightLine(sourceMesh, targetMesh, emotionColors[2]); // Love
      else if (index === 3) plotWigglyLine(sourceMesh, targetMesh, emotionColors[3]); // Enemies

      plottedEdges.add(edgeKey); // Track plotted edge
    }
  });
}







// Master function to initialize everything
// Master function to initialize everything
function make_scene(jsonFile) {
  if (!scene) setScene(); // Ensure scene is initialized
  setRenderer();
  setCamera();
  setGridHelper();
  setControls();

  loadAndPlotNodes(jsonFile);

  function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
  }
  animate();
}


class Book {
  constructor(name, path) {
    this.name = name;   // Book title
    this.path = path;   // Path to the JSON file
    this.layers = {};   // Initialize layers as an empty object
  }

  // Function to add a node to a specific layer
  addNodeToLayer(layerNumber, nodeObject) {
    if (!this.layers[layerNumber]) {
      this.layers[layerNumber] = []; // Initialize layer if it doesn't exist
    }
    this.layers[layerNumber].push(nodeObject); // Add the node to the specified layer
  }

  // Function to display nodes in the book (for debugging)
  displayNodes() {
    console.log(`Nodes in book: ${this.name}`);
    Object.entries(this.layers).forEach(([layer, nodes]) => {
      console.log(`Layer ${layer}:`);
      nodes.forEach((node, index) => {
        console.log(`  ${index + 1}. ${node.name}`);
      });
    });
  }
}

// Global variables
const books = [
  new Book("Alice's Adventures in Wonderland", "./book_json_files/Alice's_Adventures_in_Wonderland.json"),
  new Book("The Count of Monte Cristo", "./book_json_files/The_Count_of_Monte_Cristo.json"),
  new Book("The Metamorphosis", "./book_json_files/The_Metamorphosis.json"),
  new Book("The Odyssey", "./book_json_files/The_Odyssey.json"),
  new Book("The Picture of Dorian Gray", "./book_json_files/The_Picture_of_Dorian_Gray.json"),
  new Book("The Strange Case of Dr. Jekyll and Mr. Hyde", "./book_json_files/The_Strange_Case_of_Dr._Jekyll_and_Mr._Hyde.json")
];


// Function to populate the dropdown
function populateLibraryDropdown() {
  const dropdown = document.getElementById("book-selector");
  dropdown.innerHTML = "<option value=''>-- Select a Book --</option>"; // Default option

  books.forEach((book) => {
    const option = document.createElement("option");
    option.value = book.path;   // Store file path in value
    option.textContent = book.name;
    dropdown.appendChild(option);
  });
}
// Function to load selected book data
function loadSelectedBook() {
  const dropdown = document.getElementById("book-selector");
  const selectedPath = dropdown.value;

  if (selectedPath) {
    console.log(`Fetching JSON file: ${selectedPath}`);
    clearScene();
    loadAndPlotNodes(selectedPath); // Pass the valid file path
  } else {
    alert("Please select a book from the Library.");
  }
}

function clearScene() {
  if (!scene) {
    console.error("Scene is not initialized. Cannot clear.");
    return;
  }
  console.log("Clearing the scene...");
  
  // Remove all children from the scene
  for (let i = scene.children.length - 1; i >= 0; i--) {
    scene.remove(scene.children[i]);
  }

  setGridHelper(); // Re-add grid helper to reset visuals
}

// Function to clear previous data or scene

// Initialize dropdown and attach event listeners
// Initialize dropdown and attach event listeners
document.addEventListener("DOMContentLoaded", () => {
  populateLibraryDropdown(); // Correct function name to populate the dropdown

  const loadButton = document.getElementById("load-book");
  loadButton.addEventListener("click", () => {
    loadSelectedBook();
  });

  // Initialize the scene on page load with a placeholder JSON or clear scene
  make_scene("./book_json_files/Alice's_Adventures_in_Wonderland.json");
});
