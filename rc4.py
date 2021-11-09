import eel

eel.init("web")


def swap(a, b):
    t = a
    a = b
    b = t


def key_schedule(s, k):
    j = 0
    for i in range(0, 256):
        j = (j+s[i]+k[i]) % 256
        swap(s[i], s[j])

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
    s = set_s()  # Defining S-array

    key_schedule(s, k_array)  # Key schedule funct to get modified s-array

    # Pseudo random generation step to get keystring in decimal format
    kstr = pseudo_random_gen(s, len(pt_ascii))

    kstrbin = list_bin_convert(kstr)  # Converting keytring to binary

    pt_bin = list_bin_convert(pt_ascii)  # Converting message to binary

    ct_bin = xor(pt_bin, kstrbin, len(pt_bin))  # Creating cipher in binary

    # Converting binary cipher to ascii format
    ct_ascii = list_dec_convert(ct_bin)

    ct = ascii_to_string(ct_ascii)  # Convert ascii cipher to ciphertext

    eel.disp(ct)


@eel.expose
def rc4_decrypt(ct, k):
    k_array = key_arr_create(k)  # creating the ascii array of the key string
    ct_ascii = ascii_convert(ct)  # converting cipher text to equivalent ascii
    s = set_s()  # Defining S-array

    key_schedule(s, k_array)  # Key schedule funct to get modified s-array
    kstr = pseudo_random_gen(s, len(ct_ascii))

    kstrbin = list_bin_convert(kstr)  # Converting keytring to binary
    ct_bin = list_bin_convert(ct_ascii)  # Converting message to binary
    pt_bin = xor(ct_bin, kstrbin, len(pt_bin))  # Creating cipher in binary
    # Converting binary cipher to ascii format
    pt_ascii = list_dec_convert(pt_bin)
    pt = ascii_to_string(pt_ascii)  # Convert ascii cipher to ciphertext

    eel.disp(pt)


eel.start("c_index.html")
