from flask import Flask, request, jsonify, send_from_directory
import cv2
import numpy as np
import tensorflow as tf
# Load your CNN model
model = tf.keras.models.load_model('constellation_model.h5')
# Define constellation labels that the model recognise
constellation_labels = [
    'andromeda', 'antares', 'aquarius', 'aquila', 'aries', 'auriga', 'boötes',
    'caelum', 'camelopardalis', 'cancer', 'canes_venatici', 'canis_major',
    'canis_minor', 'capricornus', 'carina', 'cassiopeia', 'centaurus', 'cepheus',
    'cetus', 'chamaeleon', 'circinus', 'columba', 'comae_berenices', 'corona_australis',
    'corona_borealis', 'corvus', 'crater', 'crux', 'cygnus', 'delphinus', 'dorado',
    'draco', 'equuleus', 'eridanus', 'fornax', 'gemini', 'grus', 'hercules',
    'horologium', 'hydra', 'hydrus', 'indus', 'lacerta', 'leo', 'leo_minor', 
    'lepus', 'libra', 'lupus', 'lynx', 'lyra', 'mensa', 'microscopium', 'monoceros', 
    'musca', 'norma', 'octans', 'ophiuchus', 'orion', 'pavo', 'pegasus', 'perseus', 
    'phoenix', 'pictor', 'pisces', 'pisces_austrinus', 'puppis', 'pyxis', 'reticulum', 
    'sagitta', 'sagittarius', 'scorpius', 'sculptor', 'scutum', 'serpens', 'sextans', 
    'taurus', 'telescopium', 'triangulum', 'triangulum_australe', 'tucana', 
    'ursa_major', 'ursa_minor', 'vela', 'virgo', 'volans', 'vulpecula'
]
  # Replace with actual constellation names
def decode_prediction(prediction):
    max_index = np.argmax(prediction)
    constellation_name = constellation_labels[max_index]
    return constellation_name
app = Flask(__name__)

@app.route('/')
def serve_frontend():
    return send_from_directory('/Users/ayushmishra/Desktop/Constellation_proj/templates/stars2.html', 'stars2.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['image']
    img = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (180, 180))  # Resize as per your model requirements
    img = np.expand_dims(img, axis=0) / 255.0  # Preprocessing for the model

    # Prediction
    prediction = model.predict(img)
    constellation = decode_prediction(prediction)

    return jsonify({"constellation": constellation})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
