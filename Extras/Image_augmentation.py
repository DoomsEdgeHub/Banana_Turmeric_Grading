import cv2
import os
import albumentations as A
import numpy as np
from albumentations.pytorch import ToTensorV2

# Define paths
input_folder = "/home/sandy0810/Documents/Banana_Turmeric/Turmeric"  # Folder with underrepresented class images
output_folder = "/home/sandy0810/Documents/Banana_Turmeric/Turmeric_augmented/"  # Folder to save augmented images
os.makedirs(output_folder, exist_ok=True)

# Define augmentation pipeline
augmentations = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
    A.Rotate(limit=30, p=0.5),
    A.GaussianBlur(blur_limit=(3, 7), p=0.3),
    A.ElasticTransform(alpha=1, sigma=50, p=0.3),  # Removed 'alpha_affine'
    A.RandomResizedCrop(size=(128,128), scale=(0.5, 1.0), ratio=(0.75, 1.33), p=1.0),  # Fixed syntax
    ToTensorV2()
])

# Number of augmented images per original image
num_augmented = 5  

# Process all images in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(input_folder, filename)
        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        for i in range(num_augmented):
            augmented = augmentations(image=image)['image']
            aug_image = augmented.permute(1, 2, 0).numpy()  # Convert tensor back to image
            aug_image = cv2.cvtColor(aug_image, cv2.COLOR_RGB2BGR)
            
            # Save augmented image
            new_filename = f"{os.path.splitext(filename)[0]}_aug_{i}.jpg"
            output_path = os.path.join(output_folder, new_filename)
            cv2.imwrite(output_path, aug_image)
        
        print(f"Augmented {filename} -> {num_augmented} new images")

print("Data augmentation completed!")








