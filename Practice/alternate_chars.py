from itertools import combinations,groupby

def count_alter(combo, string):
    new_str = ""
    for char in string:
        if char in combo:
            new_str += char
    
    grouping = groupby(new_str)
    
    
    length = 0
    for key, group in grouping:
        temp = list(group)
        length += 1
        if len(temp)>1:
            return 0
        
    return length
    


def alternate(s):
    u_s = list(set(tuple(s)))
    
    combos = combinations(u_s,2)
    maxa = 0
    
    for combo in combos:
        num = count_alter(combo, s)
        print(combo, num)
        if num> maxa:
            maxa = num
            
    return maxa