#!/usr/bin/python3
#-*- coding: utf-8 -*-

x = int(input())
strHex = str(hex(x))
strHex = strHex.split('0x').pop()
print(strHex.upper())
