import time as t

initial = t.time()
print(initial)

sum=0
for i in range(25):
    sum+=i
print(sum)

print(t.time()-initial)