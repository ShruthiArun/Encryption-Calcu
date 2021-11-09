import eel

eel.init("web")


@eel.expose
def pyfun(text):
    print("The text is : " + text)
    eel.addText("yotoashdgashdcbasudv")


eel.start("index.html")
