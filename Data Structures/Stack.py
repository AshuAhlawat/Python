class Stack:
    def __init__(self,x):
        if type(x)==list:
            self.stack = x
            self.top = self.stack[0]
        else:
            return Exception

    def __str__(self):
        x = ""
        for i in self.stack:
            x = x+i+"\n"
            
        return x

    def push(self,x):
        self.stack = [x]+self.stack
        
    def pop(self):
        del(self.stack[0])
        


a = ["a","b","c"]

# b = 3
b = Stack(a)

print(b)

b.push("d")

print(b)

b.pop()
b.pop()

print(b)

print(b.top)
