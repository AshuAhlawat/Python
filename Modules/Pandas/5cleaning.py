import pandas as pd

x = pd.read_csv("Python\PandasModule\datac2.csv")
print(x.to_string())

meanx = x["Calories"].mean()
medianx = x["Calories"].median()
modex = x["Calories"].mode()[0]

x["Calories"].fillna(meanx,inplace = True)
print(x.to_string())

x.dropna(inplace = True)
# x.dropna(subset=['Date'], inplace = True)
print(x.to_string())

x["Date"]=pd.to_datetime(x["Date"])
print(x.to_string())

x.loc[7,"Duration"]=45
print(x.to_string())

x["Date"]=pd.to_datetime(x["Date"])
print(x.to_string())

for x in x.index:
  if x.loc[x, "Duration"] > 120:
    x.drop(x, inplace = True)
print(x.to_string())

x.drop_duplicates(inplace = True)
print(x.to_string())