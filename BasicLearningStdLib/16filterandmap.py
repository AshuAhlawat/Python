# Functions

def intinput():
    while True:
        try:
            x=int(input())
            break
        except:
            print("wrong, Re-enter ")
            pass
    return x

# Main
print("No of inputs : ",end="")
x = intinput()

nums = []

print("\n   Inputs")
for i in range(x):
    y = intinput()
    nums.append(y)

print(nums)

even_nums = list(filter(lambda n : n%2==0 , nums))

print("\n", even_nums)

evens_half = list(map(lambda n : int(n/2) , even_nums))

print("\n", evens_half)
    