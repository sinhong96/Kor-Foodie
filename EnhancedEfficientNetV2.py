import timm
import torch 

food_list= open("./class/class_namesV3.txt", "r", encoding='UTF-8').read().split('\n')
class_names = food_list

def get_model():
    checkpoint_path = './model/No_num_worker_model_efficientnetv2_m-KoreanFood100_current_ckpt.pt'
    checkpoint = torch.load(checkpoint_path, map_location = 'cpu')
    model_name = 'efficientnetv2_rw_m'
    model = timm.create_model(model_name, pretrained=True)
    model.reset_classifier(len(class_names))  
    model.load_state_dict(checkpoint['state_dict'],strict=False)    
    model.eval()
    return model
