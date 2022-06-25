data1 = [1,23,4,134,1412,1,23]
data2 = [2,53,1312,233,13121,56,4]

# for i, (v1, v2) in enumerate(zip(data1, data2)):
#     print(i , v1 + v2)


for v1, v2 in zip(data1,data2):
    print(v1, v2)

for i, val in enumerate(data1):
    print(i, val)