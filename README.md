# CutiScan-AI-skin-disease-diagnosis-web-platform

## Video Demo:

https://youtu.be/kVCwetoE7ek

## Introduction:

"Cuti" in "CutiScan" originates from the latin word "cutis" which stands for "skin".

This project ultilizes InceptionV3 model trained on a dataset that conbines resources from "DermNet" and https://www.kaggle.com/datasets/subirbiswas19/skin-disease-dataset. ** CONTACT ME FOR THE DATASET USED IN THIS PROJECT. **

### Accuracy (Training): 93%

### Accuracy (Validation): 92%

The dataset consists of 12 classes and 8000 images in total, splits into 80% for training and 20% for testing.

### Skin diseases included are:

acne

alopecia

athlete_foot

cellulitis

chickenpox

cutaneous_larva_migrans

impetigo

nail_fungus

ringworm

shingles

urticaria

vitiligo

<img width="1099" alt="index" src="https://github.com/user-attachments/assets/4cbff99c-d1a9-49e6-a381-063a94b20f3e">

<img width="1098" alt="upload" src="https://github.com/user-attachments/assets/3c35dd49-ca94-49c9-8aeb-e1131eea2afb">

<img width="1098" alt="result" src="https://github.com/user-attachments/assets/bee5d278-a0e2-4278-a40a-32766f35ca80">



## *** Notes ***
### !!!!!Note that this repository does not contain "my_model.keras" model since it exceeds the maximum uploading limit, please contact me for the model if you need it. Also this project requires you to create a database "cutiscan" to store information regarding each disease. You can create such a database with "PHPMyAdmin", only one table with the name "disease" is needed in this project, here is the database structure:


Figure 1: table structure

<img width="552" alt="Screen Shot 2024-10-12 at 10 15 14 AM" src="https://github.com/user-attachments/assets/f75d8448-d105-4312-9e8c-79f81c202b0f">


Figure 2: example of table contents 

<img width="567" alt="Screen Shot 2024-10-12 at 10 15 38 AM" src="https://github.com/user-attachments/assets/9c6c43bd-9b83-42fb-92e5-08b35daf9a61">




## Folder Structure

templates: all web pages are under this folder

static & example: images for displaying on the web

uploads: your uploaded skin images will be stored in here

app.py: main backend component



## How do you run this project (without hosting)
### Prerequisites:

make sure you start your "MySQL Database", "ProFTPD", "Apache Web Server" with Xammp.

### Step 1: 

in cmd/terminal, make sure you locate inside the "CutiScan" directory.

### Step 2:

run command: python app.py or python3 app.py

use the generated link to access CutiScan web platform, it should be http://127.0.0.1:5000









