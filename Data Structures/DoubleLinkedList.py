class Node:
    def __init__(self,data):
        self.cur = data
        self.prev = None
        self.next = None
    
    def __str__(self):
        return str(self.cur)

class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self,data):
        x = Node(data)

        if self.head:
            self.tail.next = x
            x.prev = self.tail

            self.tail  = x
            self.tail.next = None
            
        else:
            self.head = x
            self.tail = x
    
    def insert(self,data,index=0):
        if index>= len(self):
            return "RuntimeError : Index["+str(index)+"] out of Range["+str(len(self))+"]"
        else:
            x = Node(data)
            if index==0:
                x.next = self.head
                self.head.prev = x
                self.head = x
            else:
                t = self.head
                while index>1:
                    t= t.next
                    index -=1
                
                y = t.next

                t.next = x
                y.prev = x
                x.next = y
                x.prev = t
    
    def get(self,index):
        if index>= len(self):
            return "RuntimeError : Index["+str(index)+"] out of Range["+str(len(self))+"]"
        else:
            t = self.head
            
            while index>0:
                t = t.next
                index -=1
            
            return t

    def clear(self):
        self.head.next = None
        self.head = None
        self.tail.prev = None
        self.tail = None

    def pop(self):
        if self.head:
            t = self.tail.prev
            x = self.tail

            t.next = None
            x.prev = None
                
            self.tail = t

            return x
        else:
            return Exception
    
    def remove(self,index=0):
        if index>= len(self):
            return "RuntimeError : Index["+str(index)+"] out of Range["+str(len(self))+"]"
        else:
            t = self.head
            if index==0:
                t.next.prev = t.prev
                self.head = t.next
                t.next = None
                
            else:
                while index>0:
                    t= t.next
                    index -=1

                t.prev.next = t.next
                t.next.prev = t.prev

                t.next = None
                t.prev = None
            
            return t
                
    
    def __str__(self):
        txt = "[ "
        x = self.head
        while x:
            txt+=str(x.cur)+" "
            x = x.next
        
        return txt +"]"
    
    def __len__(self):
        x = self.head
        size = 0

        while x:
            size+=1
            x = x.next
        
        return size
        


def example1():
    ex = DoubleList()

    ex.add(4)
    ex.add(3)
    ex.add(9)
    ex.add(6)
    print(ex)

    ex.insert(7)
    print(ex)

    ex.insert(5,3)
    print(ex)

    ex.pop()
    print(ex)

    ex.remove()
    print(ex)

    ex.remove(2)
    print(ex)

    print(ex.get(2).prev)


# example1()