# Kor-Foodie

This is the documentation of Master thesis project 

This project is about using trained model (En-EffNetV2) to develop a food recognition Python Flask application and deploy to using Heroku through Heroku

This repo contains a sample code to show how to create a Flask API server by deploying our PyTorch model. This is a sample code which goes with [tutorial](https://pytorch.org/tutorials/intermediate/flask_rest_api_tutorial.html).

The deployment of flask application to Heroku through Docker is with the reference of [Flask-Docker-Heroku](https://medium.com/@ashok7067/containerise-your-python-flask-using-docker-and-deploy-it-onto-heroku-a0b48d025e43).

## Requirements

Install them from 'requirements.txt':

    pip install -r requirements.txt

## Local Deployment

Run the server:

    python app.py

## Our Demo App

Click this link to run our demo app

[Kor-Foodie Demo App](https://korfoodiev1.herokuapp.com/)

## How it works
Screen 1: Homepage             |  Screen 2: Take photo with camera or choose image from gallery              
:-------------------------:|:-------------------------:
<img src="https://github.com/sinhong96/Kor-Foodie/blob/main/app_screen/S1.jpg" width="250" height="500">   |   <img src="https://github.com/sinhong96/Kor-Foodie/blob/main/app_screen/S2.jpg" width="250" height="500">   
Screen 3: preview uploaded image             |  Screen 4: Retrieve prediction of food and corresponding nutrient content                  
<img src="https://github.com/sinhong96/Kor-Foodie/blob/main/app_screen/S4.jpg" width="250" height="500"> | <img src="https://github.com/sinhong96/Kor-Foodie/blob/main/app_screen/S5.jpg" width="250" height="500">   |   

## Heroku Deployment

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://korfoodiev1.herokuapp.com/)

## License

Please check 'LICENSE' for more details.

Please star this github repo if you like the content. Thank you ~
