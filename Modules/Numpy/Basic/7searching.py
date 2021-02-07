import numpy

arr = numpy.array([1, 2, 3, 4, 5, 4, 4, 7])
print(arr)

x = numpy.where(arr%2==1)
print(x)

odd=[]
for i in x[0]:
    odd.append(arr[i])

print(odd)

b = int(input("How many entries do you want? "))
a=[]
for i in range(b):
    inp = int(input("Enter  : "))
    a.append(inp)

for i in range(len(a)):
    y = numpy.searchsorted(odd,a[i])
    odd.insert(y,a[i])

oddr=[]
for i in range(len(odd)):
    oddr.append(odd.pop())

print(oddr)