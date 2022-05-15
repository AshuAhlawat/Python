def pangrams(s):
    if len(s) < 26:
        return "not pangram"
    
    u_s = list(set(tuple(s.lower())))
    u_s.remove(" ")
    
    if len(u_s) != 26:
        return "not pangram"
    else:
        return "pangram"