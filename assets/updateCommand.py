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
    itemPriceInput, itemQuantityInput = addCommand.addItemValuesCheck()
    if itemPriceInput or itemQuantityInput is None:   # If validation failed, stop here
        return

    addCommand.addItem(itemNameInput, itemPriceInput, itemQuantityInput)
    print("Updated", itemNameInput)




# Update command mostly uses the addCommand scripts

