#!/usr/bin/python3
#-*- coding: utf-8 -*-

def get_multiples(divisor, values):
    multiples = []
    for x in values:
        if ((x % divisor) == 0):
            multiples.append(values)
    return multiples

int(input())
str_input = input()
values = [int(x) for x in str_input.split(" ")]

for i in range(2, 6):
    print("%d Multiplo(s) de %d" %(len(get_multiples(i, values)), i))
