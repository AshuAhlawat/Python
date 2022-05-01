from _timer import timeit

def total_delay(head,queue):
    diff = []

    diff.append(abs(head-queue[0]))

    mini = 999
    for i in range(len(queue)):
    
        x  = abs(queue[i]-queue[i+1])
        if x<mini:
            mini = x
        
        diff.append(x)

    print(diff)
    print(sum(diff))



head = 53

queue = [53, 87, 82, 6,12, 89, 78, 10, 62]
queue.sort()
print(queue)

timeit(total_delay,(head,queue))