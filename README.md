# What is this?  
Animal classification using CNN to identify the animal from an image, then return an animated gif from giphy.  
The images used to train the model are from https://www.kaggle.com/alessiocorrado99/animals10  
Other references are commented in the notebook

# About
CSPC481  
Project name: Animal Classification  
Member: Alexander Lin  
Undergrad  

# Installation
Download the repo  
`pip install -r requirements.txt`  
If that doesn't work for everything, please install dependencies as needed  
`pip install flask`  
`pip install tensorflow`  
`pip install keras`  
`pip install pillow`  

# Setup
1. Follow Installation step above  
2. Create models folder where app.py is  
3. Download model from https://www.dropbox.com/s/tdp0u8ywkezu208/model7.h5?dl=0  
4. Put Model7.h5 in models folder  
5. Start API with `python app.py`  
6. Use either of the options below  

# Option: browser
1. Go to localhost:5000/ or the IP of the machine running the API
2. Upload an image  

# Option: android device/emulator
1. Install "animal classification.apk", for this option you have to use same machine running API  
2. Tap on select image button  
3. Upload an image  
4. Tap on guess button  
