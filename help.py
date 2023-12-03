class Help:

    # Function that iterates over the list of commands and prints them
    def helper():
        commands = ("/list: View your to-do list.", "/add: Add an item.", "/edit: Edit an item.", "/remove: Remove an item.",
                        "/clear: Clear the list.", "/exit: Exit the program.")
        for command in commands:
            print(command)