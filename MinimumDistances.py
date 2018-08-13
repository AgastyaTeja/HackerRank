#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    values={}
    output=[]
    for i in set(a):
        values[i]=[]
        for j in range(len(a)):
            if a[j] == i:
                values[i].append(j)
        if(max(values[i])-min(values[i])!=0):
            
            output.append(max(values[i])-min(values[i]))
    if not output:
        
            
        return(-1)
    else:
        return(min(output))
            
                
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

