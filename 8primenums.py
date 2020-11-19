numbers=[]
i = int(input("How many entries : "))

while i>0:
    numbers.append(int(input("No. ")))
    i-=1
print(numbers)

for number in numbers:
    if number==1 or number==0:
        print("{} is neither prime not composite".format(number))
        continue
    if number==2:
        print("{} is a prime number".format(number))
        continue
    j = 2
    while number%j != 0:
        if j==(number+1)/2:
            print("{} is a prime number".format(number))
            break
        else:
            j += 1
    if number%j == 0:
        print("{} is a composite number".format(number))