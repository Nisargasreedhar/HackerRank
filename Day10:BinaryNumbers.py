import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
quo=n
rem = 0
maximum = 0
count=0
while (quo > 0):  
    rem=quo % 2 
    if rem==1: 
        count+=1  
        if count > maximum:
            maximum = count
    else:
        count=0 
    quo=quo//2  
print (maximum)
