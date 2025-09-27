from assets import itemData
from pathlib import Path
import json

currentSessionName = None   #For currentSession

def sessionIntro():
    print("Welcome to the session feature in ConsoleCash.")
    print("With sessions, you can save your work, switch between multiple sessions, and improve your workflow.")
    print("Learn more about sessions: https://github.com/jammyjunior/ConsoleCash")

def sessionNavigator(consoleInput):
    assetsDir = Path(__file__).resolve().parent
    sessionDir = assetsDir / "sessions"
    sessionDir.mkdir(exist_ok=True)     # Check if the dir is not exist, create a new one

    lenConsoleInput = len(consoleInput)
    sessionCommand = consoleInput[1]

    if lenConsoleInput == 2:
        if sessionCommand in ("c", "create"):
            createSession(sessionDir)

        elif sessionCommand in ("co", "checkout"):
            checkoutSession(sessionDir)

        elif sessionCommand == "current":
            currentSession()

        elif sessionCommand in ("d", "del", "delete"):
            deleteSession(sessionDir)

        elif sessionCommand in ("h", "help"):
            sessionIntro()

        elif sessionCommand in ("l", "ls", "list"):
            listSession(sessionDir)

        elif sessionCommand in ("s", "save", "commit"):
            saveSession(sessionDir)

        else:
            print("Unknown command!")

    else:
        print("Unknown command!")

def createSession(sessionDir):
    inputSessionName = input("Session name: ").replace(" ", "_")
    newSessionName = sessionDir / inputSessionName

    if newSessionName.exists():
        print(f"[\033[31mFAILED\033[0m] {inputSessionName} already exists. Please choose another name.")
        return
    else:
        try:
            sessionBlankData = {}
            with open(newSessionName, "w") as sf:
                json.dump(sessionBlankData, sf, indent=4)

            print(f"[\033[32mOK\033[0m] Session {inputSessionName} was created successfully!")

        except Exception as e:
            print(f"[\033[31mFAILED\033[0m] Error: {e}")
            print("Report at: https://github.com/jammyjunior/ConsoleCash")


def checkoutSession(sessionDir):
    global currentSessionName   #For currentSession
    inputSessionName = input("Session name: ")
    checkoutSessionName = sessionDir / inputSessionName
    if checkoutSessionName.exists():
        try:
            with open(checkoutSessionName, "r") as sd:
                sessionData = json.load(sd)
            itemData.itemDict = sessionData     #Copy data from sessionData to itemData, no write to itemData
            currentSessionName = inputSessionName   #Return currentSessionName to use for currentSession 
            print(f"[\033[32mOK\033[0m] Switched to: {currentSessionName}")

        except Exception as e:
            print(f"[\033[31mFAILED\033[0m] Error: {e}")
            print("Report at: https://github.com/jammyjunior/ConsoleCash")

        currentSessionName = inputSessionName   #Return currentSessionName to use for currentSession    
    
    else:
        print(f"[\033[31mFAILED\033[0m] Error: Can't found session named {inputSessionName}")


def currentSession():
    global currentSessionName
    if currentSessionName is None:
        print("No session is currently checked out.")
    else:
        print(f"Current session: {currentSessionName}")
        
    
def listSession(sessionDir):
    global currentSessionName
    try:
        sessionList = [f.name for f in sessionDir.iterdir() if f.is_file()]
        if sessionList:
            print("Sessions list:")
            for sn in sessionList:    
                if sn == currentSessionName:
                    print(f"> \033[32m{sn}\033[0m")
                else:    
                    print(f"  {sn}")

        else:
            print("No session was found. Type 'session create' to create a new one")

    except Exception as e:
            print(f"[\033[31mFAILED\033[0m] Error: {e}")
            print("Report at: https://github.com/jammyjunior/ConsoleCash")


def deleteSession(sessionDir):
    inputSessionName = input("Session name: ")
    deleteSessionName = sessionDir / inputSessionName

    if deleteSessionName.exists():
        try:
            deleteSessionName.unlink()
            print(f"[\033[32mOK\033[0m] {inputSessionName} has been deleted.")
        except Exception as e:
            print(f"[\033[31mFAILED\033[0m] Error: {e}")
            print("Report at: https://github.com/jammyjunior/ConsoleCash")
    
    else:
        print(f"[\033[31mFAILED\033[0m] {inputSessionName} does not exist. Type 'session list' to list all exist sessions.")


def saveSession(sessionDir):
    global currentSessionName
    if currentSessionName is None:
        inputSessionName = input("Session name :")
        saveSessionName = sessionDir / inputSessionName
        try:
            with open(saveSessionName, "w") as ssw:
                json.dump(itemData.itemDict, ssw, indent=4)
            print(f"[\033[32mOK\033[0m] Saved to: {inputSessionName}") 

        except Exception as e:
            print(f"[\033[31mFAILED\033[0m] Error: {e}")
            print("Report at: https://github.com/jammyjunior/ConsoleCash")  

    else:
        saveSessionName = sessionDir / currentSessionName
        if saveSessionName.exists():
            try:
                with open(saveSessionName, "w") as ssw:
                    json.dump(itemData.itemDict, ssw, indent=4)
                print(f"[\033[32mOK\033[0m] Saved to: {currentSessionName}") 

            except Exception as e:
                print(f"[\033[31mFAILED\033[0m] Error: {e}")
                print("Report at: https://github.com/jammyjunior/ConsoleCash")  
    
        else:
            print(f"[\033[31mFAILED\033[0m] Error: {e}")
            print("Report at: https://github.com/jammyjunior/ConsoleCash") 
