from Queue import Queue


class Stack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
    
    def __str__(self):
        x = ""
                if self.queue1:
            return str(self.queue1)
        else:
            return str(self.queue2)
        
        return x

    def __len__(self):
        if len(self.queue1)>0:
            return len(self.queue1)
        else:
            return len(self.queue2)

    def push(self,data):
        if self.queue1:
            self.queue2.enqueue(data)

            while len(self.queue1)!=0:
                self.queue2.enqueue(self.queue1.dequeue())
        
        elif self.queue2:
            self.queue1.enqueue(data)
             
            while len(self.queue2)!=0:
                self.queue1.enqueue(self.queue2.dequeue())
        
        else:
            self.queue1.enqueue(data)
    
    def pop(self):
        if self.queue1:
            return self.queue1.dequeue()
        else:
            return self.queue2.dequeue()
    
    def is_Empty(self):
        if len(self.queue1)>0 or len(self.queue2)>0:
            return False
        else:
            return True
    
    
x = Stack()

x.push(2)
x.push(3)
x.push(1)

x.pop()

print(len(x))
print(x.is_Empty())
