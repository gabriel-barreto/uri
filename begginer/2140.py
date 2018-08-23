#!/usr/bin/python3
#-*- coding: utf-8 -*-

bills = [100, 50, 20, 10, 5, 2]

def get_change(value):
    used = 0

    # Decrement values with bills
    for bill in bills:
        if (value >= bill):
            value -= bill
            used += 1
        if (value == 0):
            break
    
    # Checking value and returning result
    if (value == 0 and used == 2):
        return True
    else:
        return False

while(True):
    # Getting user input
    str_input = input()
    [x, y] = [int(x) for x in str_input.split(" ")]
    
    # Break loop condition
    if (x == y == 0):
        break
    
    # Printing results
    if (get_change(y - x)):
        print("possible")
    else:
        print("impossible")
