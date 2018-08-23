#!/usr/bin/python3
#-*- coding: utf-8 -*-

from math import factorial
while(True):
    try:
        # Getting user input
        str_input = input().strip().replace(" ", "")
        
        # Loop break condition
        if (str_input == "0"):
            raise
        
        print(factorial(len(str_input)))
    except:
        break
        
