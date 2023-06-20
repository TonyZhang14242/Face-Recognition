import matplotlib.pyplot as plt
import numpy as np

model = ['VGG-Face', 'Facenet', 'OpenFace', 'ArcFace']
y_1_e = [0.745, 0.689, 0.132, 0.670]
y_1_c = [0.811, 0.708, 0.113, 0.726]
y_3_e = [0.687, 0.624, 0.159, 0.656]
y_3_c = [0.767, 0.688, 0.253, 0.703]


x =list(range(len(model)))
total_width, n = 0.8, 2
width = total_width / n


plt.bar(x, y_1_c,  width=width, label='cosine distance', fc='r')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, y_1_e, width=width, label='euclidean distance', tick_label= model, fc='b')

index = np.arange(len(model))
plt.title('Accuracy Under α=1')
plt.xticks(index + width/2, model)
plt.ylabel('Evaluation Factor')
plt.ylim(0,1)
plt.legend()
plt.savefig('./alpha1.png')

