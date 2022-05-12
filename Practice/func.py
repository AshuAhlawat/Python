
def palindrome_checher(str_input):

    rev = str_input[::-1]

    # for i in range(len(str_input)-1,-1,-1):
    #     rev+= str_input[i]

    if rev == str_input:
        return True
    else:
        return False


print(palindrome_checher("ababa"))