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
    itemUpdateValues = addCommand.addItemValues()
    if itemUpdateValues is None:   # If validation failed, stop here
        return
    
    itemName = itemNameInput
    itemPrice, itemQuantity = itemUpdateValues

    addCommand.addItem(itemName, itemPrice, itemQuantity)
    print("Updated", itemNameInput)




# Update command mostly uses the addCommand scripts

