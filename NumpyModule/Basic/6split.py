import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)
flatarr=[]

for arre in newarr:
    
    print(arr)
    
    sarre = np.array_split(arre,2)
    for s in sarre:
        flatarr.append(s)

print(flatarr)   

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)

