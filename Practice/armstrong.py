
x = 15


x_str = str(x)

total = 0

for char in x_str:
    digit = int(char)

    total+= digit**3

if total == x:
    print("Armstrong Number")
else:
    print("No")