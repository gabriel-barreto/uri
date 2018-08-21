#!/usr/bin/python3
#-*- coding: utf-8 -*-

while(True):
    try:
        date = input()
        [day, month, year]= date.split("/")
        print("{}/{}/{}".format(month, day, year))
        print("{}/{}/{}".format(year, month, day))
        print("{}-{}-{}".format(day, month, year))
    except:
        break
