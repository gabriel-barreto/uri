#!/usr/bin/python3
#-*- coding: utf-8 -*-

str_input = input()
[tabs, actions] = [int(x) for x in str_input.split(" ")]

for i in range(actions):
    action = input()
    if (action == "clicou"):
        tabs -= 1
    elif(action == "fechou"):
        tabs += 1
print(tabs)
