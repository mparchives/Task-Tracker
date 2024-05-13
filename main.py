from todo import Todo
#Function for Display
from task import greet, menu, showToday, showTask
#Function for Boolean
from task import noTask
#Function for Adding
from task import idTracker, addTask, addArchives
#Function for Editing
from task import editTask
#Function for Removing
from task import removeID



def main():

    greet()

    seq = 4            #count amount of tasks
    idLyst = []        #store ongoing task id numbers
    tasklyst = []      #store ongoing task objects 
    archivelyst = []   #store archived task objects
    flag_menu = True


    ###test data###
    test1 = Todo(1, "business", "fund", "$30K", 30, 0)
    test2 = Todo(2, "personal", "shopping", "dress", 3, 1)
    test3 = Todo(3, "drama", "repair", "roof", 2, 1)
    test4 = Todo(4, "personal", "grocery", "", 1, 0)
    
    idLyst.append(1)
    idLyst.append(2)
    idLyst.append(3)
    idLyst.append(4)

    tasklyst.append(test1)
    tasklyst.append(test2)
    tasklyst.append(test3)
    tasklyst.append(test4)
    ###---------###

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
                idLyst = idTracker(seq, idLyst)
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

                removeNum = int(input("Which task would you like to edit? >"))
                if removeNum >= 1 and removeNum <= seq:

                    removeSeq = removeID(removeNum, idLyst)
                    print(removeSeq)
                    temp = addArchives(removeSeq, tasklyst, archivelyst)
                    showTask(archivelyst)
                    #tasklyst = removeTask(removeSeq, tasklyst)
                    tasklyst.remove(temp)

                else:

                    print("Out of range!")


        elif action == 6:
            
            #Check if there's task on the list
            taskFlag = noTask(archivelyst)
            if taskFlag == True:
                print("No archived tasks on the list.")

            else:
                showTask(archivelyst)

        #6. End This Program
        elif action == 7:
            flag_menu = False

        else:
            print("Invalid action, please try again!")

        print()


if __name__ == "__main__":
    main()