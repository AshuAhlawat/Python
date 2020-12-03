#function

def factorial(a):
    #This function is used to find factorial
    #INPUT : an integer greater than 0
    #OUTPUT : gives the factorial
    
    a=int(a)
    
    if a==1:
        return 1
    else:
        return a * factorial(a-1)

#main

x=0
while x<1:
    #x=int(input("Factorial of : "))
    x=10
    if x<1:
        print("Wrong Entry")

print("= {}".format(factorial(x)))
