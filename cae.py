import eel

eel.init("web")


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

    eel.disp(res)


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
        res = "Invalid cipher input!"

    eel.disp(res)


eel.start("c_index.html")
