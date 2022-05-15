def insertionSort1(n, arr):
    val = arr[-1]
    for i in range(n-2, -1,-1):
        if arr[i]> val:
            arr[i+1] = arr[i]
            print(arr)

            if i == 0:
                arr[0] = val
                print(arr)
        else:
            arr[i+1] = val
            print(arr)
            break
        





arr = list(range(2,11))
arr.append(1)
n = len(arr)

insertionSort1(n, arr)