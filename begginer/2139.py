#!/usr/bin/python3
#-*- coding: utf-8 -*-

from datetime import date

def get_diff(month, day):
    # Getting dates
    christmas = date(2016, 12, 25)
    today = date(2016, month, day)
    
    # Return difference in days
    return (christmas - today).days

while(True):
    try:
        str_input = input()
        [month, day] = [int(x) for x in str_input.split(" ")]
        diff = get_diff(month, day)
        if (diff < 0):
            print("Ja passou!")
        elif (diff == 1):
            print("E vespera de natal!")
        elif (diff == 0):
            print("E natal!")
        else:
            print("Faltam %d dias para o natal!" %diff)
    except:
        break
