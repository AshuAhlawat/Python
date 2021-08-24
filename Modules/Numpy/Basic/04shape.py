import numpy

multi = numpy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(multi,"\n\n",multi.shape,"\n")

for i in numpy.nditer(multi):
    print(i,end=" ")

multu = numpy.array(multi,ndmin=4)
print("\n",multu,"\n",multu.shape)

multo = multu.copy()
print("\n")
multo = multo.reshape(-1)

print(multo)

multy = multo.reshape(4, -1)

print(multy)

print(multy.base)
