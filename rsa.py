import random
import eel

eel.init("web")


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def modInverse(a, m):  # a= e, m = phi_n, x = d
    m0 = m
    y = 0
    x = 1

    if (m == 1):
        return 0

    while (a > 1):

        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if (x < 0):
        x = x + m0

    return x


def key_gen(p, q):
    n = p*q

    print("n:")
    print(n)

    phi_n = (p-1)*(q-1)

    print("phin:")
    print(phi_n)

    e = random.randrange(1, phi_n)

    while gcd(e, phi_n) != 1:
        e = random.randrange(e, phi_n)

    print("e:")
    print(e)

    d = modInverse(e, phi_n)

    d = int(d)
    print("d: ")
    print(d)

    keys = [[e, n], [d, n]]

    return keys


def rsa_encrypt1(message, p, q, keys):
    mes_hash = []  # mes_hash is the hashed value of message which is basically a string made out of concatenating ascii values of the message characters in sequence

    print(keys)
    for i in message:
        mes_hash.append(ord(i))
    print("Mes_hash:")
    print(mes_hash)

    cipher = []
    ct = ""

    for i in mes_hash:
        temp = (i ** keys[0]) % keys[1]
        cipher.append(temp)
        ct += str(temp)
    print("cipher: ")
    print(cipher)
    print(ct)

    return cipher


def rsa_decrypt1(cipher, p, q, keys):

    print(cipher)

    print(keys)

    decrypted_hash = []
    for x in cipher:
        decrypted_hash.append((x ** keys[0]) % keys[1])
    print(decrypted_hash)

    decrypted_message = ""
    for x in decrypted_hash:
        decrypted_message += (chr(x))

    return decrypted_message


@eel.expose
def rsa_encrypt(msg, keytype=0):
    p = 739
    q = 827
    ke, kd = key_gen(p, q)

    c = rsa_encrypt1(msg, p, q, ke)
    if keytype != 1:
        eel.disp(c)
    if(keytype == 1):
        m = rsa_decrypt1(c, p, q, kd)
        eel.disp(m)


eel.start("c_index.html")
