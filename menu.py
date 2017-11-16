# -*- coding: utf-8 -*-#

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

    print("==========================================================================")
    print("Computer Security Coursework \nPart 1: RSA Algorithm \nby Uyen Le (tle004)")
    print("==========================================================================\n")

    print("Hello Alice! \n\nSuppose you want to send a private message to Bob...\n")
    print("What would you like to say? \n(Note: you can only use alphanumeric characters in your message)\n")
    inputMessage = str(input("Your plaintext message: "))

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
        print ("\nAlice public key (e,n) is: ", alice_pubKey)
        alice_privKey = alice_d, alice_n
        print ("Alice private key (d,n) is: ", alice_privKey)

        ciphertext = [ pow(ord(c), alice_e, alice_n) for c in inputMessage ]
        print("\nEncryption completed. Your ciphertext is: ", ciphertext)

        send = str(input("\nPress S then Enter to send your ciphertext and public key to Bob..."))
        if not send == 's':
            print("\nYou must send your ciphertext to Bob to continue.\n")
            sys.exit(1)
        else:
            print("\n################ RSA Decryption - BOB #################")

            plaintext = [ chr(pow(c, alice_d, alice_n)) for c in ciphertext ]
            print("\nBob's decrypted message is: ", plaintext)

            #Verify decrypted message matches original plaintext
            if (Counter(inputMessage) == Counter(plaintext)):
                print("\nVerified decrypted message is correct. RSA completed.")
                pass
            else:
                print("\nERROR: Decrypted message is not correct. Please try again.")
                sys.exit(1)


    # Convert to binary
    # bin_inputMessage = bin(int.from_bytes(str(inputMessage).encode(), 'big'))
    # bin_ciphertext = bin(int.from_bytes(str(ciphertext).encode(), 'big'))
    # bin_plaintext = bin(int.from_bytes(str(plaintext).encode(), 'big'))

    # print("\n\n################ RSA Interception - CHARLIE ###############")
    # print("\nOh no, Charlie has interceted your communication flow with Bob!")

menu()
