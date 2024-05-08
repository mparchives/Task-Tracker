from todo import Todo
import datetime

def greet():
    print(f"Welcome back to the task-tracker! Today's date: {(datetime.date.today()).strftime("%m/%d/%y")}")

def menu():
    print("Choose Action:")
    print("1. Print Today's Date")
    print("2. Add Task to the List")
    print("3. Show Tasks")
    print("4. End This Program")
    action = int(input("> "))
    return action

def showToday():
    print(f"Today's date: {(datetime.date.today()).strftime("%m/%d/%y")}")


def idTrack(seq, idlyst):
    idlyst.append(seq)
    return idlyst

def addTask(taskNum, tasklyst):

        
    newCateg = input("Input category for the new task: >")
    newTopic = input("Input topic for the new task: >")
    newDes = input("Input description for the new task: >")
    newdue = int(input("Input number of days from now the task is due: >"))
    newStat = int(input("Input status for the new task: (0/1/2)>"))
    temp = Todo(taskNum, newCateg, newTopic, newDes, newdue, newStat)

    print(temp)
    tasklyst.append(temp)

    return tasklyst


def showTask(tasklyst):

    if len(tasklyst) == 0:
        print("You have no task now.")

    else:
        for i in tasklyst:
            print(i)
