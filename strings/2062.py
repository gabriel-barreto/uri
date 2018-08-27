#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re

# Building regexs
uri_exp = re.compile('(^|\s){1}(UR){1}([A-Z]){1}(?![a-zA-Z])+')
obi_exp = re.compile('(^|\s){1}(OB){1}([A-Z]){1}(?![a-zA-Z])+')

# Getting user inputs
n = int(input())
sentence = input()

# Replace cases
sentence = str(uri_exp.subn(" URI", sentence)[0]).strip()
sentence = str(obi_exp.subn(" OBI", sentence)[0]).strip()

print(sentence.strip())
