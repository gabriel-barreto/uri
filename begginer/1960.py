#!/usr/bin/python3
#-*- coding: utf-8 -*-

numerals = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM"
}

num = int(input())
values = sorted(list(numerals.keys()), reverse=True)

def get_major(num):
    for value in values:
        if (num == 0):
            return 0
        elif (value <= num):
            return value

roman = ""
while(num > 0):
    value = get_major(num)
    num -= value
    roman += numerals[value]
print(roman)
