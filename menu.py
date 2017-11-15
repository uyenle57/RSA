# -*- coding: utf-8 -*-#

import os, sys, re
from collections import Counter
from rsa_functions import *


def letter_to_int(letter):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    return alphabet.index(letter) + 1

def menu():

    # Call the rsa_functions.py script
    os.system('python3 rsa_functions.py')

    # regexStr = re.compile("^[a-zA-Z,.].*$")

    print("==========================================================================")
    print("Computer Security Coursework \nPart 1: RSA Algorithm \nby Uyen Le (tle004)")
    print("==========================================================================\n")

    print("Hello Alice! \n\nSuppose you want to send a private message to Bob...\n")
    print("What would you like to say? \n(Note: you can only use alphanumeric characters in your message)\n")
    inputMessage = str(input("Your plaintext message: "))

    #Input message cannot be empty
    if not inputMessage:
        print("ERROR: Please enter a message.")
        sys.exit(1)
    # Validate input using regular expression
    # only alphanumeric characters are allowed
    # elif not(regexStr.match(inputMessage)):
    #     print("\nSorry, only alphabetic characters allowed. Please try again.")
    #     sys.exit(1)
    #If all above is passed, start the crytosystem
    else:
        print("\nStarting RSA cryptosystem...\n")

        # Generate keys p and q
        alice_p = generateRandKey()
        alice_q = generateRandKey()
        print('p is:', alice_p)
        print('q is:', alice_q)

        # Caluculate key n
        alice_n = calculateN(alice_p, alice_q)
        print("\nn is:", str(alice_p), "*", str(alice_q), "=", alice_n)

        # Calculate phi(n)
        phiN = totient(alice_p, alice_q)
        print("\nphi(n) is: (", str(alice_p), "-1) * (", str(alice_q), "-1) =", phiN)

        # Generate key e
        coPrimeList = []

        for i in range(1, phiN):
            if(isCoPrime([i, phiN])):
                coPrimeList.append(i)

        alice_e = coPrimeList[random.randint(coPrimeList[0], len(coPrimeList)-1)]
        print("\ne is: ", alice_e)

        # Verify d is coprime to phiN
        if(gcd(alice_e,phiN) == 1):
            print("Verified e is coprime!")
        else:
            print("E is not coprime.")
            sys.exit(1)

        # Generate key d
        _, alice_d, _ = egcd(alice_e, phiN)

        # ensure key d is positive
        if alice_d < 0:
            alice_d = alice_d % phiN

        print("d is: ", alice_d)

        # verify d is coprime to phiN
        if(gcd(alice_d,phiN) == 1):
            print("Verified d is coprime!")
        else:
            print("D is not coprime.")
            sys.exit(1)

        # Alice's public and private keys
        alice_pubKey = alice_e, alice_n
        print ("\nYour public key (e,n) is: ", alice_pubKey)
        alice_privKey = alice_d, alice_n
        print ("Your private key (d,n) is: ", alice_privKey)

        # Encryption
        print("\n################ RSA Encryption ###############")

        # TO DO: fix modular_exp!
        # print([ encrypt(ord(c), alice_e, alice_n) for c in inputMessage ])

        ciphertext = [ pow(ord(c), alice_e, alice_n) for c in inputMessage ]
        print("Your ciphertext is: ", ciphertext)

        send = str(input("\nPress S then Enter to send your ciphertext and public key to Bob..."))
        if not send == 's':
            print("\nYou must send your ciphertext to Bob to continue.\n")
            sys.exit(1)
        else:
            print("\n################ RSA Decryption ###############")
            print("Bob starts decrypting your ciphertext...")
            # plaintext = [ chr(pow(c, alice_d, alice_n)) for c in ciphertext ]
            plaintext = [ chr(pow(c, alice_d, alice_n)) for c in ciphertext ]
            print("\nBob's decrypted message is: ", plaintext)

            #Verify decrypted message matches original plaintext
            if (Counter(inputMessage) == Counter(plaintext)):
                print("\nVerified message matches Alice's input message. RSA cryptosystem completed.")
                pass
            else:
                print("Not matched!")
                sys.exit(1)

menu()
