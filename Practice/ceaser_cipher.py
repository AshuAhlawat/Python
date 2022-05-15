def caesarCipher(string, k):
    k = k%26
    
    up_range = (ord("A"),ord("Z"))
    low_range = (ord("a"),ord("z"))
    
    new_str = ""
    
    for char in string:
        val = ord(char)
        
        if up_range[1] >= val >= up_range[0]:
            val += k
            if val>up_range[1]:
                temp = val - up_range[1]
                temp = temp%26
                val = up_range[0] + temp -1
            
        elif low_range[1] >= val >= low_range[0]:
            val += k
            if val>low_range[1]:
                temp = val - low_range[1]
                temp = temp%26
                val = low_range[0] + temp -1
        
        new_str += chr(val)
        
    return new_str