import sys
import os

def clearCommand():
    if os.name == 'nt': # For Windows
        _ = os.system('cls')
    else:               # For macOS and Linux
        _ = os.system('clear')
    return

def exitCommand():
    print("Exiting...")
    sys.exit(0)

def helpCommand():
    print("""
    'add'         : Add a new item
    'calculate'   : Calculate the total check
    'clear'       : Clear the console
    'exit'        : Exit the console
    'help'        : Show help
    'list'        : List all items
    'remove'      : Remove an item by name
    'remove -all' : Remove all items from the register
    For more infomation about ConsoleCash, go to https://github.com/jammyjunior/ConsoleCash.
    """)
    return
