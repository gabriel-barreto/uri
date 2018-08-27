#!/usr/bin/python3
#-*- coding: utf-8 -*-

def join(itens):
    s = ""
    for item in itens:
        s += ("{} ".format(item))
    return s.strip()
    
# Setting static value
s = [1, 1]

# Getting user input
n = int(input())

# Handle with index
if (n < 2):
    # Building an index to get a substring of default sequnece
    index = (n - 1)
    if (index <= 0):
        index = 1
    
    # Printing result
    print(join(s[0:index]))
else:
    # Removing initialized values
    n -= len(s)
    
    # Generating sequence
    for i in range(n):
        s.append(s[-1] + s[-2])
        
    # Printing genereted sequence
    print(join(s[::-1]))
    
