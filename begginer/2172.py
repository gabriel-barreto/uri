#!/usr/bin/python3
#-*- coding: utf-8 -*-

while(True):
    try:
        [x, y] = [int(x) for x in input().split(" ")]

        # Loop break condition
        if (x == y == 0):
            raise
       
        print("%d" %(x * y))
    except:
        break
