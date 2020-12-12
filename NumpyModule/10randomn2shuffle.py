import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(np.random.permutation(arr))

print(arr)

np.random.shuffle(arr)

print(arr)