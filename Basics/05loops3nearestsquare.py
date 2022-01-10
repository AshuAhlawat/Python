limit =int(input("Nearest Square to : "))
a=1
square=0
while square < limit:
    a += 1
    square=(a)**2

nearest_lower_square=(a-1)**2
nearest_upper_square=square

if nearest_upper_square-limit<limit-nearest_lower_square:
    print(nearest_upper_square)
else:
    print(nearest_lower_square)