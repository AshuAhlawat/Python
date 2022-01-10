import numpy as np

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))

arr=arr.reshape(-1)
arr=np.sort(arr)
print(arr)

arr=np.array_split(arr,2)

print(np.sort(arr))