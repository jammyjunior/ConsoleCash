from assets import itemData

def removeCommand():
    removeItem = input("Item name to remove: ")
    if removeItem in itemData.itemDict:
        itemData.itemDict.pop(removeItem)
        print("Removed", removeItem)

    else:
        print(removeItem, "item not found! Nothing was changed.")


def removeCommandAdvanced(consoleInput):
    lenConsoleInput = len(consoleInput)
    itemNameInput = " ".join(consoleInput[1:-2])

    if itemNameInput in itemData.itemDict:
        itemData.itemDict.pop(itemNameInput)

    elif itemNameInput in ("-a", "-all"):
        removeAllAuth = input("Are you sure? All your data will be wiped out. (Y/n)").lower().strip()
        if removeAllAuth in ("y", "yes"):
            itemData.itemDict.clear()

        elif removeAllAuth in ("n", "no"):
            print("Nothing was changed.")
    
        else:
            print("Authentication failed!")
            print("Nothing was changed.")

    else:
        print("Item not found!")
        print("Please ensure your input is in the correct format, then try again. Type 'h' for help.")