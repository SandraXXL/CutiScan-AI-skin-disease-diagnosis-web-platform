# CutiScan: AI skin disease diagnosis web platform

<p align="center">
  <strong>Accuracy: 0.9127</strong><br>
  <strong>Precision: 0.9168</strong><br>
  <strong>Recall: 0.9127</strong><br>
  <strong>F1-score: 0.9121</strong><br>
  <br>

  👋 Hi! Please contact me if you need the dataset and model used in this project, as I cannot upload them due to file size limits.
</p>

## Video Demo:

https://youtu.be/kVCwetoE7ek

## Introduction:
This is my first AI project, utilizing the InceptionV3 model trained on a dataset that merges resources from DermNet and https://www.kaggle.com/datasets/subirbiswas19/skin-disease-dataset. The dataset consists of 12 classes and 8000 images in total, splits into 80% for training and 20% for testing. The name "CutiScan" is derived from the Latin word "cutis," meaning "skin."

### The main functions are:  
1. Upload skin photo  
2. Crop photo  
3. Display possible results  
4. Classify 12 different skin diseases  
5. Provide detailed information on each skin disease

### Skin diseases included are:

acne, 
alopecia, 
athlete_foot, 
cellulitis, 
chickenpox, 
cutaneous_larva_migrans, 
impetigo, 
nail_fungus, 
ringworm, 
shingles, 
urticaria, 
vitiligo.

### Preview of main web pages:

<img width="1099" alt="index" src="https://github.com/user-attachments/assets/4cbff99c-d1a9-49e6-a381-063a94b20f3e">

<img width="1098" alt="upload" src="https://github.com/user-attachments/assets/3c35dd49-ca94-49c9-8aeb-e1131eea2afb">

<img width="1098" alt="result" src="https://github.com/user-attachments/assets/bee5d278-a0e2-4278-a40a-32766f35ca80">



## Notes:
This project requires you to create a database "cutiscan" to store information regarding each disease. You can create such a database with "PHPMyAdmin", only one table with the name "disease" is needed in this project, here is the database structure:


Figure 1: table structure

<img width="552" alt="Screen Shot 2024-10-12 at 10 15 14 AM" src="https://github.com/user-attachments/assets/f75d8448-d105-4312-9e8c-79f81c202b0f">


Figure 2: example of table contents 

<img width="567" alt="Screen Shot 2024-10-12 at 10 15 38 AM" src="https://github.com/user-attachments/assets/9c6c43bd-9b83-42fb-92e5-08b35daf9a61">




## Folder Structure:

### templates: 
all web pages are under this folder

### static & example: 
images for displaying on the web

### uploads: 
your uploaded skin images will be stored in here

### app.py: 
main backend component



## How do you run this project (without hosting):
### Prerequisites:

make sure you start your "MySQL Database", "ProFTPD", "Apache Web Server" with Xammp.

### Step 1: 

in cmd/terminal, make sure you locate inside the "CutiScan" directory.

### Step 2:

run command: python app.py or python3 app.py

use the generated link to access CutiScan web platform, it should be http://127.0.0.1:5000









