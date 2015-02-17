__author__ = 'Bill Lee'

import time

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# Car wash: Use a queue for each customer
# While car wash is not busy get a new car to wash
# Otherwise calc how long each car wash was waiting if it
# takes x minutes to wash a car.

class CarWash():

    def __init__(self, numEmployees):
        self.busy = False
        self.timeRemaining = 0
        self.numEmployees = numEmployees

    def busy(self):
        if self.busy.eq(None):
            return False

        else:
            return True

    def startTask(self, newWashTask):

        if self.busy == None:

            self.currentTask = newWashTask

            self.timeRemaining = newWashTask.getServiceTime() * 60 / self.numExployees

    def taskTimeDecrement(self):

        if self.busy != None:
            self.timeRemaining -= 1

        if self.timeRemaining <= 0:
            self.busy = False


class WashTask():

    def __init__(self, serviceName):

        self.serviceType = serviceName
        self.serviceAmountTime = 0
        self.serviceStartTime = time

    def setService(self):

        if self.serviceType == "A":
            self.serviceTime = 20

        elif self.serviceType == "B":
            self.serviceTime = 15

        elif self.serviceType == "C":
            self.serviceTime = 10

        else:
            self.serviceTime = 5

    def getServiceType(self):
        return self.serviceType

    def getServiceTime(self):
        return self.serviceTime

    def waitTime(self, currentTime):

        return currentTime - self.serviceStartTime


def CarWashSim(numEmployees, numSeconds, maxTasksperCustomer, ):
