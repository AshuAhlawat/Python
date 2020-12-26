from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr=random.logistic(size=(2,4))

print(arr)
sns.distplot(arr,hist=False)

plt.show()