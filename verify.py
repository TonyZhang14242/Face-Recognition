from deepface import DeepFace
import os
model_name = "VGG-Face"
metrics = "cosine"

def find():
    cur_path = os.getcwd()
    print(cur_path)
    fig_name = os.listdir('./VGG-Face2/test/4/')[0]
    res = DeepFace.find(img_path='./VGG-Face2/test/4/'+fig_name, db_path='./VGG-Face2/train', model_name= model_name, distance_metric=metrics, enforce_detection= False)
    print(res)
    
if __name__ == '__main__':
    find()