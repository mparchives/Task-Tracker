
import datetime

class Todo():

    def __init__(self, id = 0, category = "", topic="", descrip = "", deadline = 0, status = 0):
        
        self.__id = id
        self.__category = category
        self.__topic = topic
        self.__descrip = descrip
        self.__deadline = (datetime.date.today() - datetime.timedelta(days=-deadline)).strftime("%m/%d/%y")
        self.__status = status

    #set/get taskID
    def setID(self, taskID):
        self.__id = taskID
    
    def getID(self):
        return self.__id
    
    #set/get category
    def setCateg(self, categ):
        self.__category = categ

    def getCateg(self):
        return self.__category

    #set/get topic
    def setTopic(self, subject):
        self.__topic = subject

    def getTopic(self):
        return self.__topic
    
    #set/get description
    def setDes(self, des):
        self.__descrip = des

    def getDes(self):
        return self.__descrip

    #set/get deadline
    def setDeadline(self, due):
        self.__deadline = due

    def getDeadline(self):
        return self.__deadline

    #set/get status
    def setStatus(self, stat):
        self.__status = stat

    def getStatus(self):
        return self.__status

    def __str__(self):
        return f"{self.__id}. {self.__category} {self.__topic}  {self.__deadline}\n"