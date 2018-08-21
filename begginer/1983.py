#!/usr/bin/python3
#-*- coding: utf-8 -*-

from operator import itemgetter

n = int(input())

itens = [];
for i in range(n):
    str_input = input()
    [x, y] = [float(x) for x in str_input.split(" ")]
    itens.append({ "code": x, "value": y })
    
itens = sorted(itens, key=itemgetter("value"), reverse=True)
if (itens[0].get("value", 0) < 8):
    print("Minimum note not reached")
else:
    print(int(itens[0].get("code", 0)))

