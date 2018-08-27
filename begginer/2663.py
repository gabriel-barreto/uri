#!/usr/bin/python3
#-*- coding: utf-8 -*-

# Getting user input
n = int(input())
mx = int(input())
points = [int(input()) for i in range(n)]

# Sorting points
points = sorted(points, reverse=True)

# Getting number of classifieds
bigger = points[0]
i = 0
while(i < mx):
    # Counting classifieds
    i += points.count(bigger)
    
    # Removing used number
    [points.remove(bigger) for i in range(points.count(bigger))]
        
    # Update bigger number from points list
    if (i < mx):
        bigger = points[0]
    
# Printing result
print(i)
