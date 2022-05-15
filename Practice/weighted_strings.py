from itertools import groupby

def weightedUniformStrings(s, queries):
    combos = set()
    
    
    grouping = groupby(s)
    
    for key, group in grouping:
        temp = list(group)
        pos = ord(temp[0])-96
        
        for i in range(len(temp)):
            combos.add(pos*(i+1))
    
            
    out = []
    for query in queries:
        if query in combos:
            out.append("Yes")
        else:
            out.append("No")
    
    return out
