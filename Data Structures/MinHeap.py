from BinaryTree import BinaryTree

class MinHeap(BinaryTree):
    def __init__(self):
        super().__init__()

    def add(self,data):
        if self.array:
            self.array.append(data)

            pos = len(self)-1
            
            while data<self.array[self.parent(pos,value=False)]:
                self.swap(pos,self.parent(pos,value=False))
                
                if self.parent(pos,value=False):
                    pos = self.parent(pos,value=False)
                else:
                    break        
        else:
            self.array.append(data)
    

    def remove(self,data,value=True):
        if value:
            pos = self.array.index(data)
        else:
            pos = data
        
        self.swap(pos,len(self)-1):
        self.array.pop()

        


def example1():
    x = MinHeap()

    x.add('d')

    x.add('c')
    x.add('e')
    print(x)
    x.add('a')
    x.add('t')
    x.add('b')
    x.add('f')
    print(x)
    x.add('a')
    x.add('h')
    x.add('i')
    x.add('k')
    x.add('b')
    print(x)

# example1()

def example2():
    y = MinHeap()
    for i in range(20,0,-1):
        y.add(i)
    
    print(y)

# example2()