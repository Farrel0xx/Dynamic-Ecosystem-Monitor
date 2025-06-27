# 🚀 Dynamic Ecosystem Monitor Offline

## Overview
This is an offline environmental monitoring application built for the "Google - The Gemma 3n Impact Challenge" on Kaggle. It leverages the Gemma 3n model to process multimodal data (images, audio, and vibration) to detect plant health, environmental sounds, and seismic activity, providing real-time alerts and risk visualizations. Designed for remote areas, it supports sustainability and crisis response with privacy-first, on-device performance.

## Features
✔ **Image Processing**: Detects plant health using OpenCV, calculating a health score based on green pixel intensity.
✔ **Audio Analysis**: Records and analyzes ambient sounds (e.g., rain, wildlife) for ecological insights.
✔ **Vibration Detection**: Simulates seismic data to predict disaster risks (to be enhanced with real sensors).
✔ **Risk Visualization**: Displays a basic risk map combining all inputs.
✔ **Offline Ready**: Optimized for low-resource devices using Gemma 3n's submodel 2B.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Farrel0xx/Dynamic-Ecosystem-Monitor.git
   cd Dynamic-Ecosystem-Monitor
   ```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure a plant.jpg image is in the project directory for initial testing.

## Usage
Run the script:
```bash
python main.py
```
✔ The app will process an image, record audio, simulate vibration, and display a risk map.
✔ Test offline to verify performance on your device.

## Future Improvements
✔ Integrate real vibration sensor data from mobile devices.
✔ Fine-tune Gemma 3n for specific classifications using Unsloth.
✔ Add multilingual voice alerts with text-to-speech.

## Contributing
Feel free to fork this repository, submit issues, or pull requests to enhance the project!
