import time


def timeit(func):
    start = time.time()
    func()
    end = time.time()
    print("Execution Time: ",end-start)