# -*- coding: utf-8 -*-#
import secrets
import re
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




def menu():


    regexStr = re.compile("^[a-zA-Z0-9_,.].*$")

    print("==========================================================================")
    print("Computer Security Coursework \nPart 1: RSA Algorithm \nby Uyen Le (tle004)")
    print("==========================================================================\n")

    print("Hello Alice! \n\nSuppose you want to send a private message to Bob...\n")
    print("What would you like to say? \n(Note: you can only use alphanumeric characters in your message)\n")
    inputMessage = str(input("Your plaintext message: "))

    #Input message cannot be empty
    if not inputMessage:
        print("ERROR: Please enter a message.")
        return

    # Validate input using regular expression
    # only alphanumeric characters are allowed
    elif not(regexStr.match(inputMessage)):
        print("\nSorry, only alphanumeric characters allowed. Please try again.")
        return

    #If all above is passed, start the crytosystem
    else:
        print("\nStarting RSA encryption...\n")
        key_p = generateRandKey()
        key_q = generateRandKey()
        print('p is:', key_p)
        print('q is:', key_q)

        print("\nn is:", str(key_p), "*", str(key_q), "=", calculateN(key_q, key_p))

        phiN = totient(key_q, key_p)
        print("\nphi(n) is: (", str(key_p), "-1) * (", str(key_q), "-1) =", phiN)

        # TO DO
        for e in range(1, phiN):
            result = generateE(e, phiN)
        print("\ne (coprime to phi(n)) is: ", result)

        # print("\n d is: ")

        # print ("\n\n Your public key (e,n) is: (", ....)
        # print ("\n\n Your private key (d,n) is: (", ....)

        # print("\n-------------------------------------------------")
        # print("Your Public key can be published anywhere! However your Private Key is be confidential!")
        # print("So that Charlie cannot intercept your private message!\n")
        # print("Your Communication diagram now looks like this:")
menu()
