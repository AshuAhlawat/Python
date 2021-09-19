x = 'abcba'
y = 'acbac'
z = 'abcd'



def is_palindrome(str):
    inv = ""
    x = len(str)
    for i in range(x):
        inv += str[x-i-1]
    
    if inv == str:
        return True
    else:
        return False
    

print(is_palindrome(z))
print(is_palindrome(x))
print(is_palindrome(y))