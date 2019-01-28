#This is the afternoon classwork for Python. It is created to display lists, add and remove
#from lists, and use and call several functions.
def main():  # point of entry
    Project1()
    # listAllTasks()
    # addToList()
    # deleteFromList()
    # quitTheProgram()


# Create a task list. A user is presented with the text below.
# Let them select an option to list all of their tasks, add a
# task to their list, delete a task, or quit the program.
# Make each option a different function in your program. Do NOT use Google.
# Do NOT use other students. Try to do this on your own.

# myTaskList = ["Buy groceries", "Feed the dog.", "Fill gas", "Water flowers"]

#Afternoon CW Python Review Project
myTaskList = []
def Project1():


    userChoice = ""
    while(userChoice != 0):
        userChoice = int(input("What would you like to do next?\n"
                               "Enter 1 to List all tasks.\n"
                               "Enter 2 to Add a task to the list.\n"
                               "Enter 3 to Delete a task from the list.\n"
                               "Enter 0 to quit the program.\n"))
        if (userChoice == 1):
            listAllTasks()
        elif (userChoice == 2):
            addToList()
        elif (userChoice == 3):
            deleteFromList()
        elif (userChoice == 0):
            quitTheProgram()
            break

# myTaskList = ["Buy grocercies", "Feed the dog.", "Fill gas", "Water flowers"]

#prints the list
def listAllTasks():
    print(myTaskList)
#adds items to list
def addToList():
    userAdd = input("What do you want to add?\n")
    myTaskList.append(userAdd)
    print(myTaskList)
#deletes items from list
def deleteFromList():
    userRemove = input("What to you want to remove?\n")
    myTaskList.remove(userRemove)
    print(myTaskList)

#lets user quit program
def quitTheProgram():
    print("You have chosen to quit")



    #listAllTasks()
    #addToList()
    #deleteFromList()
    #quitTheProgram()


if __name__ == '__main__':
    main()
