class UnionFind():
    def __init__(self,array=[]):
        self.array = array
        self.group = []
    
    def __len__(self):
        x = 0

        for i in self.group:
            if x:
                if i not in comps:
                    x+=1
            else:
                x+=1
        
        return x

    def __str__(self):
        comps =[]

        for i in self.group:
            if comps:
                if i not in comps:
                    comps.append(i)
            else:
                comps.append(i)

        value = ""

        for comp in comps:
            value+="\n"+str(comp)+": [ "
            for i in range(len(self.group)):
                if comp==self.group[i]:
                    value += str(self.array[i])+" "
            value+="]"


        return value

    def add(self,data):
        self.array.append(data)
        self.group.append(len(self.array)-1)
    
    def union(self,a,b,value=True):
        if value:
            a = self.array.index(a)
            b = self.array.index(b)
        
        a_comp = self.group[a]
        b_comp = self.group[b]

        if a_comp==b_comp:
            pass
        if a_comp!=b_comp:
            a_comp_size = self.group.count(a_comp)
            b_comp_size = self.group.count(b_comp)

            new_comp = None
            if a_comp_size==b_comp_size:
                if a_comp<b_comp:
                    for i in range(len(self.group)):
                        if self.group[i]==b_comp:
                            self.group[i]=a_comp 
                else:
                    for i in range(len(self.group)):
                        if self.group[i]==a_comp:
                            self.group[i]=b_comp 

            elif a_comp_size>b_comp_size:
                for i in range(len(self.group)):
                    if self.group[i]==b_comp:
                        self.group[i]=a_comp      
            else:
                for i in range(len(self.group)):
                    if self.group[i]==a_comp:
                        self.group[i]=b_comp    
    
    def find(self,data,value=True):
        if value:
            data = self.array.index(data)
        
        root = self.group[data]

        comp = []

        for i in range(len(self.group)):
            if root == self.group[i]:
                comp.append(self.array[i])
        
        return comp


def example():
    x = UnionFind()

    x.add(2)
    x.add(3)
    x.add(1)
    x.add(5)

    print(x)

    x.union(2,1)
    print(x)
    x.add(7)
    print(x)
    x.union(7,3)
    print(x)

    print(x.find(7))

    x.union(2,5)
    print(x)

    print(x.find(1))

    x.union(1,7)
    print(x)

# example()

