import scipy.io as io
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,0])

io.savemat('arr.mat', {"vec" : arr})

mydata = io.loadmat('arr.mat')
print(mydata)