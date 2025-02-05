import os
import shutil
import cv2
import numpy as np
from sklearn.cluster import KMeans

# Define paths
dataset_path = "/home/sandy0810/Documents/Banana_Turmeric/Turmeric_augmented"  # Update this path
output_path_A = os.path.join(dataset_path, "Class_A")
output_path_B = os.path.join(dataset_path, "Class_B")

# Create folders if not exist
os.makedirs(output_path_A, exist_ok=True)
os.makedirs(output_path_B, exist_ok=True)

# Read images and extract features
image_features = []
image_paths = []
for img_name in os.listdir(dataset_path):
    if img_name.endswith(".jpg"):
        img_path = os.path.join(dataset_path, img_name)
        image = cv2.imread(img_path)
        image = cv2.resize(image, (100, 100))  # Resize for consistency

        # Convert to HSV and extract mean color values
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mean_hue = np.mean(hsv[:, :, 0])  # Hue value
        mean_saturation = np.mean(hsv[:, :, 1])  # Saturation
        mean_value = np.mean(hsv[:, :, 2])  # Brightness

        image_features.append([mean_hue, mean_saturation, mean_value])
        image_paths.append(img_path)

# Apply KMeans clustering (2 clusters for Class A & B)
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
labels = kmeans.fit_predict(image_features)

# Move images based on clustering
for i, img_path in enumerate(image_paths):
    if labels[i] == 0:
        shutil.move(img_path, os.path.join(output_path_A, os.path.basename(img_path)))
    else:
        shutil.move(img_path, os.path.join(output_path_B, os.path.basename(img_path)))

print("Turmeric images sorted into Class A and Class B.")
