import os
import numpy as np
import tensorflow as tf
from flask import Flask, render_template, request, jsonify
from tensorflow.keras.preprocessing.image import load_img, img_to_array # type: ignore
import traceback  # Add this at the top of your file

app = Flask(__name__)

# Load trained model
model = tf.keras.models.load_model("banana_turmeric_grading.h5")

# Class Labels (Assuming you used 'Banana_A', 'Banana_B', 'Turmeric_A', 'Turmeric_B')
class_labels = ["Banana_A", "Banana_B", "Turmeric_A", "Turmeric_B"]

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def predict_image(image_path):
    img = load_img(image_path, target_size=(128, 128))  # Resize image
    img_array = img_to_array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Expand dims for CNN

    prediction = model.predict(img_array)  # Predict
    predicted_class = np.argmax(prediction)  # Get class index
    confidence = np.max(prediction) * 100  # Get confidence %

    full_class_name = class_labels[predicted_class]

    # Handle class name format
    if "_" in full_class_name:
        category, grade = full_class_name.split("_")
    else:
        category = full_class_name
        grade = "Unknown"

    return {
        "category": category, 
        "grade": grade, 
        "accuracy": "{:.2f}".format(confidence)  # Convert np.float32 to float
    }


# Home Route
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if "image" not in request.files:
            return jsonify({"error": "No image uploaded!"}), 400

        image = request.files["image"]
        image_path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
        image.save(image_path)

        result = predict_image(image_path)  # Ensure this function works correctly

        print("Prediction Result:", result)  # Debugging
        return jsonify(result)
    except Exception as e:
        print("Error:", e)  # Log error in terminal
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500


       

if __name__ == "__main__":
    app.run(debug=True)
