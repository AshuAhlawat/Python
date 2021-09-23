keyboard = ['','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

pattern = int(input("Enter Number: "))

digits = []
while pattern>0:
    digit = pattern%10
    digits.append(digit)
    pattern = int(pattern/10)
    
digits.reverse()

def prob(digits,n=0,x=''):

    if len(digits)>n:
        for i in keyboard[digits[n]-1]:
            
            prob(digits,n+1,x+i)

    if len(x)==len(digits):
        print(x)

prob(digits)
