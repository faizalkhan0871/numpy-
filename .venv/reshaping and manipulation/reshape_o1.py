import numpy as np
matrix = np.array([[10,20,30],[3,4,5]])
vector = np.array([2,3,3])
reshape_arr = vector.reshape(1,3)
print(reshape_arr)
new = matrix + vector
print(new)