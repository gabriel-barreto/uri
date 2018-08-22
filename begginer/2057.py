#!/usr/bin/python3
#-*- coding: utf-8 -*-

str_input = input()
itens = [int(x) for x in str_input.split(" ")]
r = sum(itens)
if (r > 24):
    r -= 24
elif (r < 0):
    r += 24
elif (r == 24):
    r = 0
print(r)
