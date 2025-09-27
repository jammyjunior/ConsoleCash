from assets import itemData

def listCommand():
    if not itemData.itemDict:  # check if dictionary is empty
        print("No items in the register.")
        print("Type 'add' to add a new item.")
        return
    
    listOutput = []
    listOutput.append("Items in register:\n")
    listOutput.append("{:<35} {:<10} {:<10}".format("Name", "Price", "Quantity"))
    listOutput.append("-" * 65)
    
    for itemName, (itemPrice, itemQuantity, _) in itemData.itemDict.items():
        listOutput.append("{:<35} {:<10.2f} {:<10}".format(itemName, itemPrice, itemQuantity))

    print( "\n".join(listOutput))
    print()
    return