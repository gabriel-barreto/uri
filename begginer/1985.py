#!/usr/bin/python3
#-*- coding: utf-8 -*-

menu = {
    1001: 1.50,
    1002: 2.50,
    1003: 3.50,
    1004: 4.50,
    1005: 5.50
}

total = 0
n = int(input())
for i in range(n):
    str_input = input()
    [code, qtt] = [int(x) for x in str_input.split(" ")]
    total += (menu.get(code, 0) * qtt)

print("%.2f" %total)
