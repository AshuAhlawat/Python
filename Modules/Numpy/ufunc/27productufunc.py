import numpy as np

arr = np.array([1, 2, 3, 4])

x = np.prod(arr)
print(x)

x = np.prod([arr,arr])
print(x)

x = np.prod([arr, arr], axis=1)
print(x)

x = np.cumprod(arr)
print(x)