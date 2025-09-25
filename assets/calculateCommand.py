from assets import itemData

def calculateCommand():
    print("Items in register:\n")
    print("{:<35} {:<10} {:<10} {:<10}".format("Name", "Price", "Quantity", "Amount"))
    print("-" * 65)
    
    for itemName, (itemPrice, itemQuantity, itemTotal) in itemData.itemDict.items():
        print("{:<35} {:<10.2f} {:<10} {:<10}".format(itemName, itemPrice, itemQuantity, itemTotal))

    print()
    itemTotalAll = 0
    for itemName, (itemPrice, itemQuantity, itemTotal) in itemData.itemDict.items():
        itemTotalAll+=itemTotal

    print("Total: {:.2f} $".format(itemTotalAll))
    return