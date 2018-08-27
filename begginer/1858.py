#!/usr/bin/python3
#-*- coding: utf-8 -*-

from operator import itemgetter

def set(x):
    index = 1
    if (len(entries) >= 1):
        index = (len(entries) + 1)
    entries.append({ "value": x, "index": index })
    return True

# Init values
entries = []

# Getting user input
n = int(input())
[set(int(x)) for x in input().split(" ")]

# Sorting entries
entries = sorted(entries, key=itemgetter("value"))

# Printing result
print(entries[0].get("index", 1))
