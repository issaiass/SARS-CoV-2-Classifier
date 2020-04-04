from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications import imagenet_utils
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import flask
import io
import tensorflow as tf
from flask import render_template


# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
model = None


def loadmodel():
    # load the pre-trained Keras model (here we are using a model
    # pre-trained on ImageNet and provided by Keras, but you can
    # substitute in your own networks just as easily)
    global model

    model = load_model('./model/model.h5')


def prepare_image(image, target):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    # return the processed image
    return image


@app.route("/")
def render_static():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the
    # view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            # read the image in PIL format
            image = flask.request.files["image"].read()
            image = Image.open(io.BytesIO(image))

            # preprocess the image and prepare it for classification
            image = prepare_image(image, target=(299, 299))

            # classify the input image and then initialize the list
            # of predictions to return to the client
            preds = model.predict(image)
            data["predictions"] = []
            # loop over the results and add them to the list of
            # returned predictions
            for normal, covid in preds:
                r = {"normal": float(normal), "covid": float(covid)}
                data["predictions"].append(r)
            # indicate that the request was a success
            data["success"] = True

    # return the data dictionary as a JSON response
    return flask.jsonify(data)



# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    print(("[INFO] - Loading Keras model and Flask starting server... please wait!"))
    loadmodel()
    print(("[INFO] - Model Loades"))
    app.run(host='0.0.0.0')