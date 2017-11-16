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
    # print(modExp(3,5,7))
    # print(modExp(4,2,12))
    # print(modExp(9,3,50))
    # print(modExp(5,2,19))
    # print(modExp(33,2,125))
    # print(modExp(5,9,11))
    # print(modExp(4,4,22))
    # print(modExp(9,8,7))
    # print(modExp(2,4,20))


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

        # Randomly generate keys p and q between 0 and 100
        key_p = generateRandKey()
        key_q = generateRandKey()
        print('p is:', key_p)
        print('q is:', key_q)

        # Caluculate key n
        key_n = calculateN(key_p, key_q)
        print("n is:", str(key_p), "*", str(key_q), "=", key_n)

        # Calculate phi(n)
        phiN = totient(key_p, key_q)
        print("phi(n) is: (", str(key_p), "-1) * (", str(key_q), "-1) =", phiN)

        # Generate key e
        # by adding all coprime numbers to phi(n) to a list
        # then randomly pick a number in that list
        coPrimeList = []

        for i in range(1, phiN):
            if(isCoPrime([i, phiN])):
                coPrimeList.append(i)

        key_e = coPrimeList[random.randint(coPrimeList[0], len(coPrimeList)-1)]
        print("\ne is: ", key_e)

        # Verify d is coprime to phiN
        if gcd(key_e,phiN) == 1:
            print("Verified e is coprime!")
        else:
            print("ERROR: E is not coprime. Please try again.")
            sys.exit(1)

        # Generate key d using Extended Euclidean algorithm
        _, key_d, _ = egcd(key_e, phiN)

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

        # Public and private keys
        publicKey = key_e, key_n
        print ("\nPublic key is: ", publicKey)
        privateKey = key_d, key_n
        print ("Private key is: ", privateKey)
        print("\n(!) You can now publish your public key, however your private key must be kept private!")

        # RSA Encryption with Private key
        ciphertext = [ pow(ord(c), key_d, key_n) for c in inputMessage ]
        print("\nEncryption completed. Your ciphertext is: ", ciphertext)

        # test = [ modExp(ord(c), key_d, key_n) for c in inputMessage ]
        # print("\ntest ", test)


        send = str(input("\nPress S then Enter to send your ciphertext to Bob: "))
        if not send == 's':
            print("\nYou must send your ciphertext to Bob to continue.\n")
            sys.exit(1)
        else:

            print("\n################ RSA Decryption - BOB #################")

            # RSA Decryption with Public key
            plaintext = [ chr(pow(c, key_e, key_n)) for c in ciphertext ]
            print("\nDecryption completed. Original plaintext is: ", plaintext)

            #Verify decrypted message matches original plaintext
            if Counter(inputMessage) == Counter(plaintext):
                print("\nVerified decrypted message is correct. RSA completed.")
                pass
            else:
                print("\nERROR: Decrypted message is not correct. Please try again.")
                sys.exit(1)

menu()
