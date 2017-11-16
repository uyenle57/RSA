# -*- coding: utf-8 -*-#

import sys, re
import random, secrets
from binascii import *
from array import *
from math import gcd
from collections import Counter
from itertools import combinations


# RANDOM KEY GENERATOR #
# randomly generate a prime number between 0 and 100
def generateRandKey():
    while True:
        num = secrets.randbelow(100)
        if(isPrime(num)):
            return num

# Check that generated number is a prime
def isPrime(x):
    for i in range(2, x-1):
        if x % i == 0:
            return False
        else:
            return True

# RSA CALCULATIONS #
# Compute n
def calculateN(p, q):
    return p * q

# Phi(n)
def totient(p, q):
    return (p-1) * (q-1)

# Generate public key (e) using Euclidean algorithm
# find Greatest Common Divisor (largest integer divisible by both e and phi(n) is 1)
def euclid(a,b):
    while b != 0:
        return gcd(b, a % b)
    else:
        return a

# Check if key is coprime to phi(n)
def isCoPrime(list):
    for num,totient in combinations(list, 2):
        if(euclid(num,totient) == 1):
            return True
    return False

# Generate private key (d) using Extended Euclidean algorithm
# to calculate Modular multiplicative inverse
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, y, x = egcd(b % a, a)
        return (gcd, x - (b // a) * y, y)

    # gcd is always 1 because a and b are relatively prime
    # (x-(b//a)*y) is the private key (d)
    # // is the integer division operator


# Not working
# def modInverse(a,b):
#     store = a
#     sign, r, s = 1, 1, 0
#     temp, q = 0, 0
#
#     while b != 0:
#         q = a/b
#         temp = r
#         r = temp * q + r
#         s = temp
#         temp = b
#         b = a - q * temp
#         a = temp
#         sign = -sign
#     answer = (r - (sign * s)) % store
#     return answer


# Modular Exponential algorithm for encryption and decryption
# x is base
# n is exponent
# m is modulus
def modExp(x, n, m):
    y = 1
    while (n > 0):
        if (n % 2 == 1): #if odd
            y = y * x % m
        n = n/2
        x = x * x % m
    return y

# Encryption
# p is plaintext
# e is public key
# c is ciphertext
def encrypt(p, e, n):
    c = modExp(p, e, n) # c = p^e mod n
    return c

# Decryption
# d is private key
def decrypt(c, d, n):
    p = modExp(c, d, n) # p = c^d mod n
    return p
