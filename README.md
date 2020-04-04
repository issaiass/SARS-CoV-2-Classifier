# SARS-nCOV-2 Classifier

## Warning!, this is not a medical grade tool.


<img src="./imgs/webapp.png" align="right"
     alt="COVID Classifier" width="120">


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
  <img src="./img/runserver.png" alt="Keras Server" width="738">
</p>

I uploaded a non trained version of the model to see the functionality work in the folder 'model'