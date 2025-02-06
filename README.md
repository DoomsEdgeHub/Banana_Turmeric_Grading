# Banana_Turmeric_Grading


## 📌 Project Overview
This project aims to classify and grade Banana & Turmeric using a **Convolutional Neural Network (CNN)**. The model is trained on image data and predicts whether an input image belongs to one of the predefined categories.

### **CNN Model Architecture**
The deep learning model is built using **TensorFlow & Keras** with the following CNN layers:

1. **Conv2D** (32 filters, 3x3 kernel, ReLU activation) + **MaxPooling2D** (2x2)
2. **Conv2D** (64 filters, 3x3 kernel, ReLU activation) + **MaxPooling2D** (2x2)
3. **Conv2D** (128 filters, 3x3 kernel, ReLU activation) + **MaxPooling2D** (2x2)
4. **Flatten** layer to convert the feature maps into a vector
5. **Dense** (128 neurons, ReLU activation) + **Dropout** (0.5)
6. **Output Layer** (Softmax activation for multi-class classification)

## 🚀 Installation Guide
Follow these steps to install and run the project on your system.

### **1️⃣ Prerequisites**
Ensure you have the following installed:
- Python (>=3.8 and <=3.12)
- pip
- Virtual environment (optional but recommended)

### **2️⃣ Clone the Repository**
```sh
git clone https://github.com/your-repo/banana_turmeric_grading.git
cd banana_turmeric_grading
```
### **3️⃣ Dataset**

For the Dataset We collected own images of Banana and Turmeric

**For Grading Banana:** we collected the Fresh (class A) and rotten (class B) images


**For Grading Turmeric:** We Use ***Kmeans Clustering***  to seperate the turmeric.
The code for the KMeans Clusering: ***Extras/seperator.py***

After Collecting the required dataset, We use **Image Augmentation techniques** to increase the datas
In **Image Augmentation:** We Use 
1. **Horizontal Flip** 
2. **RandomBrightnessContrast** 
3. **GaussianBlur** 
4. **ElasticTransform** 

The code for the Image Augmentation: ***Extras/Image_augmentation.py***

Now We need to convert the RGB image to GreyScale Image for the better Classification
The code for the RGB_to_Gray: ***Extras/RGB_Grey.py***


Download the Dataset : ***https://drive.google.com/file/d/17fxYUeVm6ke44rN0O9PATseT7b-WBIcF/view?usp=sharing***


### **4️⃣ Create & Activate Virtual Environment (Optional)**
```sh
python -m venv venv
# Activate venv:
# On Windows:
.\venv\Scripts\activate.bat
# On macOS/Linux:
source venv/bin/activate
```

### **5️⃣ Install Required Dependencies**
```sh
pip install -r requirements.txt
```

### **6️⃣ Run the Backend (Flask Server)**
```sh
python app.py
```
This will start the Flask server on **http://127.0.0.1:5000**

### Demo Video: ***https://drive.google.com/drive/folders/1T5iyNS-usaWoS_69hw2PB2IrLSIIGyiw?usp=sharing***


## 🖼️ How to Use?
1. Click **Upload & Predict** and select an image.
2. The model processes the image and displays the predicted class & confidence score.
3. The result will be shown below the upload form.

## 📊 Model Performance
- Training Accuracy: **94%**
- Validation Accuracy: **92%**
- Confusion Matrix & Classification Report available in `results`

## 🔥 Technologies Used
- **Python**
- **TensorFlow / Keras**
- **Flask (Backend)**
- **HTML, CSS, JavaScript (Frontend)**

## 🤝 Contributing
Feel free to contact: ***doomsedgehub@gmail.com***


