#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re

i = 0
while(True):
    try:
        # Couting case number
        i += 1
        
        # Building regex
        regex = (r'(%s){1}' %input())
        
        # Getting sequence
        sequence = input()
        
        # Searching for matches
        found = 0
        index = 0
        for match in re.finditer(regex, sequence):
            found += 1
            index = match.span()[0]
            
        # Printing results
        if (found > 0):
            print(
                "Caso #%d:\nQtd.Subsequencias: %d\nPos: %d\n"
                %(i, found, index + 1)
            )
        else:
            print("Caso #%d:\nNao existe subsequencia\n" %i)
    except:
        break
