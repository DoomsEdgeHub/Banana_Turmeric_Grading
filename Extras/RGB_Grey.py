import cv2
import os

# Input and Output folder paths
input_folder = "/home/sandy0810/Documents/Banana_Turmeric/stale_banana"
output_folder = "/home/sandy0810/Documents/Banana_Turmeric/Banana/Class B"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process all images in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith((".png", ".jpg", ".jpeg")):  # Check image formats
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)  # Read the image
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        output_path = os.path.join(output_folder, filename)  # Save path
        cv2.imwrite(output_path, gray_img)  # Save grayscale image
        print(f"Converted: {filename}")

print("Batch conversion completed!")
