# -*- coding: utf-8 -*-#

from rsa_functions import *


def decryption(ciphertext, key_d, key_n):

    print("\n\n################ RSA Decryption - BOB ################")

    plaintext = [ chr(pow(c, key_d, key_n)) for c in ciphertext ]

    print("\nDecryption completed. Original plaintext is: ", plaintext)
    return plaintext
