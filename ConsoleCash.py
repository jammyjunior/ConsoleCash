import sys
import os

print("""
    #############################
    #                           #
    #        ConsoleCash        #
    #                           #
    #############################
""")
print("Welcome to ConsoleCash! For a new user, type 'help' for help, 'exit' to exit.")

consoleInput = "" #Start with blank to have a new console newCommand()
itemDict = {}   #Create an empty dictionary

def newCommand():
    return input("\033[1;32;40mconsole@cashregister:$ \033[0m").strip()

def exitCommand():
    print("Exiting...")
    sys.exit(0)

def addCommand():
    itemNameInput = input("Item name: ").strip()    #itemNameInput
    if itemNameInput == "":
        print("Data type error!")
        print("The Item name can't be left empty.")
        print("Nothing was changed.")
        return
    
    elif itemNameInput == "-all":
        print("Invalid name!")
        print("The item's name can't be '-all'. Try a different name.")
        print("Nothing was changed.")
        return

    itemPriceInput = input("Price: ")               #itemPriceInput
    try:
        itemPriceInput = float(itemPriceInput)
    except ValueError:
        print("Data type error!")
        print("Price must be a number (float).")
        print("Nothing was changed.")
        return
    
    itemQuantityInput = input("Quantity: ")         #itemQuantityInput
    try:
        itemQuantityInput = int(itemQuantityInput)
    except ValueError:
        print("Data type error!")
        print("Quantity must be an integer.")
        print("Nothing was changed.")
        return
    
    itemPriceInput = float(itemPriceInput)
    itemQuantityInput = int(itemQuantityInput)
    #Add new item to itemDict
    addItem(itemNameInput, itemPriceInput, itemQuantityInput)
    print("Added", itemNameInput)
    return

def addItem(itemName, itemPrice, itemQuantity):
    itemTotal = itemPrice*itemQuantity  #Save the total per item
    itemDict.update({itemName: [itemPrice, itemQuantity, itemTotal]})

def calculateCommand():
    listCommand()
    itemTotalAll = 0
    for ItemName, (itemPrice, itemQuantity, itemTotal) in itemDict.items():
        itemTotalAll+=itemTotal

    print("Total: {:.2f} $".format(itemTotalAll))
    
def clearCommand():
    if os.name == 'nt': # For Windows
        _ = os.system('cls')
    else:               # For macOS and Linux
        _ = os.system('clear')

def listCommand():
    if not itemDict:  # check if dictionary is empty
        print("No items in the register.")
        print("Type 'add' to add a new item.")
        return
    
    print("Items in register:\n")
    print("{:<35} {:<10} {:<10}".format("Name", "Price", "Quantity"))
    print("-" * 55)
    
    for itemName, (itemPrice, itemQuantity, itemTotal) in itemDict.items():
        print("{:<35} {:<10.2f} {:<10}".format(itemName, itemPrice, itemQuantity))
    print()
    return

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

    """)

def removeCommand():
    removeItem = input("Item name to remove: ")
    if removeItem in itemDict:
        itemDict.pop(removeItem)
        print("Removed", removeItem)

    else:
        print(removeItem, "item not found! Nothing was changed.")

def removeAllCommand():
    removeAllConfirm = input("Are you sure? All your data will be wiped out. (Y/n)").lower().strip()
    if removeAllConfirm in ("y", "yes"):
        itemDict.clear()

    elif removeAllConfirm not in ("n", "no"):
        print("Confirmation failed!")
    
    else:
        print("Nothing was changed.")

while consoleInput not in ("e", "exit"):

    if consoleInput == "":
        pass

    elif consoleInput in ("a", "add"):
        addCommand()

    elif consoleInput in ("h", "help"):
        helpCommand()

    elif consoleInput == "clear":
        clearCommand()

    elif consoleInput in ("c", "calculate"):
        calculateCommand()

    elif consoleInput in ("l", "list"):
        listCommand()

    elif consoleInput in ("r", "remove"):
        removeCommand()

    elif consoleInput in ("r -a", "r -all", "remove -a", "remove -all"):
        removeAllCommand()

    else:
        print("Unknown Command!")
        
    consoleInput = newCommand()

exitCommand()   #while consoleInput in ("e", "exit")





# ConsoleCash - Made by JammyJunior

