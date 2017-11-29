# -*- coding: utf-8 -*-#

class RsaDecryption():

    def __init__(self):
        pass

    def modular_exponentiation(self, x, n, m):
        """ Returns x to the power of n modular m """

        # not working - using pow() instead
        # y = 1.0
        # n = float(n)
        # m = float(m)
        #
        # while (n > 0):
        #     if(n % 2 == 1):
        #         y = y * x % m
        #     n = n/2
        #     x = x * x % m
        # return int(y)

        return pow(x,n,m)

    def decrypt(self, ciphertext, publicKey, totient):
        """ Return plaintext by computing ciphertext to the power of publicKey modular totient """
        p = self.modular_exponentiation(ciphertext, publicKey, totient)
        return p
