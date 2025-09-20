#when we need to change one data type to another data type
# firstly we create a new block [new block=arr.as type(new)]
#print(arr.dtype) that prints only which type of data
 

import numpy as np
arr = np.array([3.5,5.6,3.4])
print(arr.dtype)
int_arr=arr.astype(int)
print(int_arr)
print(int_arr.dtype)