# -*- coding: utf-8 -*-#

import secrets
from array import *
from math import gcd

# Cryptorandom key generator
# randomly generate a prime number between 0 and 10000
def generateRandKey():
    while True:
        num = secrets.randbelow(10000)
        if(isPrime(num)): return num

def isPrime(x):
    for i in range(2, x-1):
        if x % i == 0: return False
        else: return True

# Compute n
def calculateN(p, q):
    return p * q

# Phi(n)
def totient(p, q):
    return (p-1) * (q-1)

# Generate key e coprime to phi(n)
# this means that the largest integer divisible by both e and phi(n) is 1
def generateE(num, totient):
    while totient != 0:
        num, totient = totient, num % totient
    return num
    # for num in range(1, totient):
    #     if(gcd(num,totient) == 1):
    #         return num

# Generate d, where ed = 1 mod phi(n)
def generateD():
    pass


# Extended Euclid's algorithm to find inverse of ModExp
# ed = 1 % totient(n)
#def euclid(a, b):

# Modular Exponential - used for encrpytion and decryption
# x is base
# n is exponen
# m is modulus
def modular_exp(x, n, m):
    y = 1

    while (n > 0):
        if (n % 2 == 1): #if remainder is 1 then n is an odd
            y = y * x % m
        n = n/2
        x = x * x % m
    return y

# Encryption
# p is plaintext
# e is exponen
# n is modulus
# c is ciphertext
def encrypt(n, e):
    c = modular_exp(p, e, n)
    return c

# Decryption
def decrypt(d, n):
    # use euclid
    pass
