#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re

while(True):
    try:
        itens = re.findall(r'[(0-9)]+', input())
        [print(item) for item in itens]
    except:
        break
        
