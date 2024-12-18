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


//
// Place node code for placing node 
//


function placeNode(nodeObject, x, y, z) {
  const nodeMesh = new THREE.Mesh(nodeObject.geometry, nodeObject.material);
  nodeMesh.position.set(x, y, z);
  nodeMesh.name = `${nodeObject.name}_Z${nodeObject.metadata.layer}`; // Unique per Z-level

  nodeMeshes[nodeMesh.name] = nodeMesh; // Store in global mesh tracker
  nodes.push({ object: nodeObject, mesh: nodeMesh }); // Add to global nodes array

  scene.add(nodeMesh);
  console.log(`Node "${nodeMesh.name}" placed at (${x}, ${y}, ${z})`);
}
async function loadAndPlotNodes(jsonFile) {
  try {
    if (!scene) setScene(); // Ensure the scene is initialized before adding nodes

    const response = await fetch(jsonFile);
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

    const data = await response.json();
    if (!data.layers) throw new Error("Invalid JSON structure: Missing 'layers' property.");

    console.log(`Loaded JSON: ${data.title}`);

    clearScene(); // Safely clear the scene
    nodes.length = 0;
    Object.keys(nodeMeshes).forEach((key) => delete nodeMeshes[key]);
    plottedEdges.clear();

    currentBook = new Book(data.title);
    data.layers.forEach((layer) => {
      if (!layer.nodes) return;
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

    const totalChapters = Object.keys(currentBook.layers).length;
    updateChapterScrollbar(totalChapters); // Update the scrollbar dynamically
  } catch (error) {
    console.error("Error loading or parsing JSON:", error);
  }
}

function updateChapterScrollbar(totalChapters) {
  const scrollBar = document.getElementById("chapter-scrollbar");
  if (scrollBar) {
    scrollBar.max = totalChapters - 1; // Set max to total chapters minus 1
    scrollBar.value = 0; // Reset to first chapter
    console.log(`Scrollbar updated: 0 to ${scrollBar.max}`);
  }
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Function to create a wavy friendship edge
// Updated plotAllEdgesFromBook function to process layers and edges
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



// Master Edge Plotting Configuration
const EDGE_PLOT_FUNCTIONS = {
  0: { color: 0x00ff00, plot: plotFriendshipEdge },        // Friendship
  1: { color: 0x000000, plot: plotFamilyEdge },            // Family
  2: { color: 0xffc0cb, plot: plotRomanticEdge },          // Romantic
  3: { color: 0xff0000, plot: plotEnemiesEdge },           // Enemies
  4: { color: 0x6a0dad, plot: plotPoliticalAlignmentEdge },// Political Alignment
  5: { color: 0xffd700, plot: plotEmploymentRelationshipEdge }, // Employment Relationship
  6: { color: 0xc0c0c0, plot: plotSocialStandingEdge },    // Social Standing
  7: { color: 0xffffff, plot: plotTrustEdge },             // Trust
  8: { color: 0xffd700, plot: plotRespectEdge },           // Respect
  9: { color: 0x87cefa, plot: plotCommunicationEdge },     // Communication
};



// Global Edge Tracker

// Master Edge Plotting Function
function plotEdge(sourceMesh, targetMesh, emotions) {
  emotions.forEach((weight, index) => {
    if (weight > 0 && EDGE_PLOT_FUNCTIONS[index]) {
      const edgeKey = `${sourceMesh.name}-${targetMesh.name}-${index}`;
      if (plottedEdges.has(edgeKey)) return; // Avoid duplicates

      EDGE_PLOT_FUNCTIONS[index].plot(sourceMesh, targetMesh);
      plottedEdges.add(edgeKey);
    }
  });
}

// Plot All Edges from Book
function plotAllEdgesFromBook(book) {
  console.log(`Plotting edges for book: ${book.title}`);

  Object.entries(book.layers).forEach(([layerNumber, nodesInLayer]) => {
    console.log(`Processing Layer ${layerNumber}...`);

    nodesInLayer.forEach((sourceNode) => {
      const sourceMesh = nodeMeshes[`${sourceNode.name}_Z${layerNumber}`];
      if (!sourceMesh) return;

      sourceNode.relationships.forEach((rel) => {
        const targetMesh = nodeMeshes[`${rel.target}_Z${layerNumber}`];
        if (!targetMesh) return;

        plotEdgeWithOffset(sourceMesh, targetMesh, rel.emotions);
      });
    });
  });
}
function findNodePositionOnLowerLevel(nodeName, currentLayer) {
  // Start checking from the layer below the current one
  for (let layer = currentLayer - 1; layer >= 0; layer--) {
    const targetMesh = nodeMeshes[`${nodeName}_Z${layer}`];
    if (targetMesh) {
      return targetMesh.position.clone(); // Return the position
    }
  }

  // Fallback: Return the current node's position shifted down a Z level
  console.warn(`Node "${nodeName}" not found on lower levels. Falling back.`);
  return new THREE.Vector3(0, -CHAPTER_SPACING, 0); // Default fallback
}
function plotPastExperienceEdge(sourceMesh, targetMesh, relationshipType, scale, currentLayer) {
  // Determine color based on relationship type
  const color = relationshipType === "Shared History" ? 0x00ff00 : 0xff0000; // Green for good, Red for bad

  // Find target position on the lower Z-level
  const lowerTargetPos = findNodePositionOnLowerLevel(targetMesh.name.split('_')[0], currentLayer);
  const sourcePos = sourceMesh.position;

  // If fallback, shift down the target position
  if (!lowerTargetPos) {
    lowerTargetPos.copy(targetMesh.position);
    lowerTargetPos.y -= CHAPTER_SPACING; // Shift down by chapter spacing
  }

  // Geometry for dotted line
  const points = [sourcePos.clone(), lowerTargetPos];
  const geometry = new THREE.BufferGeometry().setFromPoints(points);

  // Dashed Line Material
  const material = new THREE.LineDashedMaterial({
    color: color,
    dashSize: 0.5, // Length of dashes
    gapSize: 0.2,  // Space between dashes
    linewidth: scale * 0.1, // Line thickness proportional to scale
  });

  // Create the line and compute dash distances
  const line = new THREE.Line(geometry, material);
  line.computeLineDistances();

  // Add to the scene
  scene.add(line);

  console.log(`Plotted PE edge (${relationshipType}) between ${sourceMesh.name} and ${targetMesh.name}`);
}
function plotEdgeWithOffset(sourceMesh, targetMesh, emotions, currentLayer) {
  emotions.forEach((weight, index) => {
    if (weight > 0) {
      if (index === 0) { // Shared History (Good - index 0)
        plotPastExperienceEdge(sourceMesh, targetMesh, "Shared History", weight, currentLayer);
      } else if (index === 1) { // Conflict History (Bad - index 1)
        plotPastExperienceEdge(sourceMesh, targetMesh, "Conflict History", weight, currentLayer);
      } else {
        console.warn(`Unhandled emotion index: ${index}`);
      }
    }
  });
}

// Edge Plotting Functions
function plotFriendshipEdge(sourceMesh, targetMesh) {
  plotQuadraticBezierEdge(sourceMesh, targetMesh, 0x00ff00, 1.5); // Bright Green
}

function plotEnemiesEdge(sourceMesh, targetMesh) {
  plotJaggedEdge(sourceMesh, targetMesh, 0xff0000); // Red
}

function plotFamilyEdge(sourceMesh, targetMesh) {
  plotThickGlowingLine(sourceMesh, targetMesh, 0x000000); // Black
}

function plotRomanticEdge(sourceMesh, targetMesh) {
  plotThickGlowingLine(sourceMesh, targetMesh, 0xffc0cb); // Soft Pink
}
function plotPoliticalAlignmentEdge(sourceMesh, targetMesh) {
  plotDoubleHelixEdge(sourceMesh, targetMesh, 0x6a0dad, 3); // Purple with 3 twists
}

function plotEmploymentRelationshipEdge(sourceMesh, targetMesh) {
  plotArrowRibbonEdge(sourceMesh, targetMesh, 0xffd700); // Gold
}
function plotTrustEdge(sourceMesh, targetMesh) {
  plotGlowingThreadEdge(sourceMesh, targetMesh, 0x00ffff, 0xffffff); // Cyan to White Glow
}

function plotRespectEdge(sourceMesh, targetMesh) {
  plotArchingBridgeEdge(sourceMesh, targetMesh, 0xcd7f32, 0xffd700); // Bronze to Gold Arch
}

function plotCommunicationEdge(sourceMesh, targetMesh) {
  plotWavyParticleEdge(sourceMesh, targetMesh, 0x00008b, 0x87cefa); // Dark Blue to Sky Blue
}


function plotSocialStandingEdge(sourceMesh, targetMesh) {
  const sourcePos = sourceMesh.position;
  const targetPos = targetMesh.position;

  // Determine color based on relative social standing
  const color = (sourcePos.y + targetPos.y) / 2 > 5 ? 0xffd700 : 0x808080; // Gold for high, Grey for low

  // Calculate control point (below the midpoint of the nodes)
  const controlPoint = new THREE.Vector3(
    (sourcePos.x + targetPos.x) / 2,      // Midpoint X
    Math.min(sourcePos.y, targetPos.y) - 2, // Offset downward below nodes
    (sourcePos.z + targetPos.z) / 2       // Midpoint Z
  );

  // Create a Quadratic Bézier Curve
  const curve = new THREE.QuadraticBezierCurve3(
    new THREE.Vector3(sourcePos.x, sourcePos.y, sourcePos.z), // Start point
    controlPoint,                                             // Control point (below midpoint)
    new THREE.Vector3(targetPos.x, targetPos.y, targetPos.z)  // End point
  );

  // Generate points for the curve
  const points = curve.getPoints(50);

  // Create geometry and material for the curve
  const geometry = new THREE.BufferGeometry().setFromPoints(points);
  const material = new THREE.LineBasicMaterial({ color: color, linewidth: 2 });

  // Create a line object and add it to the scene
  const bezierLine = new THREE.Line(geometry, material);
  scene.add(bezierLine);
}

//
/// helper 
//
function plotGlowingThreadEdge(sourceMesh, targetMesh, lowColor, highColor) {
  const sourcePos = sourceMesh.position;
  const targetPos = targetMesh.position;

  // Calculate color based on midpoint height (as a placeholder for trust strength)
  const trustStrength = (sourcePos.y + targetPos.y) / 2; // Example trust scaling
  const color = trustStrength > 5 ? highColor : lowColor;

  const geometry = new THREE.BufferGeometry().setFromPoints([
    sourcePos.clone(),
    targetPos.clone(),
  ]);

  const material = new THREE.LineBasicMaterial({
    color: color,
    linewidth: 1,
    transparent: true,
    opacity: 0.8,
  });

  // Create glowing effect
  const line = new THREE.Line(geometry, material);
  scene.add(line);

  // Add pulsing glow effect
  const clock = new THREE.Clock();
  function animateGlow() {
    const time = clock.getElapsedTime();
    material.opacity = 0.6 + 0.4 * Math.sin(time * 2); // Pulse between 0.6 and 1
    requestAnimationFrame(animateGlow);
  }
  animateGlow();
}
function plotArchingBridgeEdge(sourceMesh, targetMesh, lowColor, highColor) {
  const sourcePos = sourceMesh.position;
  const targetPos = targetMesh.position;

  // Calculate color based on relative node height
  const respectStrength = (sourcePos.y + targetPos.y) / 2;
  const color = respectStrength > 5 ? highColor : lowColor;

  // Control point for arching effect (above the midpoint)
  const controlPoint = new THREE.Vector3(
    (sourcePos.x + targetPos.x) / 2,    // Midpoint X
    Math.max(sourcePos.y, targetPos.y) + 2, // Offset upward
    (sourcePos.z + targetPos.z) / 2     // Midpoint Z
  );

  // Quadratic Bézier curve for the arch
  const curve = new THREE.QuadraticBezierCurve3(
    sourcePos.clone(),
    controlPoint,
    targetPos.clone()
  );

  const points = curve.getPoints(50);
  const geometry = new THREE.BufferGeometry().setFromPoints(points);
  const material = new THREE.LineBasicMaterial({ color: color, linewidth: 3 });

  const archLine = new THREE.Line(geometry, material);
  scene.add(archLine);
}
function plotWavyParticleEdge(sourceMesh, targetMesh, lowColor, highColor) {
  const points = [];
  const numPoints = 50;
  const sourcePos = sourceMesh.position;
  const targetPos = targetMesh.position;

  // Wavy curve points
  for (let i = 0; i <= numPoints; i++) {
    const t = i / numPoints;
    const x = THREE.MathUtils.lerp(sourcePos.x, targetPos.x, t);
    const y = THREE.MathUtils.lerp(sourcePos.y, targetPos.y, t) + Math.sin(10 * t) * 0.5; // Wavy motion
    const z = THREE.MathUtils.lerp(sourcePos.z, targetPos.z, t);
    points.push(new THREE.Vector3(x, y, z));
  }

  const geometry = new THREE.BufferGeometry().setFromPoints(points);
  const material = new THREE.LineBasicMaterial({ color: lowColor, linewidth: 2 });

  const wavyLine = new THREE.Line(geometry, material);
  scene.add(wavyLine);

  // Add particle flow
  const particleGeometry = new THREE.SphereGeometry(0.1, 8, 8);
  const particleMaterial = new THREE.MeshBasicMaterial({ color: highColor });
  const particle = new THREE.Mesh(particleGeometry, particleMaterial);
  scene.add(particle);

  let t = 0;
  function animateParticles() {
    t += 0.01;
    const index = Math.floor(t * numPoints) % points.length;
    const position = points[index];
    particle.position.set(position.x, position.y, position.z);
    requestAnimationFrame(animateParticles);
  }
  animateParticles();
}

function plotDoubleHelixEdge(sourceMesh, targetMesh, color, twists = 3) {
  const points = [];
  const numPoints = 100;
  const sourcePos = sourceMesh.position;
  const targetPos = targetMesh.position;

  for (let i = 0; i <= numPoints; i++) {
    const t = i / numPoints;
    const x = THREE.MathUtils.lerp(sourcePos.x, targetPos.x, t);
    const y = THREE.MathUtils.lerp(sourcePos.y, targetPos.y, t) + Math.sin(twists * Math.PI * t) * 0.5; // Twist effect
    const z = THREE.MathUtils.lerp(sourcePos.z, targetPos.z, t) + Math.cos(twists * Math.PI * t) * 0.5; // Opposing twist
    points.push(new THREE.Vector3(x, y, z));
  }

  const curve = new THREE.CatmullRomCurve3(points);
  const geometry = new THREE.TubeGeometry(curve, 64, 0.05, 8, false);
  const material = new THREE.MeshBasicMaterial({ color });
  scene.add(new THREE.Mesh(geometry, material));
}
function plotArrowRibbonEdge(sourceMesh, targetMesh, color) {
  const points = [
    sourceMesh.position.clone(),
    targetMesh.position.clone(),
  ];
  const geometry = new THREE.BufferGeometry().setFromPoints(points);

  // Ribbon material
  const material = new THREE.MeshBasicMaterial({
    color: color,
    transparent: true,
    opacity: 0.8,
  });

  // Arrow direction
  const arrowDirection = targetMesh.position.clone().sub(sourceMesh.position).normalize();
  const arrowHelper = new THREE.ArrowHelper(
    arrowDirection,
    sourceMesh.position,
    sourceMesh.position.distanceTo(targetMesh.position),
    color,
    0.5, // Arrowhead length
    0.3  // Arrowhead width
  );

  scene.add(new THREE.Line(geometry, material));
  scene.add(arrowHelper);
}
function plotZigzagEdge(sourceMesh, targetMesh, color, levels = 2) {
  const points = [];
  const sourcePos = sourceMesh.position;
  const targetPos = targetMesh.position;
  const segments = 10;

  for (let i = 0; i <= segments; i++) {
    const t = i / segments;
    const x = THREE.MathUtils.lerp(sourcePos.x, targetPos.x, t);
    const y = sourcePos.y + (i % 2 === 0 ? levels : -levels) * 0.5; // Alternating up and down
    const z = THREE.MathUtils.lerp(sourcePos.z, targetPos.z, t);
    points.push(new THREE.Vector3(x, y, z));
  }

  const geometry = new THREE.BufferGeometry().setFromPoints(points);
  const material = new THREE.LineBasicMaterial({ color });
  scene.add(new THREE.Line(geometry, material));
}

// Core Edge Drawing Helpers
function plotSineWaveEdge(sourceMesh, targetMesh, color, amplitude = 1.5) {
  const points = [];
  const numPoints = 50;
  const sourcePos = sourceMesh.position;
  const targetPos = targetMesh.position;

  for (let t = 0; t <= 1; t += 1 / numPoints) {
    const x = THREE.MathUtils.lerp(sourcePos.x, targetPos.x, t);
    const y = THREE.MathUtils.lerp(sourcePos.y, targetPos.y, t) + amplitude * Math.sin(2 * Math.PI * t);
    const z = sourcePos.z; // Fix z at the source's z-position
    points.push(new THREE.Vector3(x, y, z));
  }

  const curve = new THREE.CatmullRomCurve3(points);
  const geometry = new THREE.TubeGeometry(curve, 64, 0.05, 8, false);
  const material = new THREE.MeshBasicMaterial({ color });
  scene.add(new THREE.Mesh(geometry, material));
}

function plotQuadraticBezierEdge(sourceMesh, targetMesh, color, offset = 2) {
  const sourcePos = sourceMesh.position;
  const targetPos = targetMesh.position;

  // Calculate the control point in the middle, offset along Y-axis
  const controlPoint = new THREE.Vector3(
    (sourcePos.x + targetPos.x) / 2,    // Midpoint X
    (sourcePos.y + targetPos.y) / 2 + offset, // Offset upward in Y
    sourcePos.z // Keep Z fixed
  );

  // Create a Quadratic Bézier Curve on the X-Y plane
  const curve = new THREE.QuadraticBezierCurve3(
    new THREE.Vector3(sourcePos.x, sourcePos.y, sourcePos.z), // Start point
    controlPoint, // Control point
    new THREE.Vector3(targetPos.x, targetPos.y, targetPos.z)  // End point
  );

  // Generate points for the curve
  const points = curve.getPoints(50);

  // Create geometry and material for the curve
  const geometry = new THREE.BufferGeometry().setFromPoints(points);
  const material = new THREE.LineBasicMaterial({ color: color, linewidth: 2 });

  // Create a line object and add it to the scene
  const bezierLine = new THREE.Line(geometry, material);
  scene.add(bezierLine);
}

function plotThickGlowingLine(sourceMesh, targetMesh, color = 0x9400D3, lineWidth = 0.1) {
  const points = [
    sourceMesh.position.clone(),
    targetMesh.position.clone(),
  ];

  // Geometry for the straight line
  const geometry = new THREE.BufferGeometry().setFromPoints(points);

  // Material with glowing effect (emissive and bright purple)
  const material = new THREE.MeshBasicMaterial({
    color: color, // Purple color
    transparent: true,
    opacity: 0.9, // Slight transparency
    emissive: color, // Emissive for glowing effect
    emissiveIntensity: 0.8, // Adjust glow strength
  });

  // Create a tube geometry for thickness
  const curve = new THREE.LineCurve3(points[0], points[1]);
  const tubeGeometry = new THREE.TubeGeometry(curve, 20, lineWidth, 8, false);

  const lineMesh = new THREE.Mesh(tubeGeometry, material);
  scene.add(lineMesh);
}

function plotFamilyEdge(sourceMesh, targetMesh) {
  plotThickGlowingLine(sourceMesh, targetMesh);
}


function plotJaggedEdge(sourceMesh, targetMesh, color) {
  const points = [];
  const segments = 20;
  const sourcePos = sourceMesh.position;
  const targetPos = targetMesh.position;

  for (let i = 0; i <= segments; i++) {
    const t = i / segments;
    const x = THREE.MathUtils.lerp(sourcePos.x, targetPos.x, t);
    const y = sourcePos.y + (i % 2 === 0 ? 0.2 : -0.2);
    const z = THREE.MathUtils.lerp(sourcePos.z, targetPos.z, t);
    points.push(new THREE.Vector3(x, y, z));
  }

  const geometry = new THREE.BufferGeometry().setFromPoints(points);
  const material = new THREE.LineBasicMaterial({ color });
  scene.add(new THREE.Line(geometry, material));
}

function plotStraightLine(sourceMesh, targetMesh, color) {
  const points = [
    sourceMesh.position.clone(),
    targetMesh.position.clone(),
  ];
  const geometry = new THREE.BufferGeometry().setFromPoints(points);
  const material = new THREE.LineBasicMaterial({ color });
  scene.add(new THREE.Line(geometry, material));
}

function plotDashedLine(sourceMesh, targetMesh, color) {
  const points = [
    sourceMesh.position.clone(),
    targetMesh.position.clone(),
  ];
  const geometry = new THREE.BufferGeometry().setFromPoints(points);
  const material = new THREE.LineDashedMaterial({ color, dashSize: 0.5, gapSize: 0.2 });
  const line = new THREE.Line(geometry, material);
  line.computeLineDistances();
  scene.add(line);
}





////////////////////////////////////////
// 
//////////////////////////////////////
////////////////////////////////////// 
const EDGE_OFFSET = 0.2; // Constant for offset spacing
const plottedEdges = new Map(); // Map to track edges and prevent overlap

function plotEdgeWithOffset(sourceMesh, targetMesh, emotions) {
  emotions.forEach((weight, index) => {
    if (weight > 0 && EDGE_PLOT_FUNCTIONS[index]) {
      const edgeKey = `${sourceMesh.name}-${targetMesh.name}-${index}`;
      const reverseKey = `${targetMesh.name}-${sourceMesh.name}-${index}`;

      // Check for duplicate edges
      const existingCount = plottedEdges.get(edgeKey) || 0;
      plottedEdges.set(edgeKey, existingCount + 1);

      const offset = existingCount * EDGE_OFFSET; // Apply offset per duplicate edge

      // Adjust positions with offset
      const sourcePos = sourceMesh.position.clone();
      const targetPos = targetMesh.position.clone();

      // Offset positions slightly in X and Y
      sourcePos.x += existingCount % 2 === 0 ? offset : -offset; // Alternate direction
      targetPos.x += existingCount % 2 === 0 ? offset : -offset;

      sourcePos.y += existingCount % 2 === 1 ? offset : -offset; // Alternate direction
      targetPos.y += existingCount % 2 === 1 ? offset : -offset;

      // Call the appropriate plot function
      EDGE_PLOT_FUNCTIONS[index].plot(
        { position: sourcePos },
        { position: targetPos },
        EDGE_PLOT_FUNCTIONS[index].color
      );
    }
  });
}



////////////////////////////////////////////////////////////////////////////
////////////////////////////////////// 
////////////////////////////////////// //////////////////////////////////////
////////////////////////////////////// 
// Function to dynamically create the chapter navigation bar
function createChapterNav(totalChapters) {
  const nav = document.getElementById("chapter-nav");
  nav.innerHTML = ""; // Clear existing chapter squares

  for (let i = 0; i < totalChapters; i++) {
    const square = document.createElement("div");
    square.classList.add("chapter-square");
    square.dataset.chapter = i; // Store chapter index
    square.textContent = i + 1; // Display chapter number

    // Event listener to move the camera to the corresponding Z-level
    square.addEventListener("click", () => {
      moveCameraToChapter(i);
    });

    nav.appendChild(square);
  }
}

// Function to smoothly move the camera to a chapter's Z-level
const CAMERA_DISTANCE = 10; // Distance along Z-axis to view the chapter
const CAMERA_HEIGHT = 5;    // Height adjustment to match node positions

// Function to smoothly move and angle the camera to focus on the selected chapter plane
function moveCameraToChapter(chapterIndex) {
  const yLevel = chapterIndex * 10; // Each chapter is spaced by 10 units on the Y-axis

  if (yLevel !== undefined) {
    const cameraDistance = 20; // Distance away to get a clear view
    const cameraHeight = yLevel + 10; // Raise the camera slightly above the plane

    // Set the camera's position
    camera.position.set(15, cameraHeight, cameraDistance); // Shift on X, go up in Y, and keep Z at distance
    camera.lookAt(0, yLevel, 0); // Look at the center of the chapter plane

    console.log(`Camera moved to chapter ${chapterIndex} at Y-level: ${yLevel}`);
  } else {
    console.error("Invalid chapter index or Z-level missing.");
  }
}


const chapterLevels = []; // Holds Z-levels for each chapter

function updateChapterLevels(book) {
  chapterLevels.length = 0; // Reset previous levels
  Object.keys(book.layers).forEach((layerNumber) => {
    const zLevel = parseInt(layerNumber) * 10; // Adjust Z-level spacing, e.g., every 10 units
    chapterLevels.push(zLevel);
  });
}



// Master function to load and plot nodes for the book
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

    clearScene(); // Clear existing nodes
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

    // Update chapter navigation bar
    const totalChapters = Object.keys(currentBook.layers).length;
    createChapterNav(totalChapters);

  } catch (error) {
    console.error("Error loading or parsing JSON:", error);
  }
}

// Modified function to load a selected book
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





//////////////////////////////////////
////////////////////////////////////// //////////////////////////////////////
////////////////////////////////////// 


// Master Function to Initialize Edge Plotting
function plotAllEdges() {
  if (currentBook) {
    plotAllEdgesFromBook(currentBook);
  } else {
    console.error("No book data loaded to plot edges.");
  }
}






// Master function to initialize everything
// Master function to initialize everything
function make_scene(jsonFile) {
  setScene();
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
  
  while (scene.children.length > 0) {
    scene.remove(scene.children[0]);
  }
  setGridHelper(); // Re-add grid helper
}


// Function to clear previous data or scene

// Initialize dropdown and attach event listeners
// Initialize dropdown and attach event listeners
document.addEventListener("DOMContentLoaded", () => {
  populateLibraryDropdown(); // Populate the dropdown menu

  const loadButton = document.getElementById("load-book");
  loadButton.addEventListener("click", () => {
    loadSelectedBook();
  });

  // Scrollbar event listener
  const scrollBar = document.getElementById("chapter-scrollbar");
  if (scrollBar) {
    scrollBar.addEventListener("input", (e) => {
      const targetChapterIndex = parseInt(e.target.value, 10);
      moveCameraToChapter(targetChapterIndex);
    });
  }

  make_scene("./book_json_files/Alice's_Adventures_in_Wonderland.json");
});
