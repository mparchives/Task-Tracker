from task import greet, menu, showToday, addTask, showTask, editTask, removeTask, noTask

def main():

    greet()

    seq = 0        #count amount of tasks
    tasklyst = []  #store ongoing task objects 
    archived = []  #store archived task objects
    flag_menu = True

    while (flag_menu != False):

        action = menu()

        #1. Show Today's Date
        if action == 1:
            showToday()

        #2. Show Tasks
        elif action == 2:

            #Check if there's task on the list
            taskFlag = noTask(tasklyst)
            if taskFlag == True:
                print("You have no task now.")

            else:
                showTask(tasklyst)
        
        #3. Add Task to the List
        elif action == 3:

            flag_add = True
            while( flag_add != False):

                seq += 1
                temp = addTask(seq)
                tasklyst.append(temp)

                add = int(input("Keep adding task? Yes: 1, No: 2 >"))

                if add == 1:
                    flag_add = True
                
                else:
                    flag_add = False       
        
        #4. Edit Task on the List
        elif action == 4:

            #Check if there's task on the list
            taskFlag = noTask(tasklyst)
            if taskFlag == True:
                print("You have no task now.")

            else:

                editNum = int(input("Which task would you like to edit? >"))
                if editNum <=0 or editNum > seq:
                    print("Out of range!")

                else:
                    temp = addTask(editNum)
                    tasklyst = editTask(editNum, temp, tasklyst)

        #5. Remove Task on the List
        elif action == 5:

            #Check if there's task on the list
            taskFlag = noTask(tasklyst)
            if taskFlag == True:
                print("You have no task now.")

            else:

                editNum = int(input("Which task would you like to edit? >"))
                if editNum <=0 or editNum > seq:
                    print("Out of range!")

                else:

                    for i in range(len(tasklyst)):
                        if i == editNum-1:
                            archived.append(tasklyst[i])
                    
                    tasklyst = removeTask(editNum, tasklyst)


        elif action == 6:
            
            #Check if there's task on the list
            taskFlag = noTask(archived)
            if taskFlag == True:
                print("No archived tasks on the list.")

            else:
                showTask(archived)

        #6. End This Program
        elif action == 7:
            flag_menu = False

        else:
            print("Invalid action, please try again!")

        print()


if __name__ == "__main__":
    main()