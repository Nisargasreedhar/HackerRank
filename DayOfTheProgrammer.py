#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    dd=0
    mm='09'
    if 1700<=year<=1917:
        if year%4==0:
            dd=12
        else:
            dd=13
    elif year==1918:
        dd=26
    elif 1919<=year<=2700:
        if (year%4==0 and year%100!=0) or year%400==0:
            dd=12
        else:
            dd=13
    return (str(dd) + '.' + (mm) + '.' + str(year))
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
