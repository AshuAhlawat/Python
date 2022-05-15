def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    lower = False
    upper = False 
    special = False
    num = False
    
    for char in password:
        if not num:
            if char in numbers:
                num = True
        if not special:
            if char in special_characters:
                special = True
        if not lower:
            if char in lower_case:
                lower = True
        if not upper:
            if char in upper_case:
                upper = True
        
    
    required = 4 - (lower + upper + special + num)
    
    if n + required <6:
        return 6 - n
    
    return required