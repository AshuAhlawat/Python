test1 = "((a+b)+c)"
test2 = "(a*b)"
test3 = "a+b"
test4 = "((a+b)+c)+(d+(e+f))"
test5 = "((a+b)+c)"
test6 = "a +((b+c))" 

def extra_brac(eqn):
    if "((" in eqn:
        index = eqn.find("((")
        for i in range(index+2, len(eqn)-1):
            if eqn[i]==")":
                if eqn[i+1]==")":
                    return True
                else:
                    return False

        return False
    else:
        return False


print(extra_brac(test1))
print(extra_brac(test2))
print(extra_brac(test3))
print(extra_brac(test4))
print(extra_brac(test5))
print(extra_brac(test6))
