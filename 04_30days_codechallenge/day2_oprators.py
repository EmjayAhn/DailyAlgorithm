# https://www.hackerrank.com/challenges/30-operators/problem

import sys

def solve(meal_cost, tip_percent, tax_percent):
    total_cost = meal_cost * (1 + tip_percent/100 + tax_percent/100)
    print(round(total_cost)) 

meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())

solve(meal_cost, tip_percent, tax_percent)

