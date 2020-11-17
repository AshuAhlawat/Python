#main

fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

result1 = 0
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
for item in basket_items:
    for fruit in fruits:
        if fruit==item:
            result1 = result1 + basket_items.get(item,0)

print(result1)


result2 = 0
basket2_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
for item in basket2_items:
    for fruit in fruits:
        if fruit==item:
            result2 = result2 + basket2_items.get(item,0)

print(result2)


result3 = 0
basket3_items = { 'lettuce': 2, 'oranges': 3, 'sandwiches': 8, 'pears': 4}
for item in basket3_items:
    for fruit in fruits:
        if fruit==item:
            result3 = result3 + basket3_items.get(item,0)

print(result3)

