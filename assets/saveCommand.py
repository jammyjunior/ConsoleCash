import os
from assets import calculateCommand

def saveFile (saveFileName):
    try:
        with open(saveFileName, "w") as sf:
            sf.write(calculateCommand.calculateCommand())

        print(f"[\033[32mOK\033[0m] File {saveFileName} was saved successfully!")

        saveFileNamePath = os.path.abspath(saveFileName)
        print(f"Path to your file: {saveFileNamePath}")

    except:
        print("[\033[31mFAILED\033[0m] Failed to save file!")
        print("Report at: https://github.com/jammyjunior/ConsoleCash")

def saveCommand():
    inputFileName = input("File name: ").replace(" ", "_")
    saveFileName = f"{inputFileName}.txt"
    saveFile(saveFileName)

def saveCommandAdvanced(consoleInput):
    inputFileName = "_".join(consoleInput[1:])
    saveFileName = f"{inputFileName}.txt"
    saveFile(saveFileName)

    