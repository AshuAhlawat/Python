import math
import os
import random
import re
import sys


def activityNotifications(ex, d):
    # print(ex, d)
    no = 0
    trail = ex[0:d]
    trail.sort()
    
    if d%2==0:
        mid = (int(d/2),int(d/2 - 1))

        for i in range(d,len(ex)):
            median = (trail[mid[0]] + trail[mid[1]])/2

            val = ex[i]
            if val >= 2*median:
                no+=1
        
            # print(trail, val)
            
            trail.pop(0)

            for j in range(len(trail)):
                if trail[j]>=val:
                    trail.insert(j,val)
                    # print(j)
            
            trail.insert(len(trail),val)

    else:
        mid = int(d/2)

        for i in range(d,len(ex)):
            median = trail[mid]

            val = ex[i]
            if val >= 2*median:
                no+=1
            
            trail.pop(0)

            for j in range(len(trail)):
                if trail[j]>=val:
                    trail.insert(j,val)
                    
            trail.insert(len(trail),val)

    return no


if __name__ == '__main__':

    with open("./test.txt","r") as f:
        data = f.readlines()

    first_multiple_input = data[0].rstrip().split()

    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])

    expenditure = list(map(int, data[1].rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)