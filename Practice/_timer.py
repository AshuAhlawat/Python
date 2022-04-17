import time


def timeit(func,params=None):
    
    start = time.time()
    if params:
        func(*params)
    else:
        func()
    end = time.time()
    print("Execution Time: ",end-start)