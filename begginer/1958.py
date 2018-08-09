#!/usr/bin/python3
#-*- coding: utf-8 -*-

x = float(input())
val = "{:.4e}".format(x).upper()
if val[0] != "-":
	print("+{}".format(val))
else:
	print(val)
