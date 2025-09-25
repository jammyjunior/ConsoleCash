from assets import addCommand
from assets import calculateCommand
from assets import listCommand
from assets import updateCommand
from assets import removeCommand
from assets import sysCommand


def newCommand():
    return input("\033[1;32;40mconsole@consolecash:~$ \033[0m").strip().split()


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
        if len(consoleInput) == 1:
            if consoleInput[0] in ("a", "add"):
                addCommand.addCommand()

            elif consoleInput[0] in ("h", "help"):
                sysCommand.helpCommand()

            elif consoleInput[0] in ("clear", "cls"):
                sysCommand.clearCommand()

            elif consoleInput[0] in ("c", "calculate"):
                calculateCommand.calculateCommand()

            elif consoleInput[0] in ("l", "list", "ls"):
                listCommand.listCommand()

            elif consoleInput[0] in ("u", "update"):
                updateCommand.updateCommand()

            elif consoleInput[0] in ("r", "remove"):
                removeCommand.removeCommand()

            else:
                print("Unknown Command!")

        elif len(consoleInput) > 1:
            if consoleInput[0] in ("a", "add"):
                addCommand.addCommandAdvanced(consoleInput)
            elif consoleInput[0] in ("u", "update"):
                print("hello") 
            elif consoleInput[0] in ("r", "remove"):
                removeCommand.removeAllCommand()
            else:
                print("Unknown Command!")
    
    consoleInput = newCommand()

sysCommand.exitCommand()   #while consoleInput in ("e", "exit")




# ConsoleCash - Made by JammyJunior

