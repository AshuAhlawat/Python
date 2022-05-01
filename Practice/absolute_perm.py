def absolutePermutation(n, k):
    arr = list(range(1,n+1))
    
    if k == 0:
        return arr
    
    if n%2 == 1:
        return [-1]
    else:
        x = int(n/k)
        print(x)
        if x%2 != 0:
            return [-1]
        
        for i in range(1,x,2):
            print(arr[(i-1)*k:i*k],arr[i*k:(i+1)*k])
            arr[(i-1)*k:i*k],arr[i*k:(i+1)*k] = arr[i*k:(i+1)*k],arr[(i-1)*k:i*k]

    
    return arr

n,k = 92, 14

x = absolutePermutation(n, k)

for i in range(len(x)):
    print(abs(x[i] - (i+1)), end=" ")
