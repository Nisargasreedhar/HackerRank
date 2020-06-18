#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    nbill=[]
    s=sum(bill)
    ns=s-bill[k]
    ans=ns/2
    if (b==ans) or (b<ans):
        print ('Bon Appetit')
    else: 
        ref= b-ans
        print (int(ref))

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
