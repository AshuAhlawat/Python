class Node:
    def __init__(self,data):
        self.parent = None
        self.cur = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.cur)


class MinHeap:
    def __init__(self):
        self.top = None
        self.depth = 0
    

    def add(self,data):
        x = Node(data)

        if self.top:
            t = self.top

            def fill(t):
                
                if t:
                    if t.left:
                        if t.right:
                            t = self.sibling(t)
                            if t.left:
                                t = t.left
                                fill(t)
                            else:
                                fill(t)
                        else:
                            x.parent = t
                            t.right = x
                    else:
                        x.parent = t
                        t.left = x
    
            fill(t)       
        else:
            self.top = x
            self.depth = 1
    
    def sibling(self,child):
        if child.parent:
            if child.parent.left == child:
                return child.parent.right
            
            if child.parent.right == child:
                return child.parent.left
        
        else:
            return child
    
    def __str__(self):
        x = ""

x = MinHeap()

x.add(1)

x.add(2)
x.add(3)

x.add(4)
x.add(5)
x.add(6)
x.add(7)
print(x.depth)
