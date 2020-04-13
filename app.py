import os

import json
import requests
from flask import Flask, request, jsonify, render_template

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

import base64
import PIL
from io import BytesIO
from PIL import Image

# init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
model_name = 'model7.h5'
model_path = os.path.join(basedir, 'models/' + model_name)

# model, image size
model = load_model(model_path)
width = 256
height = 256

labels = ['cat',
          'chicken',
          'cow',
          'dog',
          'horse',
          'sheep',
          'squirrel']

# giphy, usage: api_key=key&tag=predicted
giphy_rand = 'http://api.giphy.com/v1/gifs/random?'
API_KEY = "api_key=kRB7K4jq5sFKgZZLqAOPnIfKKlzeTm7c"


# for website upload
@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_image():
    img = request.files['image']
    # img_string = base64.b64encode(image.read())
    img = PIL.Image.open(img)
    img = img.resize((height, width))
    img = image.img_to_array(img)
    img = img / 255  # must divide the RBG val 255 to rescale to 0~1
    img = np.expand_dims(img, axis=0)
    # do image classification here
    animal_class = model.predict_classes(img).tolist()
    animal = labels[animal_class[0]]

    # get random gif url from giphy base on animal predicted then return the url
    # JSON parse reference: https://stackoverflow.com/a/32202832
    giphy_url = giphy_rand + API_KEY + '&tag=' + animal
    dict = json.loads(requests.get(giphy_url).text)
    gif_url = dict['data']['image_url']
    print(gif_url)
    return render_template('complete.html', animal=animal, gif_url=gif_url)


# predict
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        b64_string = request.form.get('image')
        img = PIL.Image.open(BytesIO(base64.b64decode(b64_string))).convert('RGB')
        img = img.resize((height, width))
        img = image.img_to_array(img)
        img = img / 255  # must divide the RBG val 255 to rescale to 0~1
        img = np.expand_dims(img, axis=0)
        # do image classification here
        animal_class = model.predict_classes(img).tolist()
        animal = labels[animal_class[0]]

        # get random gif url from giphy base on animal predicted then return the url
        # JSON parse reference: https://stackoverflow.com/a/32202832
        giphy_url = giphy_rand + API_KEY + '&tag=' + animal
        dict = json.loads(requests.get(giphy_url).text)
        gif_url = dict['data']['image_url']
        print(gif_url)
        return jsonify({"animal": animal, "gif_url": gif_url})


# Run Server
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
