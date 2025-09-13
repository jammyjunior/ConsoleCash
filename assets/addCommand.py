from assets import itemData

def addItem(itemName, itemPrice, itemQuantity):
    itemTotal = itemPrice*itemQuantity  #Save the total per item
    itemData.itemDict.update({itemName: [itemPrice, itemQuantity, itemTotal]})

def addItemValues():
    itemPriceInput = input("Price: ")               #itemPriceInput
    try:
        itemPriceInput = float(itemPriceInput)
    except ValueError:
        print("Data type error!")
        print("Price must be a number (float).")
        print("Nothing was changed.")
        return
    
    itemQuantityInput = input("Quantity: ")         #itemQuantityInput
    try:
        itemQuantityInput = int(itemQuantityInput)
    except ValueError:
        print("Data type error!")
        print("Quantity must be an integer.")
        print("Nothing was changed.")
        return
    
    itemPrice = float(itemPriceInput)
    itemQuantity = int(itemQuantityInput)
    return itemPrice, itemQuantity

def addCommand():
    itemNameInput = input("Item name: ").strip()    #itemNameInput
    if itemNameInput in itemData.itemDict:
        itemUpdateAuth = input("Item does exist. Do you want to update them? (Y/n) ").lower().strip() 
        if itemUpdateAuth in ("y", "yes"):
            pass
        elif itemUpdateAuth in ("n", "no"):
            print("Nothing was changed.")
            return
        else:
            print("Authentication failed!")
            print("Nothing was changed.")
            return

    itemName = itemNameInput
    itemValues = addItemValues()
    if itemValues is None:   # If validation failed, stop here
        return
    itemPrice, itemQuantity = itemValues
    #Add new item to itemDict
    addItem(itemName, itemPrice, itemQuantity)
    print("Added", itemNameInput)
    return

