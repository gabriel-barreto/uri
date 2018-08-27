#!/usr/bin/python3
#-*- coding: utf-8 -*-

def get_primes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    
    # Return all prime numbers
    return [p for p in range(2, n) if prime[p]]
    
def found_divisors(primes, value):
    return [p for p in primes if (value % p == 0)]

while(True):
    try:
        # Getting user input
        x = int(input())
    
        # Break loop condition
        if (x == 0):
            raise
        
        primes = get_primes(x)
        [d1, d2, d3] = found_divisors(primes, x)
        
        # Printing results
        print("%d = %d x %d x %d" %(x, d1, d2, d3))
    except:
        print(e)
        break
        
