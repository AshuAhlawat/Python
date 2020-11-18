#main

fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

result1, total_count1 = 0, 0
basket1_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
for item in basket1_items:
    for fruit in fruits:
        if fruit==item:
            result1 = result1 + basket1_items.get(item,0)
    total_count1 = total_count1 + basket1_items.get(item,0)

print("Fruits in basket1 are {}, and other stuff {}".format(result1,total_count1-result1))


result2, total_count2= 0, 0
basket2_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
for item in basket2_items:
    for fruit in fruits:
        if fruit==item:
            result2 = result2 + basket2_items.get(item,0)
    total_count2 = total_count2 + basket2_items.get(item,0)

print("Fruits in basket2 are {}, and other stuff {}".format(result2,total_count2-result2))


result3 , total_count3= 0, 0
basket3_items = { 'lettuce': 2, 'oranges': 3, 'sandwiches': 8, 'pears': 4}
for item in basket3_items:
    for fruit in fruits:
        if fruit==item:
            result3 = result3 + basket3_items.get(item,0)
    total_count3= total_count3 + basket3_items.get(item,0)

print("Fruits in basket1 are {}, and other stuff {}".format(result3,total_count3-result3))

