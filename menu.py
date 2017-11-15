# -*- coding: utf-8 -*-#

import os, sys
import re
from rsa_functions import *

def letter_to_int(letter):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    return alphabet.index(letter) + 1

def menu():

    # Call the rsa_functions.py script
    os.system('python3 rsa_functions.py')

    regexStr = re.compile("^[a-zA-Z,.].*$")


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
    elif not(regexStr.match(inputMessage)):
        print("\nSorry, only alphabetic characters allowed. Please try again.")
        return
    #If all above is passed, start the crytosystem
    else:
        print("\nStarting RSA cryptosystem...\n")

        # Generate keys p and q
        key_p = generateRandKey()
        key_q = generateRandKey()
        print('p is:', key_p)
        print('q is:', key_q)

        # Caluculate key n
        key_n = calculateN(key_q, key_p)
        print("\nn is:", str(key_p), "*", str(key_q), "=", key_n)

        # Calculate phi(n)
        phiN = totient(key_q, key_p)
        print("\nphi(n) is: (", str(key_p), "-1) * (", str(key_q), "-1) =", phiN)

        # Generate key e
        coPrimeList = []

        for i in range(1, phiN):
            if(isCoPrime([i, phiN])):
                coPrimeList.append(i)

        key_e = coPrimeList[random.randint(coPrimeList[0], len(coPrimeList)-1)]
        print("\ne is: ", key_e)

        # Verify d is coprime to phiN
        if(gcd(key_e,phiN) == 1):
            print("Verified e is coprime!")
        else:
            print("E is not coprime.")
            sys.exit(1)

        # Generate key d
        _, key_d, _ = egcd(key_e, phiN)

        # ensure key d is positive
        if key_d < 0:
            key_d = key_d % phiN

        print("d is: ", key_d)

        # verify d is coprime to phiN
        if(gcd(key_d,phiN) == 1):
            print("Verified d is coprime!")
        else:
            print("D is not coprime.")
            sys.exit(1)

        print ("\nYour public key (e,n) is: ", (key_e,key_n))
        print ("Your private key (d,n) is: ", (key_d,key_n))


        print(modular_exp(2,1,2))
        print(modular_exp(2,2,3))
        print(modular_exp(2,3,4))
        print(modular_exp(2,4,5))
        print(modular_exp(2,5,6))
        print(modular_exp(2,6,7))
        print(modular_exp(11,13,19))

        print(pow(2,1,2))
        print(pow(2,2,3))
        print(pow(2,3,4))
        print(pow(2,4,5))
        print(pow(2,5,6))
        print(pow(2,6,7))
        print(pow(11,13,19))

        # Encryption
        print("\n-------------------------------------------------")
        print("Using your public key, we can now start encprypting your input message:")



        # ciphertext = [ pow(letter_to_int(c), key_e, key_n) for c in inputMessage ]
        # print("Ciphertext: ", ciphertext)
        # print("plaintext: ", [pow(c, key_d, key_n) for c in ciphertext ])

        # print("Your Communication diagram now looks like this:")
menu()
