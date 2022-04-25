from _timer import timeit


def rev(t):
    t_rev = reversed(str(t))

    x = ""
    for i in t_rev:
        x+=i

    return int(x)


def xyz(n):

    r = int(n**(1/2))
    arr= []
    for i in range(100,1000):
        for j in range(i,1000):
            val = i*j
            
            if val<n:
                if val == rev(val):
                    if val not in arr:
                        arr.append(val)
                        
    sorted_arr = sorted(arr)
    print(sorted_arr)

timeit(xyz,(1000000,))


