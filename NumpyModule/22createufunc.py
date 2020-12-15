import numpy

def power(x,y,z):
    return x**y,z


uPower = numpy.frompyfunc(power,3,1)



print(uPower([1,2,3,4,5],[1,2,2,2,2],[1,2,3,4,5]))
