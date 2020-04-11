# SARS-nCOV-2 Classifier

## Warning!, this is not a medical grade tool.


<img src="https://github.com/issaiass/SARS-CoV-2-Classifier/blob/master/imgs/webapp.PNG?raw=true" align="right"
     alt="COVID Classifier" width="240">


This is an example of a simple SARS-CoV-2 Classifiewer Web App.  It uses simple JS, keras, flask, as the complete framework to make a deep learning simple server based app.

Steps to start are simple:

* **Install dependencies** and **Run the server**.
* First train a model based on SARS-CoV-2 (here we are using a binary classifier).
* Installed flask and keras, run the server app.py.
* Open a web browser with localhost:5000.
* Access the server (locally o remotely in your LAN) and upload an image.
* **Browse and Image** from your local machine.
* **Press Diagnose** and wait for the model to be classified.

<p align="center">
  <img src="https://github.com/issaiass/SARS-CoV-2-Classifier/blob/master/imgs/runserver.PNG?raw=true" alt="Keras Server" width="738">
</p>

I uploaded a non trained version of the model to see the functionality work in the folder 'model'.
Now you can view a first version of the transfer learning implementation.  
This will be modified later to do better estimates, right now is biased.  
I used the inceptionv3 model and image augmentation to match same samples in normal and covid folders.
The author of the covid dataset is always improving the content and columns of the dataframe are always changing (expect an error in those lines and fix it eliminating the correct columns).
app_call.py is an example of a python call to the server and view the json output (test only).
You can also call app.py and test with cURL as *curl -X POST -F image=@normal.jpg 'http://localhost:5000/predict'*.