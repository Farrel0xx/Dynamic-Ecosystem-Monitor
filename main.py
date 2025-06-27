import cv2
import numpy as np
import librosa
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Image Processing: Detect plant health
def process_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return None
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    # Simple health indicator: Count green pixels in original image
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_green = np.array([35, 100, 100])
    upper_green = np.array([85, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    health_score = np.sum(mask) / 255 / (img.shape[0] * img.shape[1]) * 100
    return thresh, health_score

# Audio Processing: Analyze environmental sounds
def process_audio(duration=5):
    fs = 44100
    print("Recording audio for", duration, "seconds...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    audio_data = audio_data.flatten()
    # Simple feature: Detect loudness (potential rain or wildlife)
    loudness = np.mean(np.abs(audio_data))
    return audio_data, loudness

# Vibration Detection: Simulate seismic data
def simulate_vibration(duration=5):
    fs = 100  # Sampling rate for vibration
    t = np.linspace(0, duration, int(duration * fs))
    # Simulate random vibration (replace with real sensor data later)
    vibration = np.sin(2 * np.pi * 1 * t) + np.random.normal(0, 0.1, len(t))
    intensity = np.max(np.abs(vibration))
    return vibration, intensity

# Visualization: Basic map with risk zones
def plot_map(health_score, loudness, intensity):
    fig, ax = plt.subplots()
    # Simulate risk zones based on inputs
    risk = 100 - health_score + (loudness * 100) + (intensity * 1000)
    colors = ['green' if risk < 150 else 'yellow' if risk < 300 else 'red']
    ax.imshow([[1]], cmap='RdYlGn_r', vmin=0, vmax=300)
    ax.set_title(f"Risk Level: {risk:.1f}")
    plt.show()

# Main execution
if __name__ == "__main__":
    # Process image
    thresh, health_score = process_image('tanaman.jpg')
    if thresh is not None:
        cv2.imshow('Plant Health Detection', thresh)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(f"Plant Health Score: {health_score:.1f}%")

    # Process audio
    audio_data, loudness = process_audio()
    print(f"Audio Loudness: {loudness:.2f}")

    # Process vibration
    vibration, intensity = simulate_vibration()
    print(f"Vibration Intensity: {intensity:.2f}")

    # Visualize risk map
    plot_map(health_score, loudness, intensity)
    print("Go, check your first ecosystem update, cok!")
