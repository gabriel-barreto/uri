#!/usr/bin/python3
#-*- coding: utf-8 -*-

def split_number(n):
    s = ("%d" %n)
    return [int(x) for x in s]

while(True):
    try: 
        # Getting user input
        [_,  x] = [int(x) for x in input().split(" ")]
        
        # Processing input and printing result
        if (x % 3 == 0):
            print("%d sim" %sum(split_number(x)))
        else:
            print("%d nao" %sum(split_number(x)))
    except:
        break
