from SingleLinkedList import SingleList

class Queue:
    def __init__(self):
        self.queue = SingleList()
        self.front = self.queue.head
        self.back = self.queue.tail

    def __str__(self):
        return str(self.queue)

    def __len__(self):
        return len(self.queue)

    def __iter__(self):
        return iter(self.queue)

    def enqueue(self,data):
        self.queue.add(data)
        self.front = self.queue.head
        self.back = self.queue.tail
        
    
    def dequeue(self):
        x = self.front
        self.queue.remove()
        self.front = self.queue.head
        self.back = self.queue.tail

        return x

    def peek(self):
        return self.front
    

x = Queue()

x.enqueue(3)
x.enqueue(5)
x.dequeue()
x.enqueue(2)
x.enqueue(6)

print(x)
print(x.peek())

for i in x:
    print(i)

