#this is just a test module

class Task():

    def __init__(self, id=0, topic = ""):
        self.__id = id
        self.__topic = topic

    #set/get taskID
    def setID(self, taskID):
        self.__id = taskID
    
    def getID(self):
        return self.__id
    
    #set/get topic
    def setTopic(self, topics):
        self.__topic = topics

    def getTopic(self):
        return self.__topic
    
    def __str__(self):
        return f"{self.__id}.  {self.__topic}\n"