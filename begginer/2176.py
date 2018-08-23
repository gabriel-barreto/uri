#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
def count(sequence):
    # Find all bits in sequence
    regex = r'[1]{1}'
    found = len(re.findall(regex, sequence))
    
    # Return false to even
    if (found % 2 == 0):
        return False
        
    # True for odds
    return True
    
    
# Getting user input
sequence = input()

# Handle with sequence
additional = "0"
if (count(sequence)):
    additional = "1"

# Printing result
print("%s%s" %(sequence, additional))
