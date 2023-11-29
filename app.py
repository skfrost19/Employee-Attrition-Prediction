from flask import Flask, request, jsonify
from flask import render_template
from src.components.predict import predict
import json

# from src.components.pipeline import pipeline


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("form.html")


@app.route("/predict", methods=["POST"])
def predict_route():
    data = request.get_json(force=True)
    prediction = predict(data)
    return jsonify(prediction)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
