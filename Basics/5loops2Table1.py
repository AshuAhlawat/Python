#one way
num = int(input("\nTable of : "))

for times in range(num,num*10+1,num):
    print("{} X {} = {}".format(num,int(times/num),times))


#another way
num2 = int(input("\nTable of : "))

for times in range(1,10+1,1):
    print("{} X {} = {}".format(num2,times,num2*times))