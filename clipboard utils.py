from java.awt.datatransfer import StringSelection
from java.awt.datatransfer import Clipboard
from java.awt import Toolkit


def setup():
    global toolkit, clipboard

    toolkit = Toolkit.getDefaultToolkit()
    clipboard = toolkit.getSystemClipboard()


def writeText(text):
    setup()
    clipboard.setContents(StringSelection(text), None)


def readText():
    setup()
    from java.awt.datatransfer import DataFlavor

    contents = clipboard.getContents(None)
    return contents.getTransferData(DataFlavor.stringFlavor)


readText()
writeText("test")
