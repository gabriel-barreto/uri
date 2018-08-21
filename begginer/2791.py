#!/usr/bin/python3
#-*- coding: utf-8 -*-

str_input = input()
cups = [int(x) for x in str_input.split(" ")]
print(cups.index(1) + 1)
