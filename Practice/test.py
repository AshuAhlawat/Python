# Python3 program to implement stack using a
# single queue
  
q = []
 
# append operation
def append(val):

    # get previous size of queue
    size = len(q)
 
    # Add current element
    q.append(val)
 
    # Pop (or Dequeue) all previous
    # elements and put them after current
    # element
    for i in range(size):
 
        # this will add front element into
        # rear of queue
        x = q.pop(0)
        q.append(x)
            
# Removes the top element
def pop():
 
    if (len(q) == 0):
        return
     
    x = q.pop(0)
    return x


q.append(4)
q.append(3)
q.append(8)
q.pop()
print(q)
