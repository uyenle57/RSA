# -*- coding: utf-8 -*-#

import textwrap
from collections import Counter
from RsaEncryption import *
from RsaDecryption import *


def menu():

    print (textwrap.dedent("""
        ==========================================================================
        Computer Security Coursework
        Part 1: RSA Algorithm
        by Uyen Le (tle004)
        ==========================================================================
    """))

    print("Hello Alice! \nSuppose you want to send a private message to Bob. What would you like to say?\n")
    inputMessage = str(input("Your message: "))

    if not inputMessage:
        print("ERROR: Please enter a message.")
        sys.exit(1)
    else:

        print("\n################ RSA Encryption - ALICE ###############")

        rsaEncryption = RsaEncryption()

        # Randomly generate keys p and q between 0 and 100
        key_p = rsaEncryption.generateRandPrime()
        key_q = rsaEncryption.generateRandPrime()

        # ensure primes are distinct
        while key_q == key_p:
            key_q = rsaEncryption.generateRandPrime()

        print('p is:', key_p)
        print('q is:', key_q)

        # Verify p an q are primes
        if rsaEncryption.isPrime(key_p):
            print("Verified p is prime!")
        else:
            print("ERROR: p is not prime. Please try again.")
            sys.exit(1)

        if rsaEncryption.isPrime(key_q):
            print("Verified q is prime!")
        else:
            print("ERROR: q is not prime. Please try again.")
            sys.exit(1)


        # Calculate key n
        key_n = rsaEncryption.calculateN(key_p, key_q)
        print("\nn is:", str(key_p), "*", str(key_q), "=", key_n)

        # Calculate phi(n)
        phiN = rsaEncryption.totient(key_p, key_q)
        print("phi(n) is: (", str(key_p), "-1) * (", str(key_q), "-1) =", phiN)

        # Generate key e
        # by adding all coprime numbers to phi(n) to a list, then randomly pick a number in that list
        coPrimeList = []

        for i in range(2, phiN):
            if(rsaEncryption.isCoPrime([i, phiN])):
                coPrimeList.append(i)

        key_e = coPrimeList[random.randint(0, len(coPrimeList)-1)]
        print("\ne is: ", key_e)

        # Verify e is coprime to phiN
        if gcd(key_e,phiN) == 1:
            print("Verified e is coprime!")
        else:
            print("ERROR: E is not coprime. Please try again.")
            sys.exit(1)

        # Generate key d using Extended Euclidean algorithm
        _, key_d, _ = rsaEncryption.egcd(key_e, phiN)

        # ensure key e and d are distinct
        while key_e == key_d:
            key_e = coPrimeList[random.randint(0, len(coPrimeList)-1)]
            _, key_d, _ = rsaEncryption.egcd(key_e, phiN)

        # ensure key d is positive
        if key_d < 0:
            key_d = key_d % phiN

        print("\nd is: ", key_d)

        # verify d is coprime to phiN
        if gcd(key_d,phiN) == 1:
            print("Verified d is coprime!")
        else:
            print("ERROR: D is not coprime. Please try again.")
            sys.exit(1)

        # Public and private key
        print ("\nPublic key is: ", (key_e, key_n))
        print ("Private key is: ", (key_d, key_n))
        print("\n(!) You can now publish your public key, however your private key must be kept private!")


        print("\n=> Starting encryption using Private key...")

        # ord(): Converts a string character to its ordinal Unicode character representation.
        ciphertext = [ rsaEncryption.encrypt(ord(c), key_d, key_n) for c in inputMessage ]
        print("\nEncryption completed. Your ciphertext is: ", ciphertext)

        send = str(input("\nPress 's' then Enter to send your ciphertext to Bob: "))
        if not send == 's':
            print("\nYou must send your ciphertext to Bob to continue.\n")
            sys.exit(1)
        else:

            print("\n################ RSA Decryption - BOB #################")

            rsaDecryption = RsaDecryption()

            print("\n=> Starting decryption using Public key...")

            # chr(): Converts an ordinal Unicode number of a character to its character representation
            plaintext = [ chr(rsaDecryption.decrypt(c, key_e, key_n)) for c in ciphertext ]
            print("\nDecryption completed. Original plaintext is: ", plaintext)


            # Verify decrypted message matches original plaintext
            if Counter(plaintext) == Counter(inputMessage):
                print("\nVerified decrypted message is correct. RSA completed.")
                sys.exit(1)
            else:
                print("\nERROR: Decrypted message is not correct. Please try again.")
                sys.exit(1)

menu()
