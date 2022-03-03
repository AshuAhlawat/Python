from _timer import timeit

def main():
    x = 5
    
    for i in range(x+1):
        for j in range(i):
            print("*",end="")
        print("")

    for i in range(x+1):
        for j in range(x+1-i):
            print("*",end="")
        print("")


timeit(main)