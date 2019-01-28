def main():
    myTaskList = ["Buy grocercies", "Feed the dog.", "Fill gas", "Water flowers"]
    userChoice = int(input("What would you like to do next? "
                           "Enter 1 to List all tasks. "
                           "Enter 2 to Add a task to the list. "
                           "Enter 3 to Delete a task from the list. "
                           "Enter 0 to quit the program."))

    while (userChoice != 0):
        print(userChoice)
    if(userChoice == 1):
        print(myTaskList)
    if(userChoice == 2):
        myTaskList.append("xyz")
        print(myTaskList)
    if(userChoice == 3):
        myTaskList.remove("xyz")
        print(myTaskList)
    if (userChoice == 0):
        print ("stop")


if __name__ == '__main__':
    main()
