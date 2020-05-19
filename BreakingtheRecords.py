import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    cmin=0
    cmax=0
    mini=scores[0]
    maxi=scores[0]
    for j in range(len(scores)):
        if (scores[j]>maxi):
            cmax+=1 
            maxi=scores[j]
        elif (scores[j]<mini):
            cmin+=1 
            mini=scores[j]
    return (cmax,cmin)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
