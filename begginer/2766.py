#!/usr/bin/python3
#-*- coding: utf-8 -*-

names = []
while(True):
    try:
        if (len(names) == 10):
            break
        names.append(input())
    except:
        break
        
print(names[2])
print(names[6])
print(names[8])
