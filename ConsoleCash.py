from assets import addCommand
from assets import calculateCommand
from assets import listCommand
from assets import updateCommand
from assets import removeCommand
from assets import sysCommand
from assets import saveCommand
from assets import sessionCommand


def newCommand():
    return input("\033[1;32;40mconsole@consolecash:~\033[0m$ ").strip().split()


print("""
    #############################
    #                           #
    #        ConsoleCash        #
    #                           #
    #############################
""")
print("Welcome to ConsoleCash! For a new user, type 'help' for help, 'exit' to exit.")

consoleInput = newCommand() #Start with blank to have a new console newCommand()

while not consoleInput or consoleInput[0] not in ("e", "exit"):

    if consoleInput == []:
        pass

    else:
        inputCommand = consoleInput[0]

        if len(consoleInput) == 1:
            if inputCommand in ("a", "add"):
                addCommand.addCommand()

            elif inputCommand in ("h", "help"):
                sysCommand.helpCommand()

            elif inputCommand in ("clear", "cls"):
                sysCommand.clearCommand()

            elif inputCommand in ("c", "calculate", "cal"):
                calculateCommand.calculateCommand()

            elif inputCommand in ("l", "list", "ls"):
                listCommand.listCommand()

            elif inputCommand in ("u", "update"):
                updateCommand.updateCommand()

            elif inputCommand in ("r", "remove"):
                removeCommand.removeCommand()

            elif inputCommand in ("s", "save"):
                saveCommand.saveCommand()

            elif inputCommand == "session":
                sessionCommand.sessionIntro()

            else:
                print("Unknown Command!")

        elif len(consoleInput) > 1: #This one is for advanced
            if inputCommand in ("a", "add"):
                addCommand.addCommandAdvanced(consoleInput)

            elif inputCommand in ("u", "update"):
                updateCommand.updateCommandAdvanced(consoleInput) 

            elif inputCommand in ("r", "remove"):
                removeCommand.removeCommandAdvanced(consoleInput)

            elif inputCommand in ("s", "save"):
                saveCommand.saveCommandAdvanced(consoleInput)

            elif inputCommand == "session":
                sessionCommand.sessionNavigator(consoleInput)

            else:
                print("Unknown Command!")

        else:
            print("Unknown Error!")
    
    consoleInput = newCommand()     #Return to get new command

sysCommand.exitCommand()   #while consoleInput in ("e", "exit")




# ConsoleCash - Made by JammyJunior

