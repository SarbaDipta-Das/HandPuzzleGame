Live AR Puzzle Game
Live AR Puzzle Game is an interactive augmented reality experience that transforms your live webcam feed into a 3x3 sliding puzzle. Using real-time computer vision, the system tracks your hand movements, allowing you to manipulate and solve the puzzle through simple gestures without the need for a mouse or keyboard.
Features
Real-Time AR Slicing
Captures live video feed and turns it into a dynamic 3x3 interactive grid.
Gesture-Based Interaction
Start Gesture: Simply show your open palm to the camera to trigger the puzzle start.
Selection & Swapping: Use a 2-second "hover-to-select" gesture to pick pieces.
Visual Feedback: Includes a progress bar and highlight colors to track selection status.
Dynamic Difficulty
Automatically shuffles the image pieces upon starting the puzzle.
Detects completion and displays a victory message.
Optimized Performance
High-resolution (720p) camera integration.
Low-latency processing using OpenCV and MediaPipe.
Project Structure
code
Text
HandPuzzleGame/
│
├── venv/                 # Virtual environment
├── puzzle_logic.py       # Main game engine and CV logic
└── README.md             # Project documentation
Tech Stack
Language: Python 3.x
Computer Vision: OpenCV (cv2)
AI/Hand Tracking: MediaPipe
Data Processing: NumPy
Current Development Status

Real-time video processing.

Hand tracking and gesture recognition.

Image slicing and grid generation.

Hold-to-swap logic.

Victory state detection.
Installation
1. Clone Repository
code
Bash
git clone https://github.com/yourusername/HandPuzzleGame.git
cd HandPuzzleGame
2. Set up Virtual Environment
code
Bash
# Create environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate
3. Install Dependencies
code
Bash
pip install opencv-python mediapipe numpy
4. Run the Game
code
Bash
python puzzle_logic.py
Future Enhancements
Timed Mode: Adding a countdown timer to challenge players.
Variable Grid Sizes: Allowing users to switch between 3x3, 4x4, and 5x5 grids.
Custom Image Support: Ability to upload an image from your computer as the puzzle background.
Advanced Gestures: Implementing "Pinch-to-drag" for more fluid movement.
Save/Load: Tracking high scores and fastest completion times.
Disclaimer
This project is an experimental computer vision application. Ensure you have adequate lighting in your room for the MediaPipe hand tracking to function optimally.
Author
[Sarbadipta Das]
