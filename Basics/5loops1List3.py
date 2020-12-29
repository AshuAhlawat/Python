num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116]
odd_list = []
total = 0
for num in num_list:
    if num%2==1:
        odd_list.append(num)

for i in range(0,5):
    total = total + odd_list[i]

print(odd_list)
print(total)
