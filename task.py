from todo import Todo
import datetime

def greet():
    print(f"Welcome back to the task-tracker! Today's date: {(datetime.date.today()).strftime("%m/%d/%y")}")

def menu():
    print("Choose Action:")
    print("1. Show Today's Date")
    print("2. Show Tasks")
    print("3. Add Task to the List")
    print("4. Edit Task on the List")
    print("5. Remove Task on the List")
    print("6. View Archieved Task")
    print("7. End This Program")
    action = int(input("> "))
    return action

def showToday():
    print(f"Today's date: {(datetime.date.today()).strftime("%m/%d/%y")}")

def showTask(tasklyst):

    for i in tasklyst:
        print(i)

def addTask(taskNum):

    newCateg = input("Input category for the new task: >")
    newTopic = input("Input topic for the new task: >")
    newDes = input("Input description for the new task: >")
    newdue = int(input("Input number of days from now the task is due: >"))
    newStat = int(input("Input status for the new task: (0/1/2)>"))
    temps = Todo(taskNum, newCateg, newTopic, newDes, newdue, newStat)

    print(temps)
    return temps


def editTask(editNum, newTemp, tasklyst):

    for i in range(len(tasklyst)):
        if i == editNum-1:
            tasklyst[i] = newTemp

    return tasklyst


#Need repair
def removeTask(editNum, tasklyst):
    
    if editNum == len(tasklyst):
        
        tasklyst.pop()
        return tasklyst
    
    else:
        for i in range(len(tasklyst)):
            
            if i >= editNum-1 and i < len(tasklyst)-1:
                tasklyst[i] = tasklyst[i+1]

        tasklyst.pop()

        return tasklyst


def noTask(tasklyst):

    if len(tasklyst) == 0:
        return True
    
    else:
        return False