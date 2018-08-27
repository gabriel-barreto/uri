#!/usr/bin/python3
#-*- coding: utf-8 -*-

# Setting static values
days = {
    "1": "MONDAY",
    "2": "MONDAY",
    "3": "TUESDAY",
    "4": "TUESDAY",
    "5": "WEDNESDAY",
    "6": "WEDNESDAY",
    "7": "THURSDAY",
    "8": "THURSDAY",
    "9": "FRIDAY",
    "0": "FRIDAY",
}

def check(plate):
    if not "-" in plate:
        return False
    
    # Spliting plate
    letters, numbers = plate.split("-")
    
    # Check length of plate groups
    if not len(letters) == 3 or not len(numbers) == 4:
        return False
        
    # Verifying if letter just contain alpha chars
    for letter in letters:
        if letter.islower() or not letter.isalpha():
            return False
            
    # Verifying if numbers just contain numbers
    for number in numbers:
        if not number.isdigit():
            return False
            
    # The plate if valid
    return True
    
    
n = int(input())
for i in range(n):
    plate = input()
    
    if (check(plate)):
        print(days.get(plate[-1]))
    else:
        print("FAILURE")

