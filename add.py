class Add:

    # Function to take input for to-do item and priority level
    def addInput():
        item = input("What would you like to add to the list?: ")
        priority = input("How much of a priority is this (high/medium/low)?: ")
        return item, priority

    # Function to check if priority input is valid
    def priorityVerify(priority):
        priorityValid = False
        while priorityValid == False:
                if priority == "high" or priority == "medium" or priority == "low":
                    priorityValid = True
                else:
                    priority = input("Please enter a valid priority level (high/medium/low): ")
        return priority

    # Function to add item to the list
    def addItem(list, item, priority):
         list.update(((item, priority),))
         print("Item successfully added to your to-do list!")
         return list