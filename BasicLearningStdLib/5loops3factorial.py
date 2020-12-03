number1 = int(input("factorial of : "))
product1 = 1

while number1 > 0:
    product1 *= number1
    number1 -= 1

print(product1)


number2 = int(input("factorial of : "))
product2 = 1

for num in range(1,number2+1):
    product2 *= num

print(product2)