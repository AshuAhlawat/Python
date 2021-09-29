class BinaryTree:
    def __init__(self):
        self.array = []

    def add(self,data):
        self.array.append(data)
        
    
    def top(self):
        return self.array[0]

    def __str__(self):
        x = ""
        
        ap = []

        depth = self.depth()
        sum = 0
        for i in range(depth):
            sum += 2**i
            ap.append(sum)


        for i in range(len(self.array)):
    
            for j in ap:
                if i==j:
                    x+="\n"
    
            x += str(self.array[i])+" "

        return x
    
    def depth(self):
        size = len(self.array)
        # print(size)
        i = 0
        j = 0

        while True:
            if size<=j:
                return i
            else:
                j += 2**i
                i +=1
        
        


x = BinaryTree()

x.add(1)

x.add(2)
x.add(3)

x.add(4)
x.add(5)
x.add(6)
x.add(7)

x.add(8)
x.add(4)
x.add(5)
x.add(6)
x.add(7)
x.add(4)
x.add(5)
x.add(6)

x.add(7)

print(x)