class Clear:

    # Function that asks user for confirmation and then clears the list
    def clearList(list):
            a = True
            while a == True:
                confirm = input("Clear the list (y/n)?: ")
                if confirm == "y":
                    a = False
                    list.clear()
                elif confirm == "n":
                    a = False
                else:
                    print("Invalid command.")
                return list
