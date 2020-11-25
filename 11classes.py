class Person:
    def __init__(theObject, name, age, percentage):
        theObject.name = name
        theObject.age = age
        theObject.percentage = percentage
    
    def percentdef(marks):
        x="I scored {} in 12 th".format(marks.percentage)
        return x    

p1 = Person("John", 36, 99.5)
p1.age=18

print(p1.name + "  "  + str(p1.age))

print(p1.percentdef())

del p1.age
print(p1)

del p1




