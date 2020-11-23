class Person:
  def __init__(self, name, age, percentage):
    self.name = name
    self.age = age
    self.percentage = percentage

p1 = Person("John", 36, 99.5)

print(p1.name + "  "  + str(p1.age))
print(p1.percentage)
