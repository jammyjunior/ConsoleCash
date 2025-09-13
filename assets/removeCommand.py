from assets import itemData

def removeCommand():
    removeItem = input("Item name to remove: ")
    if removeItem in itemData.itemDict:
        itemData.itemDict.pop(removeItem)
        print("Removed", removeItem)

    else:
        print(removeItem, "item not found! Nothing was changed.")


def removeAllCommand():
    removeAllAuth = input("Are you sure? All your data will be wiped out. (Y/n)").lower().strip()
    if removeAllAuth in ("y", "yes"):
        itemData.itemDict.clear()

    elif removeAllAuth in ("n", "no"):
        print("Nothing was changed.")
    
    else:
        print("Authentication failed!")
        print("Nothing was changed.")