import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
#revarr=[]
revarr=(arr[::-1])
for i in revarr:
  print(str(i)+' ',end='')
