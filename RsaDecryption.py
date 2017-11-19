# -*- coding: utf-8 -*-#

class RsaDecryption():

    def __init__(self):
        pass

    def modExp(self, x, n, m):
        # convert ints to floats to mitigate integer division problem (rounding errors)
        y = 1.0
        n = float(n)
        m = float(m)
        
        while (n > 0):
            if (n % 2 == 1): #if odd
                y = y * x % m
            n = n/2
            x = x * x % m
        return int(y)

    # Decryption
    def decrypt(self, ciphertext, publicKey, totient):
        p = self.modExp(ciphertext, publicKey, totient)
        return p
