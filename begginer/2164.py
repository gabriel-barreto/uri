#!/usr/bin/python3
#-*- coding: utf-8 -*-

import math
r5 = math.sqrt(5)

x = int(input())
fib = (((((1 + r5 ) / 2) ** x) - (((1 - r5) / 2) ** x)) / r5)
print("%.1f" %fib)
