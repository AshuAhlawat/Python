class Node:
    def __init__(self,data):
        self.cur = data
        self.prev = None
        self.next = None
    
    def __str__(self):
        return str(self.cur)