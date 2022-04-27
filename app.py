import io
import os
import torch
import torchvision.transforms as transforms
from flask import Flask, jsonify, request, render_template, redirect
from PIL import Image
from EnhancedEfficientNetV2 import *
from Nutrient_API import *


app = Flask(__name__)

# Modelling Task
MODEL = get_model() # EfficientNetV2


food_list= open("./class/class_namesV3.txt", "r", encoding='UTF-8').read().split('\n')
class_names = food_list
  

def get_tensor(image_bytes): # fixedz
    my_transforms = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)

def get_prediction(image_bytes):
    tensor = get_tensor(image_bytes=image_bytes)
    outputs = MODEL.forward(tensor)
    _, prediction = torch.max(outputs, 1)
    food_prediction = class_names[prediction]
    return food_prediction

# Treat the web process
@app.route('/', methods=['GET', 'POST'])
def main_page():
    # upload_file
    if request.method=='GET':
        return render_template('index.html')

    if request.method == 'POST':
        try: 
            if 'file' not in request.files:
                return redirect(request.url)
            file = request.files.get('file')
            if not file:
                return
            img_bytes = file.read()
            food_pred_name = get_prediction(img_bytes) # if utf-8, will weird code
            retrieved_info_1 = retrieve_info(food_name=food_pred_name )
            serving_size = retrieved_info_1['SERVING_WT']
            protein = retrieved_info_1['NUTR_CONT1']
            calorie = retrieved_info_1['NUTR_CONT2']
            fat = retrieved_info_1['NUTR_CONT3']
            carbo = retrieved_info_1['NUTR_CONT4']

            return render_template('result.html', name=food_pred_name, 
            serving_size = serving_size,protein=protein,
            calorie=calorie, fat =fat,  carbo=carbo)

        except:
            return render_template('index.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    # app.run(debug=True) 
    app.run(debug=True,host='0.0.0.0',port=port)