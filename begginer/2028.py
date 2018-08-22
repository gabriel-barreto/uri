#!/usr/bin/python3
#-*- coding: utf-8 -*-

def gen(digit):
    sequence = "0"
    i = 1
    while(i <= digit):
        sequence += ((" %d" %i) * i)
        i += 1
    return sequence

i = 0
while(True):
    try:
        # Populate case index
        i += 1
        
        # Getting user input
        x = int(input())

        # Gen values
        sequence = gen(x)
        size = len(sequence.split(" "))
        message = "numero" if (size == 1) else "numeros"

        # Printing result
        print("Caso %d: %d %s\n%s\n" %(i, size, message, sequence))
    except:
        break
