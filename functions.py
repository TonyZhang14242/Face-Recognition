from deepface import DeepFace
import matplotlib.pyplot as plt
import os
models = ["VGG-Face", "Facenet", "OpenFace", "DeepID", "ArcFace"]
model_name = models[0]
metrics_avail = ["cosine", "euclidean"]
metrics = metrics_avail[0]
lib_path = './VGG-Face2/train'
test_class = 10
test_path = f'./VGG-Face2/test/{test_class}/'

def find():
    cur_path = os.getcwd()
    print(cur_path)
    fig_name = os.listdir(test_path)[0]
    res = DeepFace.find(img_path=test_path+fig_name, db_path=lib_path, model_name= model_name, distance_metric=metrics, enforce_detection= False)
    print(res[0].to_numpy()[0][0], res[0].to_numpy()[0][5])
    img0 = plt.imread(test_path+fig_name)
    plt.subplot(2, 2, 1)
    plt.imshow(img0)
    plt.title('origin img')
    plt.axis('off')
    
def detect():
    #num = 61
    fig_name = os.listdir(test_path)[0]
    res = DeepFace.analyze(img_path= test_path+fig_name, actions= ['age' , 'emotion', 'race'], enforce_detection=False)
    print(res)
    
if __name__ == '__main__':
    find()