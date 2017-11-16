# -*- coding: utf-8 -*-#

import sys, re
import random, secrets
from array import *
from math import gcd
from collections import Counter
from itertools import combinations


# Cryptorandom key generator
# randomly generate a prime number between 0 and 100
def generateRandKey():
    while True:
        num = secrets.randbelow(100)
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

# Functions to generate key e
# Euclidean algorithm: find Greatest Common Divisor (largest integer divisible by both e and phi(n) is 1)
def euclid(a,b):
    while b != 0:
        return gcd(b, a % b)
    else:
        return a

#Return a number if num is coprime to phi(n)
def isCoPrime(list):
    for num,totient in combinations(list, 2):
        if(euclid(num,totient) == 1):
            return True
    return False

# Generate d, using Extended Euclid's algorithm
# which is calculating the inverse of ModExp
# ed = 1 mod totient(n)
def modInverse(a,b):
    store = a
    sign = 1
    r = 1
    s = 0
    while b != 0:
        q = a/b
        temp = r
        r = temp * q + r
        s = temp
        temp = b
        b = a - q * temp
        a = temp
        sign = -sign
    answer = (r - (sign * s)) % store
    return answer

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Modular Exponential - used for encrpytion and decryption
# x is base
# n is exponent
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
def encrypt(p, e, n):
    c = modular_exp(p, e, n)
    return c

# Decryption
def decrypt(c, d, n):
    p = modular_exp(c, d, n)
    return p
