from flask import Flask, request, jsonify
from model.model import load_model
import numpy as np


app = Flask(__name__)
model = load_model()


# Root endpoint
@app.route("/")
def home():
    return "Welcome to MLOps Assignment Flask API 🚀"


# Health check endpoint
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "message": "API is up and running ✅"})


# Model version info (can be extended)
@app.route("/version", methods=["GET"])
def version():
    return jsonify({"model_version": "1.0.0"})


# Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    try:
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400

        data = request.json.get("features", None)
        if data is None:
            return jsonify(
                {"error": "Missing 'features' key in request body"}
            ), 400

        features = np.array(data).reshape(1, -1)
        prediction = model.predict(features)

        return jsonify(
            {
                "prediction": int(prediction[0]),
                "input": data,
            }
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
