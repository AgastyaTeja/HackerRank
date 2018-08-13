#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    output=""
    for i in range(p,q+1):
        n = i**2
        temp=str(n)
        if len(str(n))%2==0:
            d=len(str(n))//2
        else:
            d=(len(str(n))+1)//2
        lp=temp[:len(temp)-d]
        rp=temp[len(temp)-d:len(temp)]
        if lp=="":
            lp=0
        elif rp=="":
            rp=0
        
        if(int(lp)+int(rp)==i):
            output=output+" "+str(i)
    if output==" ":
        print("INVALID RANGE")
    else:
        
        print(output[1:])
    
        
        
        
            
        

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)

