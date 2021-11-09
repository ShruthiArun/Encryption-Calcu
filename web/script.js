



function disp()
{
    var e = document.getElementById("ip")
    eel.pyfun(e.value)
}

function addText(text)
{
    var d = document.getElementById("op")
    d.innerHTML += text
}
eel.expose(addText)
