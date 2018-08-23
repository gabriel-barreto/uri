#!/usr/bin/python3
#-*- coding: utf-8 -*-

def handle(value):
    if (value < 10):
        return ("0%d" %value)
    else:
        return value

def get_hour(hour, minute):
    return ("%s:%s" %(handle(hour), handle(minute)))

n = int(input())
for i in range(n):
    # Getting user input
    str_input = input()
    [hour, minute, status] = [int(x) for x in str_input.split(" ")]
    
    # Getting data
    message = "abriu" if (status == 1) else "fechou"
    time = get_hour(hour, minute)
    
    # Printing result
    print("%s - A porta %s!" %(time, message))
    
