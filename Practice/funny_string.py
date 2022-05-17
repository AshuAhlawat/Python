def funnyString(s):
    s = list(map(ord, list(s)))
    s_rev = list(reversed(s))
    
    print(s) 
    print(s_rev)
    
    for i in range(1,len(s)):
        diff1 = abs(s[i] - s[i-1])
        diff2 = abs(s_rev[i] - s_rev[i-1])
        
        print(diff1, diff2)
        
        if diff1!=diff2:
            return "Not Funny"
        
    return "Funny"