import math
import os
import random
import re
import sys


def getTotalX(a, b):
    # Write your code here
    ele1=max(a)
    ele2=min(b)
    arr1=[]
    arr2=[]
    count=0
    for i in range(ele1,ele2+1):
        for j in range(len(a)):
            if i%a[j]==0:
                arr1.append(i)                
            else:
                continue
        for k in range(len(b)):
            if b[k]%i==0:
                arr2.append(i)
            else:
                continue
        for x in range(len(arr1)):
            if arr1[x] in arr2:
                count+=1
    return count

            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
