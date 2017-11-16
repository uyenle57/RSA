# -*- coding: utf-8 -*-#

import textwrap
from rsa_functions import *


def letter_to_int(letter):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    return alphabet.index(letter) + 1

def menu():

    # print(pow(3,5,7))
    # print(pow(4,2,12))
    # print(pow(9,3,50))
    # print(pow(5,2,19))
    # print(pow(33,2,125))
    # print(pow(5,9,11))
    # print(pow(4,4,22))
    # print(pow(9,8,7))
    # print(pow(2,4,20))
    #
    # print("-----")
    # print(modular_exp(3,5,7))
    # print(modular_exp(4,2,12))
    # print(modular_exp(9,3,50))
    # print(modular_exp(5,2,19))
    # print(modular_exp(33,2,125))
    # print(modular_exp(5,9,11))
    # print(modular_exp(4,4,22))
    # print(modular_exp(9,8,7))
    # print(modular_exp(2,4,20))


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

        # START RSA ENCRYPTION

        print("\n################ RSA Encryption - ALICE ###############")

        # Randomly generate keys p and q between 0 and 100
        alice_p = generateRandKey()
        alice_q = generateRandKey()
        print('p is:', alice_p)
        print('q is:', alice_q)

        # Caluculate key n
        alice_n = calculateN(alice_p, alice_q)
        print("n is:", str(alice_p), "*", str(alice_q), "=", alice_n)

        # Calculate phi(n)
        phiN = totient(alice_p, alice_q)
        print("phi(n) is: (", str(alice_p), "-1) * (", str(alice_q), "-1) =", phiN)

        # Generate key e
        # by adding all coprime numbers to phi(n) to a list
        # then randomly pick a number in that list
        coPrimeList = []

        for i in range(1, phiN):
            if(isCoPrime([i, phiN])):
                coPrimeList.append(i)

        alice_e = coPrimeList[random.randint(coPrimeList[0], len(coPrimeList)-1)]
        print("\ne is: ", alice_e)

        # Verify d is coprime to phiN
        if gcd(alice_e,phiN) == 1:
            print("Verified e is coprime!")
        else:
            print("ERROR: E is not coprime. Please try again.")
            sys.exit(1)

        # Generate key d using Extended Euclidean algorithm
        _, alice_d, _ = egcd(alice_e, phiN)

        # ensure key d is positive
        if alice_d < 0:
            alice_d = alice_d % phiN

        print("\nd is: ", alice_d)

        # verify d is coprime to phiN
        if gcd(alice_d,phiN) == 1:
            print("Verified d is coprime!")
        else:
            print("ERROR: D is not coprime. Please try again.")
            sys.exit(1)

        # Alice's public and private keys
        alice_pubKey = alice_e, alice_n
        print ("\nAlice public key is: ", alice_pubKey)
        alice_privKey = alice_d, alice_n
        print ("Alice private key is: ", alice_privKey)

        ciphertext = [ pow(ord(c), alice_e, alice_n) for c in inputMessage ]
        print("\nEncryption completed. Your ciphertext is: ", ciphertext)

        send = str(input("\nPress S then Enter to send your ciphertext to Bob..."))
        if not send == 's':
            print("\nYou must send your ciphertext to Bob to continue.\n")
            sys.exit(1)
        else:

            # START RSA DECRYPTION

            print("\n################ RSA Decryption - BOB #################")

            plaintext = [ chr(pow(c, alice_d, alice_n)) for c in ciphertext ]
            print("\nDecryption completed. Original plaintext is: ", plaintext)

            #Verify decrypted message matches original plaintext
            if Counter(inputMessage) == Counter(plaintext):
                print("\nVerified decrypted message is correct. RSA completed.")
                pass
            else:
                print("\nERROR: Decrypted message is not correct. Please try again.")
                sys.exit(1)

menu()
