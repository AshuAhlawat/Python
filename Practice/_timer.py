import time


def timeit(func,params):
    start = time.time()
    func(*params)
    end = time.time()
    print("Execution Time: ",end-start)