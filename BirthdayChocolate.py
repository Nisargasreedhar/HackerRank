import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m, n):
    summ=0
    c=0
    arr=[]
    for i in range(0,n-m+1):
        try:
            summ=sum(s[i:m+i])
            if summ==d:
                c+=1
        except:
            break
    return (c)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m, n)

    fptr.write(str(result) + '\n')

    fptr.close()
