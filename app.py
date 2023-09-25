import os

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin

from chicken_disease_classification.utils.common import decode_image
from chicken_disease_classification.pipeline.prediction_pipeline import (
    PredictionPipeline,
)

os.putenv("LANG", "en_US.UTF-8")
os.putenv("LC_ALL", "en_US.UTF-8")

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.file_name = "input_image.jpg"
        self.classifier = PredictionPipeline(self.file_name)


@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/train", methods=["GET", "POST"])
@cross_origin()
def train():
    os.system("python main.py")

    return "Training executed successfully"


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    image = request.json["image"]
    decode_image(image, client_app.file_name)
    result = client_app.classifier.predict()

    return jsonify(result)


if __name__ == "__main__":
    client_app = ClientApp()
    app.run(host="0.0.0.0", port=8080)  # local host
    app.run(host="0.0.0.0", port=8080)  # AWS
    app.run(host="0.0.0.0", port=80)  # Azure
