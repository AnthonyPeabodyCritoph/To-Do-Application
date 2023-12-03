class Edit:

    # Function that allows the user to choose whether to edit the task (key) or the priority (value)
    def chooseElement():
        editTarget = input("Which element of this entry would you like to edit (task/priority)?: ")
        editTargetValid = False
        while editTargetValid == False:
                if editTarget == "task" or editTarget == "priority":
                    editTargetValid = True
                else:
                    editTarget = input("Please enter a valid element (task/priority): ")
        return editTarget

    # Function that edits the task (key) of the selected item
    def editTask(list, choice):
        task = input("What would you like to change this task to?: ")
        priority = list[choice]
        list.pop(choice)
        list.update(((task, priority),))
        print("Task successfully updated!")
        return list
    