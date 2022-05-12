def workbook(n, k, arr):
    book = []
    for chap in arr:
        num = 0
        p_in_c = chap//k
        p_last = chap%k
        
        for i in range(p_in_c):
            page = []
            
            for j in range(k):
                num += 1
                page.append(num)
            
            book.append(page)
        
        if p_last:
            page = []
            for i in range(p_last):
                num+=1
                page.append(num)
            book.append(page)
    print(book)
    count = 0
    for i in range(len(book)):
        if (i+1) in book[i]:
            count+=1
    
    return count
        