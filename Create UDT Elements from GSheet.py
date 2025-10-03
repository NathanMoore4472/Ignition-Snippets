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


def convertGSheetToArray(text):
    return [line.strip() for line in text.split("\n") if line.strip()]


UDTPath = "[ProductGW]_types_/Staging Area/Control"

template = {
    "name": "TEMPLATE",
    "historyEnabled": False,
    "tagGroup": "Elec 1S",
    "dataType": "Boolean",
    "documentation": {"bindType": "parameter", "binding": "{TagName}"},
    "alarms": [
        {
            "setpointA": 1.0,
            "label": {
                "bindType": "Expression",
                "value": "runScript('General.Alarms.getAlarmLabel', 0, {PathToTag}, {name})",
            },
            "displayPath": {"bindType": "Expression", "value": "{label}"},
            "priority": "High",
            "enabled": True,
            "name": "Alarm",
        }
    ],
    "enabled": False,
    "opcItemPath": {"bindType": "parameter", "binding": "{OPCItemPath}{OPCDeviceName}"},
    "tagType": "AtomicTag",
    "opcServer": {"bindType": "parameter", "binding": "{OPCServer}"},
    "valueSource": "opc",
}

tagsToCreate = ["Open Command", "Close Command", "Manual Mode Command", "Reset Command"]

alarmPriorities = ["Diagnostic", "Diagnostic", "Diagnostic", "Diagnostic"]

MODE = "W"

if MODE == "C":
    writeText(str(convertGSheetToArray(readText())))

if MODE == "W":
    for tag, priority in zip(tagsToCreate, alarmPriorities):
        newTag = EI.sanitize_tree(template)
        newTag["name"] = tag

        if priority == "N/A":
            newTag["alarms"] = []
        else:
            newTag["alarms"][0]["priority"] = priority

        collisionPolicy = "o"

        system.tag.configure(UDTPath, [newTag], collisionPolicy)
