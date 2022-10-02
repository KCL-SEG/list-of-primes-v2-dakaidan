"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

import math

MAX = 1000000

def primes(number_of_primes):
    if(number_of_primes <= 0):
        raise ValueError("number_of_primes must be greater than 0")

    list = []
    prime = [True for i in range(MAX)]
    prime[1] = False

    for p in range(2, math.ceil(math.sqrt(MAX))):
        if prime[p]:
            for i in range(2*p, MAX, p):
                prime[i] = False


    for i in range(2, MAX):
        if prime[i]:
            list.append(i)
            if len(list) == number_of_primes:
                break

    return list