from assets import addCommand
from assets import calculateCommand
from assets import listCommand
from assets import updateCommand
from assets import removeCommand
from assets import sysCommand

print("""
    #############################
    #                           #
    #        ConsoleCash        #
    #                           #
    #############################
""")
print("Welcome to ConsoleCash! For a new user, type 'help' for help, 'exit' to exit.")

consoleInput = "" #Start with blank to have a new console newCommand()

def newCommand():
    return input("\033[1;32;40mconsole@consolecash:~$ \033[0m").strip()

while consoleInput not in ("e", "exit"):

    if consoleInput == "":
        pass

    elif consoleInput in ("a", "add"):
        addCommand.addCommand()

    elif consoleInput in ("h", "help"):
        sysCommand.helpCommand()

    elif consoleInput in ("clear", "cls"):
        sysCommand.clearCommand()

    elif consoleInput in ("c", "calculate"):
        calculateCommand.calculateCommand()

    elif consoleInput in ("l", "list", "ls"):
        listCommand.listCommand()

    elif consoleInput in ("u", "update"):
        updateCommand.updateCommand()

    elif consoleInput in ("r", "remove"):
        removeCommand.removeCommand()

    elif consoleInput in ("r -a", "r -all", "remove -a", "remove -all"):
        removeCommand.removeAllCommand()

    else:
        print("Unknown Command!")
        
    consoleInput = newCommand()

sysCommand.exitCommand()   #while consoleInput in ("e", "exit")




# ConsoleCash - Made by JammyJunior

