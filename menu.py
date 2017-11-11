# -*- coding: utf-8 -*-#
import sys
import random
import secrets
from array import *

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
def getN(p, q):
    return p * q

# Phi(n)
def totient(p, q):
    return (p-1) * (q-1)

# Generate key e coprime to phi(n)
def getE(e):
    pass

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

# Extended Euclidean function to find inverse of Modular Exponential
# ed = 1 % totient(n)
#def euclid(a, b):

# Encryption
# p is plaintext
# e is exponen
# n is modulus
# c is ciphertext
def encrypt(n, e):
    c = modular_exp(p, e, n)
    return c

# # Decryption
# def decrypt(d, n):
# #use euclid()

def menu():

    print("==========================================================================")
    print("Computer Security Coursework \nPart 1: RSA Algorithm \nby Uyen Le (tle004)")
    print("==========================================================================")

    input_message = str(input("Enter the message you want to encrypt: "))

    if not input_message:
        print("Please enter a message.")
        return
    else:
        print("\nStarting RSA encryption\n")
        print('Generating two primes...')
        rand_p = generateRandKey()
        rand_q = generateRandKey()
        print('p is: ', rand_p)
        print('q is: ', rand_q)
menu()
