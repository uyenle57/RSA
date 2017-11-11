# -*- coding: utf-8 -*-#
import secrets

# Cryptorandom key generator
# randomly generate a prime number between 0-1000
def randNum(num):
    for i in range(2,10):
        if (i % 2 == 0):
            return
        else:
            num = i
    return num

# Generate two 16bit primes p,q
# def randPrime():


# Compute n
def getN(p, q):
    return p * q

# Phi(n)
def totient(p, q):
    return (p-1) * (q-1)

# Generate key e coprime to phi(n)
# def getE(e):
#     #use randNum




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

    print(secrets.randbits(16))
menu()
