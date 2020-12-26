import numpy

x = numpy.random.randint(100, size=(3, 5))

y = numpy.random.rand()

print(x,y)

x = numpy.random.choice([3, 5, 7, 9],size=(1,2))

print(x)

x = numpy.random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)