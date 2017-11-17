# -*- coding: utf-8 -*-#

import textwrap
from collections import Counter
from encryption import *
from decryption import *


def menu():

    regexStr = re.compile("^[a-zA-Z0-9,.].*$")

    print (textwrap.dedent("""
        ==========================================================================
        Computer Security Coursework
        Part 1: RSA Algorithm
        by Uyen Le (tle004)
        ==========================================================================
    """))

    print("Hello Alice! \nSuppose you want to send a private message to Bob. What would you like to say?")
    print("\n(Only alphanumeric characters are allowed)\n")
    inputMessage = str(input("Your message: "))

    if not inputMessage:
        print("ERROR: Please enter a message.")
        sys.exit(1)
    # Validate input using regular expression
    # only alphanumeric characters are allowed
    elif not(regexStr.match(inputMessage)):
        print("\nSorry, only alphanumeric characters allowed. Please try again.")
        sys.exit(1)
    else:

        print("\n################ RSA Encryption - ALICE ###############")

        encryption = Encryption()

        # Randomly generate keys p and q between 0 and 100
        key_p = encryption.generateRandKey()
        key_q = encryption.generateRandKey()
        print('p is:', key_p)
        print('q is:', key_q)

        # Verify p an q are primes
        if encryption.isPrime(key_p): print("Verified p is prime!")
        else:
            print("ERROR: p is not prime. Please try again.")
            sys.exit(1)

        if encryption.isPrime(key_q): print("Verified q is prime!")
        else:
            print("ERROR: q is not prime. Please try again.")
            sys.exit(1)


        # Caluculate key n
        key_n = encryption.calculateN(key_p, key_q)
        print("\nn is:", str(key_p), "*", str(key_q), "=", key_n)

        # Calculate phi(n)
        phiN = encryption.totient(key_p, key_q)
        print("phi(n) is: (", str(key_p), "-1) * (", str(key_q), "-1) =", phiN)

        # Generate key e
        # by adding all coprime numbers to phi(n) to a list
        # then randomly pick a number in that list
        coPrimeList = []

        for i in range(1, phiN):
            if(encryption.isCoPrime([i, phiN])):
                coPrimeList.append(i)

        key_e = coPrimeList[random.randint(coPrimeList[0], len(coPrimeList)-1)]
        print("\ne is: ", key_e)

        # Verify e is coprime to phiN
        if gcd(key_e,phiN) == 1:
            print("Verified e is coprime!")
        else:
            print("ERROR: E is not coprime. Please try again.")
            sys.exit(1)

        # Generate key d using Extended Euclidean algorithm
        # key_d is a private variable
        _, __key_d, _ = encryption.egcd(key_e, phiN)

        # ensure key d is positive
        if __key_d < 0:
            __key_d = __key_d % phiN

        print("\nd is: ", __key_d)

        # verify d is coprime to phiN
        if gcd(__key_d,phiN) == 1:
            print("Verified d is coprime!")
        else:
            print("ERROR: D is not coprime. Please try again.")
            sys.exit(1)

        # Public and private keys
        publicKey = key_e, key_n
        print ("\nPublic key is: ", publicKey)
        __privateKey = __key_d, key_n
        print ("Private key is: ", __privateKey)
        print("\n(!) You can now publish your public key, however your private key must be kept private!")


        print("\n=> Starting encryption using Private key...")
        ciphertext = [ pow(ord(c), __key_d, key_n) for c in inputMessage ]
        print("\nEncryption completed. Your ciphertext is: ", ciphertext)

        # TO DO:
        # ciphertext = [ encryption.encrypt(ord(c), __key_d, key_n) for c in inputMessage ]

        send = str(input("\nPress S then Enter to send your ciphertext to Bob: "))
        if not send == 's':
            print("\nYou must send your ciphertext to Bob to continue.\n")
            sys.exit(1)
        else:

            print("\n################ RSA Decryption - BOB #################")

            decryption = Decryption()

            print("\n=> Starting decryption using Public key...")
            plaintext = [ chr(pow(c, key_e, key_n)) for c in ciphertext ]
            print("\nDecryption completed. Original plaintext is: ", plaintext)

            # TO DO
            # plaintext = [ chr(decryption.decrypt(c, key_e, key_n)) for c in ciphertext ]

            #Verify decrypted message matches original plaintext
            if Counter(inputMessage) == Counter(plaintext):
                print("\nVerified decrypted message is correct. RSA completed.")
                sys.exit(1)
            else:
                print("\nERROR: Decrypted message is not correct. Please try again.")
                sys.exit(1)

menu()
