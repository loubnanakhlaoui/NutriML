from flask import Flask, request, render_template
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import Image
import numpy as np
import requests
import json
import io

app = Flask(__name__)

# Charger le modèle
model = tf.keras.models.load_model('model/NutritML.h5')

# Dictionnaire des classes
labels = {
    0: 'apple',
    1: 'banana',
    2: 'beetroot',
    3: 'bell pepper',
    4: 'cabbage',
    5: 'capsicum',
    6: 'carrot',
    7: 'cauliflower',
    8: 'chilli pepper',
    9: 'corn',
    10: 'cucumber',
    11: 'eggplant',
    12: 'garlic',
    13: 'ginger',
    14: 'grapes',
    15: 'jalepeno',
    16: 'kiwi',
    17: 'lemon',
    18: 'lettuce',
    19: 'mango',
    20: 'onion',
    21: 'orange',
    22: 'paprika',
    23: 'pear',
    24: 'peas',
    25: 'pineapple',
    26: 'pomegranate',
    27: 'potato',
    28: 'raddish',
    29: 'soy beans',
    30: 'spinach',
    31: 'sweetcorn',
    32: 'sweetpotato',
    33: 'tomato',
    34: 'turnip',
    35: 'watermelon'
}

def preprocess_image(image):
    image = image.resize((224, 224))
    image = img_to_array(image)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    image = np.expand_dims(image, axis=0)
    return image

def predict_and_get_nutrition_info(image):
    img = preprocess_image(image)
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction, axis=1)[0]
    predicted_label = labels[predicted_class]

    api_url = f'https://api.api-ninjas.com/v1/nutrition?query={predicted_label}'
    response = requests.get(api_url, headers={'X-Api-Key': 'FJCuuMBu83nEaI7CGroR8A==z88oB9CslsPk9p80'})
    if response.status_code == requests.codes.ok:
        nutrition_info = response.json()
        return predicted_label, nutrition_info
    else:
        print("Error:", response.status_code, response.text)
        return predicted_label, None

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            img = Image.open(io.BytesIO(file.read()))
            predicted_label, nutrition_info = predict_and_get_nutrition_info(img)
            return render_template('index.html', fruit=predicted_label, nutrition_info=nutrition_info)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)

    
