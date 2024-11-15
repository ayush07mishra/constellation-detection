# Star Constellation Detection

This project uses **machine learning** to identify constellations from images of stars. The system takes an image containing stars as input and predicts which constellation is formed by those stars.

## Features
- **Image Input**: Upload an image containing stars or a constellation.
- **Prediction**: The model identifies and classifies the constellation in the image.
- **Interactive Frontend**: An easy-to-use web interface for users to upload images and get real-time predictions.


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
