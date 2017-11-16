# -*- coding: utf-8 -*-#

from rsa_functions import *


def encryption(plaintext):

    print("\n################ RSA Encryption - ALICE ###############")

    # Generate keys p and q
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
    print ("\nAlice public key is: ", alice_pubKey)
    alice_privKey = alice_d, alice_n
    print ("Alice private key is: ", alice_privKey)


    # TO DO: fix modular_exp!
    # print([ encrypt(ord(c), alice_e, alice_n) for c in inputMessage ])

    ciphertext = [ pow(ord(p), alice_e, alice_n) for p in plaintext ]
    print("Encryption completed. Ciphertext is: ", ciphertext)

    return ciphertext
