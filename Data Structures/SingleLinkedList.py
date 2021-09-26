class Node:
    def __init__(self,data):
        self.cur = data
        self.prev = None
        self.next = None
    
    def __str__(self):
        return str(self.cur)

class SingleList:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def add(self,x):
        x = Node(x)

        if self.head:
            self.tail.next = x
            self.tail = x
        else:
            self.head = x
            self.tail = x

    def insert(self,x,index=0):
        if index>= len(self):
            return "RuntimeError : Index["+str(index)+"] out of Range["+str(len(self))+"]"
        else:
            x = Node(x)
            if index==0:
                x.next = self.head
                self.head = x

            else:
                t = self.head

                while index>1:
                    t = t.next
                    index-=1

                x.next = t.next
                t.next = x

    def get(self,index):
        if index>= len(self):
            return "RuntimeError : Index["+str(index)+"] out of Range["+str(len(self))+"]"
        else:
            val = self.head
            while index>0:
                val = val.next
                index-=1
            
            return val.cur

    def clear(self):
        self.head = None
        self.tail = None    
    
    def pop(self):
        x = self.head
        y = self.tail

        while x:
            if x.next == self.tail:
                x.next = None
                self.tail = x
                break
            x = x.next
        
        return y
        
    def remove(self,index=0):
        if index>= len(self):
            return "RuntimeError : Index["+str(index)+"] out of Range["+str(len(self))+"]"
        else:
            if index==0:
                x = self.head
                self.head = x.next
                x.next = None

            else:
                t = self.head

                while index>1:
                    t = t.next
                    index -= 1
                
                x = t.next
                t.next = t.next.next
                x.next = None

    def __str__(self):
        txt = "[ "
        x = self.head

        while x:
            txt+=str(x.cur)+" "
            x=x.next

        return txt +"]"
    
    def __len__(self):
        if self.head:
            x = self.head
            size = 0
            while x:
                size += 1
                x=x.next
            
            return size
        else:
            return 0


ex = SingleList()

ex.add(4)
ex.add(3)
ex.add(9)
ex.add(6)

print(ex)

ex.insert(1)
ex.insert(5)
print(ex)

ex.insert(11,3)
print(ex)

ex.pop()
print(ex)

ex.remove()
print(ex)

ex.remove(3)
print(ex)


print(ex.head,ex.tail)
print(len(ex))
print(ex.get(2))

ex.clear()
print(ex)

