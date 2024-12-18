// Global Variables
let scene, camera, renderer, controls;

// Function to Initialize the Scene
function setScene() {
    scene = new THREE.Scene();
    console.log("Scene initialized");
}

// Function to Set the Renderer
function setRenderer() {
    renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);
    console.log("Renderer set and added to DOM");
}

// Function to Set the Camera
function setCamera() {
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.set(0, 5, 10); // Position the camera
    console.log("Camera positioned at (0, 5, 10)");
}

// Function to Add a Grid Helper
function setGridHelper() {
    const gridHelper = new THREE.GridHelper(50, 50); // Size: 50x50 divisions
    scene.add(gridHelper);
    console.log("Grid helper added to the scene");
}

// Function to Set the Scene Background
function setBackground(color = 0x000000) {
    scene.background = new THREE.Color(color);
    console.log(`Background color set to ${color.toString(16)}`);
}

// Function to Set Orbit Controls
function setControls() {
    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.update();
    console.log("Orbit controls added to the scene");
}

// Master Function to Set Up the Full Scene
function make_scene() {
    setScene();
    setRenderer();
    setCamera();
    setGridHelper();
    setBackground(0x000000); // Set background to black
    setControls();

    // Add an optional ambient light for visibility
    const light = new THREE.AmbientLight(0xffffff, 0.8);
    scene.add(light);

    console.log("Scene fully initialized");

    // Animation Loop
    function animate() {
        requestAnimationFrame(animate);
        controls.update(); // Required for controls
        renderer.render(scene, camera);
    }
    animate();
}
