from assets import itemData

def listCommand():
    if not itemData.itemDict:  # check if dictionary is empty
        print("No items in the register.")
        print("Type 'add' to add a new item.")
        return
    
    print("Items in register:\n")
    print("{:<35} {:<10} {:<10}".format("Name", "Price", "Quantity"))
    print("-" * 55)
    
    for itemName, (itemPrice, itemQuantity, itemTotal) in itemData.itemDict.items():
        print("{:<35} {:<10.2f} {:<10}".format(itemName, itemPrice, itemQuantity))
    print()
    return