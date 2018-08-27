#!/usr/bin/python3
#-*- coding: utf-8 -*-

# Define static values
songs = {
    0: "PROXYCITY",
    1: "P.Y.N.G.",
    2: "DNSUEY!",
    3: "SERVERS",
    4: "HOST!",
    5: "CRIPTONIZE",
    6: "OFFLINE DAY",
    7: "SALT",
    8: "ANSWER!",
    9: "RAR?",
    10: "WIFI ANTENNAS"
}

# Getting user input
n = int(input())

# Start loop
for i in range(n):
    try:
        # Getting user input
        [x, y] = [int(x) for x in input().strip().split(" ")]
        
        # Building song index
        song = (x + y)
        
        # Getting value and print what did found
        print(songs.get(song, ""))
    except:
        break
