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
    
    def __len__(self):
        x = 0
        for i in self.stack:
            x += 1

        return x

    def push(self,x):
        self.stack = [x]+self.stack
        
    def pop(self):
        x = self.stack[0]
        del(self.stack[0])
        return x
    
    def peek(self):
        return self.top

    def is_empty(self):
        if len(self)==0:
            return True
        else:
            return False

        


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
print(len(b))


for i in b:
    print(i)