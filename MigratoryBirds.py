import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(a):
    b=[0,0,0,0,0,0]

# iterate list a 
    for i in a:
        b[i]+=1 
    m=max(b)
    ind=b.index(m)
    return (ind)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
