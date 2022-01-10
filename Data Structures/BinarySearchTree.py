from Queue import Queue

class Node:
    def __init__(self,data):
        self.parent = None
        self.cur = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.cur)

class BinarySearchTree():

    def __init__(self):
        self.head = None
        self.length = 0
    
    def add(self,data):
        x = Node(data)
        t = self.head

        if self.head:
            while True:
                if x.cur<=t.cur:
                    if t.left:
                        t = t.left
                    else:
                        x.parent = t
                        t.left = x
                        break
                else:
                    if t.right:
                        t = t.right
                    else:
                        x.parent = t
                        t.right = x
                        break

        else:
            self.head = x
    
    def inorder(self):
        value = []
        
        def recursive(t):
            if t == None:
                return
            recursive(t.left)
            value.append(t.cur)
            recursive(t.right)
        
        recursive(self.head)
        
        return value
    
    def preorder(self):
        value = []
        
        def recursive(t):
            if t == None:
                return
            value.append(t.cur)
            recursive(t.left)
            recursive(t.right)
        
        recursive(self.head)
        
        return value
    
    def postorder(self):
        value = []
        
        def recursive(t):
            if t == None:
                return
            recursive(t.left)
            recursive(t.right)
            value.append(t.cur)
        
        recursive(self.head)
        
        return value
    
    def levelorder(self):
        value = [self.head]
        
        leveled = []

        while value:
            x = value[0]
            value.remove(x)

            if x:
                leveled.append(x.cur)
                
                value.append(x.left)
                value.append(x.right)
            else:
                leveled.append(None)

                

        return leveled


def example1():
    ref = BinarySearchTree()

    ref.add(2)
    ref.add(1)
    ref.add(3)
    ref.add(4)

    print(ref.head)
    print(ref.head.parent)
    print(ref.head.left)
    print(ref.head.right)
    print(ref.head.right.right)
    print(ref.head.left.parent)
# example1()


def example2():
    from random import randint

    ref = BinarySearchTree()

    for i in range(12):
        x = randint(0,40)
        ref.add(x)
    

    print(ref.levelorder())
    print(ref.inorder())
    print(ref.preorder())
    print(ref.postorder())
    
# example2()

# leveled.append(x.cur)

def example3():
    start = ord("A")
    print(start)
    print(chr(start))
    
    morse = BinarySearchTree()

    for i in range(65,65+27):
        morse.add(chr(i))

    print(morse.levelorder())


# example3()