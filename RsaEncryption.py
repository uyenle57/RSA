# -*- coding: utf-8 -*-#

import sys, re
import random, secrets
from array import *
from math import gcd
from itertools import combinations


class RsaEncryption():

    def __init__(self):
        pass

    # RANDOM KEY GENERATOR #
    # Check that generated number is a prime
    def isPrime(self, x):
        for i in range(2, x-1):
            if x % i == 0: #even
                return False
            else: #odd = prime
                return True

    # randomly generate a prime number between 0 and 100
    def generateRandKey(self):
        while True:
            self.num = secrets.randbelow(100)
            if(self.isPrime(self.num)):
                return self.num

    # RSA CALCULATIONS #
    # Compute n
    def calculateN(self, p, q):
        return p * q

    # Phi(n)
    def totient(self, p, q):
        return (p-1) * (q-1)

    # Generate public key (e) using Euclidean algorithm
    # find Greatest Common Divisor (largest integer divisible by both e and phi(n) is 1)
    def euclid(self, a, b):
        while b != 0:
            return gcd(b, a % b)
        else:
            return a

    # Check if key is coprime to phi(n)
    def isCoPrime(self, list):
        for num, totient in combinations(list, 2):
            if(self.euclid(num, totient) == 1):
                return True
        return False

    # Generate private key (d) using Extended Euclidean algorithm
    # to calculate Modular multiplicative inverse
    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            gcd, y, x = self.egcd(b % a, a)
            return (gcd, x - (b // a) * y, y)

        # gcd is always 1 because a and b are relatively prime
        # y is the modular multiplicative inverse of b % a
        # x is the modular multiplicative inverse of a % b
        # // is the integer division operator

    # Modular Exponential algorithm for encryption and decryption
    # x is base
    # n is exponent
    # m is modulus
    def modExp(self, x, n, m):
        y = 1
        while (n > 0):
            if (n % 2 == 1): #if odd
                y = y * x % m
            n = n/2
            x = x * x % m
        return y

    # Encryption
    def encrypt(self, plaintext, privateKey, totient):
        c = self.modExp(plaintext, privateKey, totient)
        return c
