import numpy as np

arr = np.array([0.0, 2.2, 3.3, 4.4], dtype='i')

print(arr)
print(arr.dtype)

newarr = arr.astype(float)

print(newarr)
print(newarr.dtype)

newerarr = np.array(newarr,dtype='i2')

newestarr = newerarr.astype(bool)

print(newestarr)
print(newestarr.dtype)

