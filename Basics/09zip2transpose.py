matrix=[(1,2,3),(2,3,1),(4,2,4),(9,2,5)]

matrixt=list(zip(*matrix))
print(matrixt)

columns=["col 1","col 2","col 3"]
columns=[column.title() for column in columns]

for i, column in enumerate(columns):
    print("{}:{}".format(column,matrixt[i]))