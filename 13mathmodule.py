import platform
import math
#https://www.w3schools.com/python/module_math.asp

print("\t\t\t\t   Platform : "+platform.system())

x=float(input("Square Root of : "))
print(round(math.sqrt(x),4))

print(math.ceil(math.sqrt(x)))