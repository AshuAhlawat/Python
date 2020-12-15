import numpy as np

arr = np.array([1, 2, 3])

newarr = np.add(arr, arr)
print(newarr)

newarr = np.sum([arr, arr])
print(newarr)

newarr = np.sum([arr, arr], axis=1)
print(newarr)

newarr = np.cumsum(arr)
print(newarr)

newarr = np.diff(arr)
print(newarr)

newarr = np.diff(arr,n=2)
print(newarr)