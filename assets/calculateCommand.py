from assets import itemData

def calculateCommand():
    CalculatedOutput = []
    CalculatedOutput.append("Items in register:\n")
    CalculatedOutput.append("{:<35} {:<10} {:<10} {:<10}".format("Name", "Price", "Quantity", "Amount"))
    CalculatedOutput.append("-" * 65)
    
    for itemName, (itemPrice, itemQuantity, itemTotal) in itemData.itemDict.items():
        CalculatedOutput.append("{:<35} {:<10.2f} {:<10} {:<10}".format(itemName, itemPrice, itemQuantity, itemTotal))

    itemTotalAll = sum(itemTotal for _, (_, _, itemTotal) in itemData.itemDict.items())
    CalculatedOutput.append(f"\nTotal: {itemTotalAll:.2f} $")

    print( "\n".join(CalculatedOutput))
    print()

    return "\n".join(CalculatedOutput)