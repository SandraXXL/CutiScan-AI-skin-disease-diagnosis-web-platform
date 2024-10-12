# CutiScan-AI-skin-disease-diagnosis-web-platform

Introduction:

"Cuti" in "CutiScan" originates from the latin word "cutis" which stands for "skin".

This project ultilizes InceptionV3 model trained on a dataset that conbines resources from DermNet and https://www.kaggle.com/datasets/subirbiswas19/skin-disease-dataset.

Accuracy (Training): 93%
Accuracy (Validation): 92%

The dataset consists of 12 classes and 10000+ images in total, each class contains approximately 850 images. Dataset splits into 80% for training and 20% for testing.

Skin diseases included are:
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

<img width="1435" alt="Screen Shot 2024-10-11 at 5 46 58 PM" src="https://github.com/user-attachments/assets/b9694bd2-1276-4ac9-be93-b735030de02b">

<img width="1439" alt="Screen Shot 2024-10-11 at 5 47 15 PM" src="https://github.com/user-attachments/assets/63938378-9071-4f23-a8c8-50fb62c13593">

<img width="659" alt="Screen Shot 2024-10-12 at 10 17 17 AM" src="https://github.com/user-attachments/assets/11d57e72-80d3-446e-a18c-f136636fa636">

<img width="1365" alt="Screen Shot 2024-10-12 at 10 17 54 AM" src="https://github.com/user-attachments/assets/afbdfeef-0fc3-410f-a895-0bebeebe9ad7">

# *** Notes ***
!!!!!Note that is repository does not contain "my_model.keras" since it exceeds the maximum uploading limit, you are supposed to run the model again and then save it yourself!!!!!
Also this project requires you to create a database named "cutiscan" to store informations regarding each diseases. You can create such a dataset with "PHPMyAdmin", only one table with the name "disease" is needed in this project, here is the database structure:

Figure 1: table structure
<img width="552" alt="Screen Shot 2024-10-12 at 10 15 14 AM" src="https://github.com/user-attachments/assets/f75d8448-d105-4312-9e8c-79f81c202b0f">

Figure 2: example of table contents 
<img width="567" alt="Screen Shot 2024-10-12 at 10 15 38 AM" src="https://github.com/user-attachments/assets/9c6c43bd-9b83-42fb-92e5-08b35daf9a61">




# Folder Structure
templates: all web files are under this folder
static & example: images for displaying on web pages
uploads: your uploaded skin images will be stored in here
app.py: main backend component



# How do you run this project (without hosting)
Prerequisites:
make sure you start your "MySQL Database", "ProFTPD", "Apache Web Server" with Xammp.

Step 1: 
in cmd/terminal, go to "CutiScan" directory.

Step 2:
run command: app.py
use the generated link to access to access CutiScan web platform.









