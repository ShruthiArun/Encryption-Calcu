import random
import eel

eel.init("web")

"""________________________Caesar Cipher______________________________________"""


def checkip(pt):
    flag = 0
    for i in pt:
        if ord(i) < 32 or ord(i) > 126:
            #print("Invalid input!")
            flag = 1
            break
    return flag


def check_key(n):
    if n >= 0 and n <= 100:
        flag = 0
    else:
        flag = 1
    return flag


@eel.expose
def c_encrypt(a, n):
    res = ""
    n = int(n)
    f = checkip(a)
    if f == 0:
        f = check_key(n)
        if f == 0:
            c = ""
            for i in a:
                if i == " ":
                    c += i
                elif ord(i) >= 65 and ord(i) <= 90:
                    c += chr((((ord(i)-65)+n) % 26)+65)
                elif ord(i) >= 97 and ord(i) <= 122:
                    c += chr((((ord(i)-97)+n) % 26)+97)
                elif ord(i) >= 32 and ord(i) <= 64:
                    c += chr((((ord(i)-32)+n) % 34)+32)
                elif ord(i) >= 91 and ord(i) <= 96:
                    c += chr((((ord(i)-91)+n) % 6)+91)
                elif ord(i) >= 123 and ord(i) <= 126:
                    c += chr((((ord(i)-123)+n) % 4)+123)
            res = c
        else:
            res = "Invalid key!"
    else:
        res = "Invalid plain text input!"

    eel.disp_cc(res)


@eel.expose
def c_decrypt(a, n):
    res = ""
    n = int(n)
    f = checkip(a)
    if f == 0:
        f = check_key(n)
        if f == 0:
            c = ""
            for i in a:
                if i == " ":
                    c += i
                elif ord(i) >= 65 and ord(i) <= 90:
                    c += chr((((ord(i)-65)-n) % 26)+65)
                elif ord(i) >= 97 and ord(i) <= 122:
                    c += chr((((ord(i)-97)-n) % 26)+97)
                elif ord(i) >= 32 and ord(i) <= 64:
                    c += chr((((ord(i)-32)-n) % 34)+32)
                elif ord(i) >= 91 and ord(i) <= 96:
                    c += chr((((ord(i)-91)-n) % 6)+91)
                elif ord(i) >= 123 and ord(i) <= 126:
                    c += chr((((ord(i)-123)-n) % 4)+123)
            res = c
        else:
            res = "Invalid key!"
    else:
        res = "Invalid cipher input!"

    eel.disp_cp(res)


"""__________________Starting of RC4 Encryption_______________________________-"""


def key_schedule(s, k):
    j = 0
    for i in range(0, 256):
        j = (j+s[i]+k[i]) % 256
        t = s[i]
        s[i] = s[j]
        s[j] = t
    print(s)

    return s


def pseudo_random_gen(s, ptlen):
    kstr = []
    i = j = 0
    for i in range(i+1, ptlen+1):
        j = (j + s[i]) % 256
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        t = (s[i] + s[j]) % 256
        kstr.append(s[t])
    return kstr


def set_s():
    s = []
    for i in range(0, 256):
        s.append(i)
    return s


def ascii_convert(a):
    res = []
    for x in a:
        res.append(ord(x))
    return res


def key_arr_create(k):
    if len(k) < 256:  # len(s) is 256 here
        a = []
        q = int(256/len(k))

        r = 256 % len(k)

        for i in range(q):
            for x in k:
                a.append(ord(x))

        if r != 0:
            for x in k:
                if r != 0:
                    a.append(ord(x))
                else:
                    break
                r -= 1

        return a


def bin_convert(a):
    b = bin(a)
    b1 = b[2:]

    if len(b1) < 8:
        zeroes = ""
        diff = 8-len(b1)
        for i in range(diff):
            zeroes += str(0)
        b1 = zeroes + b1

    else:
        pass
    return b1


def list_bin_convert(a):
    bin_list = []
    for x in a:
        bin_list.append(bin_convert(x))
    return bin_list


def dec_convert(a):
    x = int(a, 2)
    return x


def list_dec_convert(a):
    dec_list = []
    for x in a:
        dec_list.append(dec_convert(x))
    return dec_list


def xor(a, b, arrlen):
    cipher_bin_list = []
    for i in range(0, arrlen):
        x = a[i]
        y = b[i]
        res = ""
        for j in range(8):
            res += str(int(x[j]) ^ int(y[j]))
        cipher_bin_list.append(res)
    return cipher_bin_list


def ascii_to_string(a):
    res = ""
    for x in a:
        res += chr(x)
    return res


@eel.expose
def rc4_encrypt(message, k):
    k_array = key_arr_create(k)  # creating the ascii array of the key string
    print(k_array)
    # converting message chars to equivalent ascii list
    pt_ascii = ascii_convert(message)
    print(pt_ascii)
    s = set_s()  # Defining S-array
    # print(s)

    s1 = key_schedule(s, k_array)  # Key schedule funct to get modified s-array

    # Pseudo random generation step to get keystring in decimal format
    kstr = pseudo_random_gen(s1, len(pt_ascii))
    print(kstr)
    kstrbin = list_bin_convert(kstr)  # Converting keytring to binary
    print(kstrbin)
    pt_bin = list_bin_convert(pt_ascii)  # Converting message to binary
    print(pt_bin)
    ct_bin = xor(pt_bin, kstrbin, len(pt_bin))  # Creating cipher in binary
    print(ct_bin)
    # Converting binary cipher to ascii format
    ct_ascii = list_dec_convert(ct_bin)
    print(ct_ascii)
    ct = ascii_to_string(ct_ascii)  # Convert ascii cipher to ciphertext
    print(ct)
    eel.disp_rc4c(ct)
    return ct


@eel.expose
def rc4_decrypt(ct, k):
    k_array = key_arr_create(k)  # creating the ascii array of the key string
    ct_ascii = ascii_convert(ct)  # converting cipher text to equivalent ascii
    s = set_s()  # Defining S-array

    key_schedule(s, k_array)  # Key schedule funct to get modified s-array
    kstr = pseudo_random_gen(s, len(ct_ascii))

    kstrbin = list_bin_convert(kstr)  # Converting keytring to binary
    ct_bin = list_bin_convert(ct_ascii)  # Converting message to binary
    pt_bin = xor(ct_bin, kstrbin, len(ct_bin))  # Creating cipher in binary
    # Converting binary cipher to ascii format
    pt_ascii = list_dec_convert(pt_bin)
    pt = ascii_to_string(pt_ascii)  # Convert ascii cipher to ciphertext
    print(pt)
    eel.disp_rc4p(pt)


"""_______________________________________RSA Encryption____________________________________"""


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
        eel.disp_rsac(c)
    if(keytype == 1):
        m = rsa_decrypt1(c, p, q, kd)
        eel.disp_rsap(m)


eel.start("c_index.html")
