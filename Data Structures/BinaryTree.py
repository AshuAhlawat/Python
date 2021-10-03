class BinaryTree:
    def __init__(self):
        self.array = []
        self.dtype = None

    def __len__(self):
        return len(self.array)
    
    def __str__(self):
        x = ""
        
        ap = []
    
        depth = self.depth()
        gap = int(2**(depth-2))
        
        sum = 0
        
        for i in range(depth):
            sum += 2**i
            ap.append(sum)

        x += " "*gap
        for i in range(len(self.array)):
            
            for j in ap:
                new_gap = gap-(2**int(ap.index(j)))
                if i==j:
                    x+="\n"+" "*new_gap
    
            x += str(self.array[i])+" "

        return x

    def swap(self,pos1,pos2,value=True):
        self.array[pos1],self.array[pos2]=self.array[pos2],self.array[pos1]
    
    def top(self):
        return self.array[0]

    def add(self,data):
        if self.array:
            if type(data)==self.dtype:
                self.array.append(data)
            else:
                print("ValueError: [",data,"] not of same datatype")
                quit()
        else:
            self.dtype = type(data)
            self.array.append(data)

    def remove(self,pos,value=True):
        if value:
            self.array.remove(pos)
        else:
            if pos<len(self):
                self.array.remove(self.array[pos])
            else:
                print("Index out of Range")

    def parent(self,pos,value=True):
        if value:
            pos = self.array.index(pos)

        if pos<len(self):
            if pos ==0:
                return None

            if pos%2==0:
                if value:
                    return self.array[int((pos-2)/2)]
                else:
                    return int((pos-2)/2)
            else:
                if value:
                    return self.array[int((pos-1)/2)]
                else:
                    return int((pos-1)/2)
        else:
            print("Index out of Range")
            quit()
    
    def sibling(self,pos,value=True):
        if value:
            pos = self.array.index(pos)

        if pos%2==0:
            if value:
                return self.array[pos-1]
            else:
                return pos-1
        else:
            if pos+1<len(self):
                if value:
                    return self.array[pos+1]
                else:
                    return pos+1        

    def left(self,pos,value=True):
        if value:
            try:
                pos = self.array.index(pos)
            except:
                return None
        
        if pos*2+1<len(self):
            if value:
                return self.array[pos*2 + 1]
            else:
                return pos*2 + 1
        else:
            return None


            
    def right(self,pos,value=True):
        if value:
            pos = self.array.index(pos)

        if pos*2+2<len(self):
            if value:
                return self.array[pos*2 + 2]
            else:
                return pos*2 + 2
        else:
            return None

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

def example():
    x = BinaryTree()

    x.add('a')

    x.add('b')
    x.add('c')

    x.add('d')
    x.add('e')
    x.add('f')
    x.add('g')

    x.add('h')
    x.add('i')
    x.add('j')
    x.add('k')
    x.add('l')
    x.add('m')
    x.add('n')
    x.add('o')

    x.add('p')
    x.add('r')

    x.remove('a')

    print(x,"\n\n")

    print(x.left('c'))
    print(x.right(6,value=False))
    print(x.parent('b'))
    print(x.sibling('h'))


# example()
def example2():
    x = BinaryTree()
    for i in range(0,28):
        x.add(i)
    
    print(x)

example2()