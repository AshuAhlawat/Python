import pandas as pd

y = pd.Series([1,2,5,3,2],index=[1,2,3,4,5])
print(y,"\n",y[1])

y = pd.Series({"day1": 420, "day2": 380, "day3": 390})
print(y,"\n",y["day2"])