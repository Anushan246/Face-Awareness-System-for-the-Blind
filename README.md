
# Face Awareness System for the Blind

## Overview

The Face Awareness System for the Blind leverages computer vision and text-to-speech technologies to enhance the independence and spatial awareness of visually impaired individuals. The system performs real-time face detection and provides audio feedback regarding the number of faces detected in the environment. Users can also register their credentials and use voice input for a more accessible experience.

## Features

- **Face Detection:** Uses OpenCV's Haar Cascade Classifier to detect faces in real-time.
- **Text-to-Speech:** Provides audio feedback using the pyttsx3 library.
- **Voice Input:** Allows users to register their username and password through voice commands.
- **User Interface:** Provides a graphical user interface (GUI) using Tkinter for registration and interaction.

## Requirements

- Python 3.x
- OpenCV
- pyttsx3
- SpeechRecognition (for voice input functionality)
- Tkinter (usually included with Python)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies:**

   Ensure you have Python 3.x installed. Then, install the required packages using pip:

   ```bash
   pip install opencv-python pyttsx3 SpeechRecognition
   ```

3. **Download Haar Cascade XML:**

   The Haar Cascade XML file is used for face detection. It should be automatically included with OpenCV. If not, you can manually download it from [here](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml).

## Usage

1. **Run the Application:**

   To start the application, run the following command:

   ```bash
   python <script-name>.py
   ```

   Replace `<script-name>` with the name of your Python script (e.g., `face_awareness.py`).

2. **Register:**

   - The application will prompt you to register by entering a username and password.
   - You can use either keyboard input or voice input for registration.
   - Press "Register" to complete the registration process.

3. **Face Detection:**

   - After registration, the system will start face detection.
   - It will provide real-time audio feedback about the number of faces detected.
   - Press 'Q' to exit the face detection mode.

## How It Works

- **Registration:** Users can input their credentials via keyboard or voice. The credentials are stored for reference.
- **Face Detection:** The system captures video from the webcam, processes each frame to detect faces, and provides audio feedback about the detection results.
- **Voice Feedback:** The text-to-speech engine reads out prompts and detection results to the user.

## Troubleshooting

- **No Faces Detected:** Ensure the webcam is functioning properly and there is sufficient lighting.
- **Voice Input Issues:** Make sure your microphone is connected and working. Adjust the microphone sensitivity if necessary.


## Acknowledgments

- **OpenCV:** For providing the computer vision library.
- **pyttsx3:** For text-to-speech functionality.
- **SpeechRecognition:** For enabling voice input capabilities.
- **Tkinter:** For the graphical user interface.
