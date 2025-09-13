from assets import itemData
from assets import listCommand

def calculateCommand():
    listCommand.listCommand()
    itemTotalAll = 0
    for ItemName, (itemPrice, itemQuantity, itemTotal) in itemData.itemDict.items():
        itemTotalAll+=itemTotal

    print("Total: {:.2f} $".format(itemTotalAll))
    return