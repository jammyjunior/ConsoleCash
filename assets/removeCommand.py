from assets import itemData

def removeCommand():
    itemNameInput = input("Item name to remove: ")
    if itemNameInput in itemData.itemDict:
        itemData.itemDict.pop(itemNameInput)
        print(f"Removed {itemNameInput}")

    else:
        print(f"{itemNameInput} item not found! Nothing was changed.")


def removeCommandAdvanced(consoleInput):
    itemNameInput = " ".join(consoleInput[1:])

    if itemNameInput in itemData.itemDict:
        itemData.itemDict.pop(itemNameInput)
        print(f"Removed {itemNameInput}")

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
        print("Please ensure your input is in the correct format, then try again. Type 'help' for help.")