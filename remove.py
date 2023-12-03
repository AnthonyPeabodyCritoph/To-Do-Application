class Remove:

    # Function to allow the user to select and confirm they'd like to remove an item from the to-do list
    def selectRemovalItem(list, operation):
        inputValid, selectionValid = False, False
        while inputValid == False:
            try:
                selection = int(input("Please select the number of the item you'd like to {}: ".format(operation)))
                inputValid = True
            except ValueError:
                print("Invalid input, please enter a valid number.")
        while selectionValid == False:
            itemNumber = 0
            for item in list:
                itemNumber = itemNumber + 1
                if itemNumber == selection:
                    choice = item
                    selectionValid = True
                    return choice
            print ("Invalid input, please enter a valid number.")
    
    # Function to process the removal
    def removeItem(list, choice):
        a = False
        while a == False:
            confirm = input("Delete this item (y/n)?: ")
            if confirm == "y":
                list.pop(choice)
                print("Item removed!")
                return list
            elif confirm == "n":
                a = True
                return list
            else:
                print("Invalid command.")