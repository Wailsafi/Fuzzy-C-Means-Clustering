import numpy as np
from PIL import Image
def U_matrix(X_size, C_size):
    U=np.zeros((X_size, C_size))
    return U
def distance(a, b):
    return np.linalg.norm(a - b)

def computeCentroids(X, U, m, k):
    C = []
    d = X.shape[1]  # Number of features (e.g., 3 for RGB)
    for i in range(k):
        weight_sum = np.power(U[:, i], m).sum()
        Cj = []
        for x in range(d):
            numerator = (X[:,x] * np.power(U[:, i], m)).sum()
            c_val = numerator / weight_sum
            Cj.append(c_val)
        C.append(Cj)
    return np.array(C)
import numpy as np

import numpy as np







            
       
            

from PIL import Image
image = Image.open("milky-way.jpg")
mg_array = np.array(image)
mg_array_flat = mg_array.reshape(-1, mg_array.shape[2])
mg_array_flat.shape

image.show()



k=2
U=np.ones((1024*1024,k))


m=1.5



    



