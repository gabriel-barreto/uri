#!/usr/bin/python3
#-*- coding: utf-8 -*-

def join(itens_list):
    sequence = ""
    for item in itens_list:
        sequence += item
    return sequence

while(True):
    try:
        # Getting user input
        chars = input()
        n = int(input())
        pos = [(int(x) - 1) for x in input().split(" ")]
        
        # Mounting phrase by the positions
        phrase = [chars[x] for x in pos]
        
        # Printing result
        print(join(phrase))
    except:
        break
