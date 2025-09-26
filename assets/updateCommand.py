from assets import addCommand
from assets import itemData

def updateCommand():
    itemNameInput = input("Item name to update: ").strip()

    if itemNameInput in itemData.itemDict:
        updateItemValues(itemNameInput)

    else:
        print(f"Can not find the {itemNameInput}." )
        print("Type 'list' to list all exist items, 'add' to add a new item.")
        print("Nothing was changed.")
    return

def updateItemValues(itemNameInput):
    itemValues = addCommand.addItemValuesCheck()
    if itemValues is None:   # If validation failed, stop here
        return
    itemPriceInput, itemQuantityInput = itemValues

    addCommand.addItem(itemNameInput, itemPriceInput, itemQuantityInput)
    print("Updated", itemNameInput)

def updateCommandAdvanced(consoleInput):
    itemNameInput = " ".join(consoleInput[1:-2])
    
    if len(consoleInput) >= 4 and itemNameInput in itemData.itemDict:
        try:
            itemPriceInput = float(consoleInput[-2])
            itemQuantityInput = int(consoleInput[-1])
        except ValueError:
            print("Data type error!")
            print("Nothing was changed.")
            return

        addCommand.addItem(itemNameInput, itemPriceInput, itemQuantityInput)
        print("Updated", itemNameInput)
        return

    else:
        print("Invalid input.")
        print("Please ensure your input is in the correct format, then try again. Type 'h' for help.")
        print("Nothing was changed.")




# Simple update command mostly uses the addCommand scripts

