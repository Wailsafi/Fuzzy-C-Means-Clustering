
import numpy as np
from PIL import Image
def U_matrix(X_size, C_size):
    U=np.ones((X_size, C_size))
    return U
def distance(a, b):
    return np.linalg.norm(a - b)

def computeCentroids(X, U, m, k):
    C = []
    d = X.shape[1]  
    for i in range(k):
        weight_sum = np.power(U[:, i], m).sum()
        Cj = []
        for x in range(d):
            numerator = (X[:,x] * np.power(U[:, i], m)).sum()
            c_val = numerator / weight_sum
            Cj.append(c_val)
        C.append(Cj)
    return np.array(C)
def U_update(X, U, C, k, m):
    X_size = X.shape[0]  
    
    # Precompute the distance matrix between all points and all centroids
    dist_matrix = np.zeros((X_size, k))
    for i in range(k):
        dist_matrix[:, i] = np.linalg.norm(X - C[i], axis=1)
    
   
    dist_matrix[dist_matrix == 0] = 1e-8
    
    # Update the U matrix
    for j in range(k):
        num = dist_matrix[:, j]
        denom = np.sum((num[:, None] / dist_matrix) ** (2 / (m - 1)), axis=1)
        U[:, j] = 1 / denom

    # Normalize U so that the sum across all memberships for a point is 1
    # U /= U.sum(axis=1, keepdims=True)
    
    return U

image = Image.open("milky-way.jpg")
mg_array = np.array(image)
mg_array_flat = mg_array.reshape(-1, mg_array.shape[2])
mg_array_flat.shape

image.show()

U=np.random.rand(1024*1024,2)
U1=np.zeros(((1024*1024,2)))
epsilon=0.01
while(np.linalg.norm(U-U1)>epsilon):
    C=computeCentroids(mg_array_flat,U, 1.5,2 )
    U1=U
    U= U_update(mg_array_flat, U, C, 2, 1.5)

max_index=np.argmax(U)









    



