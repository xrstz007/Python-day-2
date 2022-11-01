# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 22:33:58 2022

@author: oluwo
"""
# Program to give a list of prime numbers between 1 and any given number.

#first create a prime number checker function
def prime_checker(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True
# then use the prime function to check each number in the range.
def prime_numbers(number):
    lst = []
    for num in range(2, number + 1):
        prime = prime_checker(num)
        if prime == True:
            lst.append(num)
    return lst

print(prime_numbers(11))
        
         