from deepface import DeepFace
import os

models = ["VGG-Face", "Facenet","OpenFace", "ArcFace"]
model_name = models[0]
metrics_avail = ["cosine", "euclidean"]
metrics = metrics_avail[1]
lib_path = './VGG-Face2/train'
test_class = 'Su Bingtian'
test_dir = './VGG-Face2/test'
test_path = f'{test_dir}/{test_class}/'


def model_comparison_acc():
    
    print('Start Test...')
    print(f'Test class number = {len(os.listdir(test_dir))}')
    for m in models:
        all_num = 0
        model_correct = 0.0
        for dir in os.listdir(test_dir):
            img = os.listdir(test_dir+'/'+dir)[0]
            res = DeepFace.find(img_path=test_dir+'/'+dir+'/'+img, db_path=lib_path, model_name=m, distance_metric=metrics, enforce_detection=False)
            for i in range(3):
                if i >= len(res[0]):
                    break
                res_dir = res[0].to_numpy()[i][0].split('/')[-2]
                if dir == res_dir:
                    model_correct += 1.0
                    print(f'find {dir}')
                all_num += 1
        print(f'{m} acc = {model_correct/(all_num)}, metrics = {metrics}')
        with open(file='./res.txt',mode='a') as f:
            f.write(f'{m} acc = {model_correct/(all_num)}, metrics = {metrics}\n')
        
def model_acc_on_first():
    
    print('Start Test...')
    print(f'Test class number = {len(os.listdir(test_dir))}')
    for m in models:
        all_num = 0
        model_correct = 0.0
        for dir in os.listdir(test_dir):
            img = os.listdir(test_dir+'/'+dir)[0]
            res = DeepFace.find(img_path=test_dir+'/'+dir+'/'+img, db_path=lib_path, model_name=m, distance_metric=metrics, enforce_detection=False)
            if len(res[0]) != 0:
                res_dir = res[0].to_numpy()[0][0].split('/')[-2]
                if dir == res_dir:
                    model_correct += 1.0
            all_num += 1
        print(f'{m} acc = {model_correct/(all_num)}')
        with open(file='./res_first.txt',mode='a') as f:
            f.write(f'{m} acc = {model_correct/(all_num)}, metrics = {metrics}\n')
                    
if __name__ == '__main__':
    model_comparison_acc()