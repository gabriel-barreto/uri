#!/usr/bin/python3
#-*- coding: utf-8 -*-

def set_bonus(values, bonus):
    if(values[2] % 2 == 0):
        values[0] += bonus
        values[1] += bonus

def check(pk1, pk2):
    p1 = pk1[0] + pk1[1]
    p2 = pk2[0] + pk2[1]
    
    if (p2 > p1):
        return "2"
    elif (p1 > p2):
        return "1"
    return "0"
    
# Getting number of rounds
n = int(input())

for i in range(n):
    # Getting user inputs
    bonus = int(input())
    p1 = [int(x) for x in input().split(" ")]
    p2 = [int(x) for x in input().split(" ")]
    
    # Aggregating bonus
    set_bonus(p1, bonus)
    set_bonus(p2, bonus)
    
    # Get result
    r = check(p1, p2)
    
    # Printing
    if (r == "0"):
        print("Empate")
    elif (r == "1"):
        print("Dabriel")
    else:
        print("Guarte")
        
