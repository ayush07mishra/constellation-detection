# Star Constellation Detection

This project uses **machine learning** to identify constellations from images of stars. The system takes an image containing stars as input and predicts which constellation is formed by those stars.

## Features
- **Image Input**: Upload an image containing stars or a constellation.
- **Prediction**: The model identifies and classifies the constellation in the image.
- **Interactive Frontend**: An easy-to-use web interface for users to upload images and get real-time predictions.

<img width="1470" alt="Screenshot 2024-11-15 at 11 12 57 AM" src="https://github.com/user-attachments/assets/8e9d592b-605c-4f39-9cd9-7dd27de7552a">
<img width="1470" alt="Screenshot 2024-11-15 at 11 12 51 AM" src="https://github.com/user-attachments/assets/9544659c-9a7a-4d5f-9bbe-f21196ee6897">
<img width="1470" alt="Screenshot 2024-11-15 at 11 13 13 AM" src="https://github.com/user-attachments/assets/fe461f4b-d17e-4c30-bcf7-04c1ea488e0d">
<img width="1470" alt="Screenshot 2024-11-15 at 11 13 59 AM" src="https://github.com/user-attachments/assets/ce9daa1f-3c3c-4909-aacd-840488d1636a">
<img width="1470" alt="Screenshot 2024-11-15 at 11 15 44 AM" src="https://github.com/user-attachments/assets/cff6a06a-99d7-46c4-a38f-f5566ca109ed">

## Technologies Used
- **Python**: Core programming language.
- **TensorFlow/Keras**: For training the machine learning model.
- **OpenCV**: For image processing.
- **Streamlit**: For creating the web interface.

- **NumPy & Matplotlib**: For data manipulation and visualization.
- **Flask/Django** (Optional): For backend API.

## Installation Instructions

### Prerequisites
Ensure you have Python 3.6+ installed on your system.


## Model
The model is a Convolutional Neural Network (CNN) trained on a dataset of star patterns. It can classify multiple constellations and works by recognizing patterns in the star coordinates.

## Dataset
The dataset consists of images of stars with labeled constellations. It includes images with varying star patterns and background noise to improve model robustness.












### 1. Clone the Repository
```bash
git clone https://github.com/ayush07mishra/constellation-detection.git
cd constellation-detection
