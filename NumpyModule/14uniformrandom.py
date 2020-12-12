from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr=random.uniform(size=(2,3))

print(arr)
sns.distplot(arr,hist=False)

plt.show()