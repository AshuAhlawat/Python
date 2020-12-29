from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr=random.poisson(lam=10, size=(2,3))
print(arr)

sns.distplot(arr, hist=False, label='poisson')

plt.show()