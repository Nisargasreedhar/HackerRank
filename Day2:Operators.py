import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip_amount=meal_cost*(tip_percent/100.0)
    tax_amount=meal_cost*(tax_percent/100.0)
    total_cost=meal_cost+tip_amount+tax_amount
    mc=round(total_cost)
    print (mc)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
