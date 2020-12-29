tokens = ['<greeting>', 'Hello World!', '</greeting>']


countall = 0
countpair=0

for token in tokens:
    if "<" in token:
        countall+=1
    if ">" in token:
        countall+=1

for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        countpair += 1
        
print(countall)
print(countpair)

