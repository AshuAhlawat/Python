import pandas as pd

c = pd.read_csv("./Modules/Pandas/datac1.csv")
print(c)

df = pd.read_json('./Modules/Pandas/dataj.json')
print(df.to_string())