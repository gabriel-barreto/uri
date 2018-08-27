#!/usr/bin/python3
#-*- coding: utf-8 -*-

from math import factorial

# Getting user input
n = int(input())

# Handle with conditions
if (n >= 4):
    # Calculating
    fact_n = factorial(n)
    e = (fact_n / (factorial(2) * factorial(n - 2)))
    f = (fact_n / (factorial(4) * factorial(n - 4)))

    # Printing results
    print("%d" %(e + f + 1))
else:
    print("%d" %(2 ** (n - 1)))
