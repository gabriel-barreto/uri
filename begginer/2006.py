#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
x = int(input())
regex = (r'[%d]{1}' %x)

tea = input()
found = re.findall(regex, tea)
print(len(found))
