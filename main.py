from exit import Exit
from help import Help
from listPrint import ListPrint
from add import Add
from remove import Remove
from edit import Edit
from clear import Clear

run = True
list = {}
print("Welcome to your to-do list! What would you like to do?\nHint: /help gives you all the commands you can use.")

# Primary loop that manages the user interface using the above commands
while run == True:
    process = input("Please enter a command: ")
    match process:
        case "/help":
            Help.helper()
        case "/list":
            ListPrint.printList(list)
        case "/add":
            item, priority = Add.addInput()
            priority = Add.priorityVerify(priority)
            list = Add.addItem(list, item, priority)
        case "/edit":
            operation = "edit"
            ListPrint.printList(list)
            choice = Remove.selectRemovalItem(list, operation)
            editTarget = Edit.chooseElement()
            if editTarget == "task":
                list = Edit.editTask(list, choice)
            elif editTarget == "priority":
                priority = input("What would you like to change the priority to (high/medium/low)?: ")
                priority = Add.priorityVerify(priority)
                list[choice] = priority
                print("Priority successfully updated!")
        case "/remove":
            operation = "remove"
            ListPrint.printList(list)
            choice = Remove.selectRemovalItem(list, operation)
            list = Remove.removeItem(list, choice)
        case "/clear":
            list = Clear.clearList(list)
        case "/exit":
            run = Exit.terminate()
        case _:
            print("Invalid command.")