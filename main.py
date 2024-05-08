from task import greet, menu, showToday, idTrack, addTask, showTask

def main():

    greet()

    seq = 0
    tasklyst = []
    idlyst = []
        
    flag_menu = True
    while (flag_menu != False):

        action = menu()
        if action == 1:
            showToday()
        
        elif action == 2:

            flag_add = True
            while( flag_add != False):

                seq += 1
                idlyst = idTrack(seq, idlyst)
                tasklyst = addTask(seq, tasklyst)

                add = int(input("Keep adding task? Yes: 1, No: 2 >"))

                if add == 1:
                    flag_add = True
                
                else:
                    flag_add = False       
        
        elif action == 3:
            showTask(tasklyst)

        elif action == 4:
            flag_menu = False

        else:
            print("Invalid action, please try again!")

        print()


if __name__ == "__main__":
    main()