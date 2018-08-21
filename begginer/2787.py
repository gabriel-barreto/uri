#!/usr/bin/python3
#-*- coding: utf-8 -*-

x = int(input())
y = int(input())

if (((x % 2 != 0) and (y % 2 != 0)) or ((x % 2 == 0) and (y % 2 == 0))):
    print(1)
else:
    print(0)
