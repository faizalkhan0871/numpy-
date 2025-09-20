# to fill the default values in arrays
# np.nan_to_num(arr,nan=value)

import numpy as np
arr  = np.array([19,34,np.nan,np.nan,23])
new_arr = np.nan_to_num(arr,nan=100)
print(new_arr)