#!/usr/bin/python3
#-*- coding: utf-8 -*-

def calc(part, total):
    return ((part * 100)/total)
    
str_input = input()
[x, y] = [float(x) for x in str_input.split(" ")]
r = calc((y - x), x)

print("%.2f%%" %r)
