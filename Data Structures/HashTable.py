class HashTable:
    
    def __init__(self,length=10,lf=0.4):
        self.lf = lf
        self.length = length
        self.hash_table = [[] for i in range(self.length)]
        
        self.array = []

    def __str__(self):
        x = "#\n"

        for pair in self.array:
            x+=str(pair)+"\n"

        return x

    def __len__(self):
        return len(self.array)

    def __iter__(self):
        return __iter__(self.array)
    
    def _hash(self,key):
        if type(key) in (str,int):
            key = str(key)
            x = 0
            for char in key:
                x += ord(char)
            
            hash_val = x%self.length

            return hash_val

        else:
            raise Exception("wrong Datatype for key")
    
    
    def get(self,key):
        hash_val = self._hash(key)
        
        for pair in self.hash_table[hash_val]:
            if pair[0]==key:
                return pair[1]
        

    def add(self,key,value):
        for pair in self.array:
            if pair[0]==key:
                raise Exception("Duplicate keys not allowed")
                
        pair = (key,value)
        self.array.append(pair)

        if len(self.array)>len(self.hash_table)*self.lf:
            self.length = self.length*2
            self.hash_table = [[] for i in range(self.length)]
            
            for pair in self.array:
                hash_val = self._hash(pair[0])
                self.hash_table[hash_val].append(pair)

        else:
            hash_val = self._hash(key)
            self.hash_table[hash_val].append(pair)
    
    def update(self,key,value):
        new = (key,value)
        for pair in self.array:
            if pair[0]==key:
                self.array[self.array.index(pair)]=new
                break

        hash_val = self._hash(key)

        for pair in self.hash_table[hash_val]:
            if pair[0]==key:
                self.hash_table[hash_val][self.hash_table[hash_val].index(pair)]=new
                break
    
    def delete(self,key):
        for i in range(len(self.array)):
            if self.array[i][0]==key:
                self.array.remove(self.array[i])
                break
        
        hash_val = self._hash(key)

        for pair in self.hash_table[hash_val]:
            if pair[0]==key:
                del(self.hash_table[hash_val][self.hash_table[hash_val].index(pair)])
                break
    


def example1():
    ref = HashTable()

    ref.add("Ashu",[1,2,3,4])
    ref.add("Ankit","whatever")
    ref.add(19,{"nice":34})
    ref.add("19",None)

    print(ref.get(19))
    print(ref.get("19"))

    ref.add("Swaksh",10)
    ref.add("a","a")
    ref.add("c","c")

    print(ref.get("a"))

    ref.add("a",43)

# example1()

def example2():
    ref = HashTable()
    ref.add("a","a")
    print(ref)
    ref.update("a", "b")
    print(ref)
    ref.delete("a")
    print(ref)
# example2()