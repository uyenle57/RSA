# -*- coding: utf-8 -*-#
import secrets
import re
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
def calculateN(p, q):
    return p * q

# Phi(n)
def totient(p, q):
    return (p-1) * (q-1)

# Generate key e coprime to phi(n)
def calculateE(e):
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

    inputMessage = str(input("Enter the plaintext message you want to encrypt: "))

    regexStr = re.compile("^[a-zA-Z0-9_,.].*$")

    #Input message cannot be empty
    if not inputMessage:
        print("ERROR: Please enter a message.")
        return

    # Validate input using regular expression
    # only alphanumeric characters are allowed
    elif not(regexStr.match(inputMessage)):
        print("\nERROR: Your message must be in plaintext (only alphanumeric characters allowed).")
        print("Please try again.")
        return

    #If all above is passed, start the crytosystem
    else:
        print("\nStarting RSA encryption...\n")
        key_p = generateRandKey()
        key_q = generateRandKey()
        print('p is:', key_p)
        print('q is:', key_q)

        print("\nn is:", str(key_p), "*", str(key_q), "=", calculateN(key_q, key_p))

        print("\nphi(n) is: (", str(key_p), "-1) * (", str(key_q), "-1) =", totient(key_q, key_p))

        # TO DO
        # print("\n e (coprime to phi(n)) is: ")
        # print("\n d is: ")
        # print ("\n\n Encryption key (e,n) is: (", ....)
        # print ("\n\n Decryption key (d,n) is: (", ....)

        # print("-------------------------------------------------")
        # print("We now have the Communication diagram as follows:")
menu()
