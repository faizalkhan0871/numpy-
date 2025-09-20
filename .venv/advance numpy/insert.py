#insert any number in an array
#arr=original array
#Index
#value
#axis=0 row wise
#axis=1 column wise
#axis=none([1,2,3])
import numpy as np
arr_list=np.array([10,20,30,40,50,60,70,80,90])
new_arr=np.insert(arr_list,2,100,axis=0)
print(new_arr)