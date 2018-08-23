#!/usr/bin/python3
#-*- coding: utf-8 -*-

# Initializing global values
remaining = {
    'people': 0,
    'cars': 0
}

# Start loop
while(True):
    try:
        # Getting user input
        str_input = input()
        
        # Loop break condition
        if (str_input == "ABEND"):
            raise
        
        # Handle with values
        [action, people] = str_input.split(" ")
        
        # Apply conditions
        if (action == "SALIDA"):
            remaining['people'] += int(people)
            remaining['cars'] += 1
        else:
            remaining['people'] -= int(people)
            remaining['cars'] -= 1
    except:
        break

# Showing results
print("%d" %remaining['people'])
print("%d" %remaining['cars'])
