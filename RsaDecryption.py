# -*- coding: utf-8 -*-#

class RsaDecryption():

    def __init__(self):
        pass

    def modExp(self, x, n, m):
        y = 1
        while (n > 0):
            if (n % 2 == 1): #if odd
                y = y * x % m
            n = n/2
            x = x * x % m
        return y

    # Decryption
    def decrypt(self, ciphertext, publicKey, totient):
        p = self.modExp(ciphertext, publicKey, totient)
        return p
