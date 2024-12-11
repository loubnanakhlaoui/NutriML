The food recognition and calorie estimation model based on images, developed using TensorFlow and Keras.
The key steps in the project:

### **1. Data Download and Preparation**
- **Data Source:** Downloading a dataset of fruits and vegetables images from Kaggle.
- **Preprocessing:**
  - Using libraries like `ImageDataGenerator` for resizing, normalization, and data augmentation.
  - Organizing data into training, validation, and test sets.

### **2. Recognition Model**
- **Architecture:**
  - Using a pre-trained MobileNetV2 model to extract features from images.
  - Adding dense layers for final classification into 36 food categories.
- **Training:**
  - Images are resized to 224x224 pixels.
  - Data generators are used to handle large volumes of images.

### **3. Demonstration and Predictions**
- **Prediction Functions:**
  - Predicting food items from new images using `model.predict`.
  - Visualizing the results with Matplotlib.
- **Interface:** Supports local images and image loading from URLs.

### **4. Deployment**
- The model is saved in `.h5` format for future use or deployment.

### **5. Challenges**
- Limited resources (CPU/GPU) and the challenge of finding suitable datasets.

<img width="497" alt="image" src="https://github.com/user-attachments/assets/aa34b188-b69e-40c7-a6ac-ced5be1bf0b4">

Choosing image : <img width="545" alt="image" src="https://github.com/user-attachments/assets/4dc22f4a-943b-480f-a7a3-0a59f2ea6750">
Results: <img width="533" alt="image" src="https://github.com/user-attachments/assets/90c55a8c-0d0c-45d8-9a7c-c34873d691fc">

