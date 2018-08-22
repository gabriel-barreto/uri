#!/usr/bin/python3
#-*- coding: utf-8 -*-

while(True):
    try:
        str_input = input()
        [hour, minutes] = [int(x) for x in str_input.split(":")]
        time = 0
        if (hour >= 7):
            hour -= 7
            time = ((hour * 60) + minutes)
        print("Atraso maximo: %d" %time)
    except:
        break
