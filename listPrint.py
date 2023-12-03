class ListPrint:

    # Function to check the to-do list's length and print its contents
    def printList(list):
        if len(list) == 0:
            print("Your to-do list is currently empty, you can add an item with /add.")
        else:
            itemNumber = 0
            for item in list:
                itemNumber = itemNumber + 1
                print("{}: {} - {}".format(itemNumber, item, list[item]))