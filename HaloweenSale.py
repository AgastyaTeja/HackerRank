#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    wallet=s
    count=0
    while(wallet>=p):
        print("Wallet",wallet,"Intial p",p)
        wallet=wallet-p
        count+=1
        p=p-d
        if(p<m):
            p=m
        
    return(count)
        
   
        
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()

