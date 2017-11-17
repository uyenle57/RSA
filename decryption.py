# -*- coding: utf-8 -*-#

class Decryption():

    def __init__(self):
        pass

    # Modular Exponential algorithm for encryption and decryption
    def modExp(self, x, n, m):
        y = 1
        while (n > 0):
            if (n % 2 == 1): #if odd
                y = y * x % m
            n = n/2
            x = x * x % m
        return y

    # Decryption
    # d is private key
    def decrypt(self, c, d, n):
        p = self.modExp(c, d, n) # p = c^d mod n
        return p
