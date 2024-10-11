from flask import Flask, request, render_template, jsonify
import os
import numpy as np
import tensorflow as tf
import mysql.connector
import base64
from tensorflow.keras.models import load_model
from PIL import Image

app = Flask(__name__)

# Load the trained model
model = load_model('my_model.keras')
class_labels = [
    'acne',
    'alopecia',
    'athlete foot',
    'cellulitis',
    'chickenpox',
    'cutaneous larva migrans',
    'impetigo',
    'nail fungus',
    'ringworm',
    'shingles',
    'urticaria',
    'vitiligo'
]

def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((299, 299))  # Resize to match input size of the model
    img = np.array(img) / 255.0   # Normalize pixel values
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

def classify_image(image_path):
    img = preprocess_image(image_path)
    predictions = model.predict(img)
    predicted_class = np.argmax(predictions)
    confidence_score = np.max(predictions) * 100  # Get the confidence score as a percentage
    disease_name = class_labels[predicted_class]
    return disease_name, confidence_score

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/acne')
def acne():
    return render_template('acne.html')

@app.route('/alopecia')
def alopecia():
    return render_template('alopecia.html')

@app.route('/athlete_foot')
def athlete_foot():
    return render_template('athlete_foot.html')

@app.route('/cellulitis')
def cellulitis():
    return render_template('cellulitis.html')

@app.route('/chickenpox')
def chickenpox():
    return render_template('chickenpox.html')

@app.route('/cutaneous_larva_migrans')
def cutaneous_larva_migrans():
    return render_template('cutaneous_larva_migrans.html')

@app.route('/impetigo')
def impetigo():
    return render_template('impetigo.html')

@app.route('/nail_fungus')
def nail_fungus():
    return render_template('nail_fungus.html')

@app.route('/ringworm')
def ringworm():
    return render_template('ringworm.html')

@app.route('/shingles')
def shingles():
    return render_template('shingles.html')

@app.route('/urticaria')
def urticaria():
    return render_template('urticaria.html')

@app.route('/vitiligo')
def vitiligo():
    return render_template('vitiligo.html')



@app.route('/upload')
def upload_image():
    return render_template('upload.html')


@app.route('/classify', methods=['POST'])
def classify_uploaded_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    image_file = request.files['image']
    image_path = 'uploads/' + image_file.filename
    image_file.save(image_path)
    disease_name, confidence_score = classify_image(image_path)
    
    def get_disease_info(disease_name):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cutiscan"
        )
        
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM disease WHERE diseaseName = %s"
        cursor.execute(query, (disease_name,))
        disease_info = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if disease_info and disease_info['image']:
            disease_info['image'] = base64.b64encode(disease_info['image']).decode('utf-8')
        
        return disease_info
    
    disease_info = get_disease_info(disease_name)
    return render_template('result.html', disease=disease_info, confidence=confidence_score)

@app.route('/crop', methods=['POST'])
def upload_and_crop_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    image_file = request.files['image']
    img_data = image_file.read()
    return render_template('crop.html', img_data=base64.b64encode(img_data).decode())

@app.route('/classify_cropped', methods=['POST'])
def classify_cropped_image():
    img_data = request.form['croppedImage']
    img_path = 'uploads/cropped_image.png'
    with open(img_path, 'wb') as img_file:
        img_file.write(base64.b64decode(img_data.split(',')[1]))
    disease_name, confidence_score = classify_image(img_path)
    
    def get_disease_info(disease_name):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cutiscan"
        )
        
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM disease WHERE diseaseName = %s"
        cursor.execute(query, (disease_name,))
        disease_info = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if disease_info and disease_info['image']:
            disease_info['image'] = base64.b64encode(disease_info['image']).decode('utf-8')
        
        return disease_info
    
    disease_info = get_disease_info(disease_name)
    return render_template('result.html', disease=disease_info, confidence=confidence_score)

if __name__ == '__main__':
    app.run(debug=True)


"""
# For hosting on ngrok
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
"""


