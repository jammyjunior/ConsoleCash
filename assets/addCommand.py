from assets import itemData

def addItem(itemName, itemPrice, itemQuantity):
    itemTotal = itemPrice*itemQuantity  #Save the total per item
    itemData.itemDict.update({itemName: [itemPrice, itemQuantity, itemTotal]})

def addItemValuesCheck():   #This one uses for simple add and update command
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
    
    return itemPriceInput, itemQuantityInput

def addCommand():
    itemNameInput = input("Item name: ").strip()    #itemNameInput
    if itemNameInput in ("-a", "-all"):     #Invalid name: The name is in removeCommand
        print("Invalid name !!!")
        print("Please use other name instead.")
        return
    
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

    itemValues = addItemValuesCheck()
    if itemValues is None:
        return
    itemPriceInput, itemQuantityInput = itemValues

    #Add new item to itemDict
    addItem(itemNameInput, itemPriceInput, itemQuantityInput)
    print("Added", itemNameInput)
    return

def addCommandAdvanced(consoleInput):
    lenConsoleInput = len(consoleInput)
    if lenConsoleInput >= 4:
        itemNameInput = " ".join(consoleInput[1:-2])
        if itemNameInput in ("-a", "-all"):     #Invalid name: The name is in removeCommand
            print("Invalid name !!!")
            print("Please use other name instead.")
            return
        
        elif itemNameInput in itemData.itemDict:
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

        try:
            itemPriceInput = float(consoleInput[-2])
            itemQuantityInput = int(consoleInput[-1])
        except ValueError:
            print("Data type error!")
            print("Nothing was changed.")
            return
        
        addItem(itemNameInput, itemPriceInput, itemQuantityInput)
        print("Added", itemNameInput)
        return

    else:
        print("Invalid input.")
        print("Please ensure your input is in the correct format, then try again. Type 'h' for help.")
        print("Nothing was changed.")

