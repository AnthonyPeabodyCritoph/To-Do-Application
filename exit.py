class Exit:

    # Function that asks the user for confirmation before terminating the program
    def terminate():
        a = True
        while a == True:
            confirm = input("Exit the program (y/n)?: ")
            if confirm == "y":
                a, run = False, False
                return run
            elif confirm == "n":
                a, run = False, True
                return run
            else:
                print("Invalid command.")