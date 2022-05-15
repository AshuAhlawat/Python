import pandas as pd

dataset = pd.read_csv("./email.csv", sep=";", index_col=None, na_values=["NA"])

print(dataset.head(2))

print(dataset.info())
print(dataset.describe())

print(dataset.Username)

print(dataset["Identifier"].add_prefix("hi"))

print(dataset.all())
print(dataset["Identifier"].abs())


dataset = dataset.sort_values("Identifier").copy()

print(dataset[:4])

print(dataset.loc[0])
print(dataset.iloc[0])

print(dataset.at[0,"Username"])
print(dataset.iat[0,0])

print(dataset.iloc[0:3, 0:3])
print(dataset.loc[[0,3,2], ["Username", "Identifier", "Login email"]])

print(dataset[dataset["Identifier"]>5000])

print(dataset[dataset["Username"].isin(["capti", "grey07"])])

print(pd.isna(dataset))

print(dataset.fillna("unknown@gmail.com"))

print(dataset.dropna())
print(dataset["Identifier"].mean())
print(dataset["Identifier"].std())

print(dataset.loc[:, ["Identifier"]].apply(lambda x: x.max() - x.min()))

print(dataset["Last name"].str.lower())
