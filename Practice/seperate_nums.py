def separateNumbers(s):
    # print(f"Number : {s}")
    
    if len(s)==1:
        print("NO")
        return
    
    
    for size in range(1,int(len(s)/2)+1):
        
        temp = s[:size]
        start = temp
        
        # print(start, end=" ")
        while size<len(s):
            val = int(temp)
            
            temp = str(val+1)
            actual = s[size:size+len(temp)]
            
            # print(temp,end=" ")
            
            if temp!=actual:
                break
            else:
                size+=len(temp)
                
        # print("")
                
        if size>=len(s):
            print("YES",start)
            return
    
    print("NO")