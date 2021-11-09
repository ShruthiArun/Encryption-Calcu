//Function to display output
eel.expose(disp_cc)
function disp_cc(x)
{
    var d = document.getElementById("cc")
    d.innerHTML = "  " + x
}

eel.expose(disp_cp)
function disp_cp(x)
{
    var d = document.getElementById("cp")
    d.innerHTML = "  " + x
}

eel.expose(disp_rc4c)
function disp_rc4c(x)
{
    var d = document.getElementById("rc4c")
    d.innerHTML = "  " + x
}

eel.expose(disp_rc4p)
function disp_rc4p(x)
{
    var d = document.getElementById("rc4p")
    d.innerHTML = "  " + x
}

eel.expose(disp_rsac)
function disp_rsac(x)
{
    var d = document.getElementById("rsac")
    d.innerHTML = "  " + x
}

eel.expose(disp_rsap)
function disp_rsap(x)
{
    var d = document.getElementById("rsap")
    d.innerHTML = "  " + x
}




//Caesar Encryption
function enc()
{
    var d = document.getElementById("ptc")
    var k = document.getElementById("keyc")
    eel.c_encrypt(d.value,k.value)
}

//Caesar Decryption
function dec()
{
    var d = document.getElementById("ctc")
    var k = document.getElementById("key2c")
    eel.c_decrypt(d.value,k.value)
}

//RC4 Encryption
function encrc4()
{
    var d = document.getElementById("ptrc4")
    var k = document.getElementById("keyrc4")
    eel.rc4_encrypt(d.value,k.value)
}

//RC4 Decryption
function decrc4()
{
    var d = document.getElementById("ctrc4")
    var k = document.getElementById("key2rc4")
    eel.rc4_decrypt(d.value,k.value)
}


//RSA Encryption and Decryption
function encrsa(keytype)
{
    var d = document.getElementById("ptrsa")
    eel.rsa_encrypt(d.value,keytype)
}




