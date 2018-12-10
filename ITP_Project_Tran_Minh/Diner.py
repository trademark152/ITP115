"""
Diner Class
This class represents one of the diners at the restaurant
    and keep tracks of their status and meal
This class makes use of MenuItem objects
Class variable: STATUSES
Instance attributes: name, order status
"""

from MenuItem import MenuItem

class Diner(object):
    # Class variable:
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]

    # Constructor
    def __init__(self, name):
        self.__name = name
        # set the diner's order attribute to an empty list
        self.__order = []
        # set the diner's status to 0, meaning "seated"
        self.__status = 0

    # Setter and getter methods
    def getOrder(self):
        return self.__order

    def setOrder(self, order):
        self.__order.append(order)

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.__status = status

    def updateStatus(self):
        self.__status += 1

    def printOrder(self):
        print(self.__name + " ordered: ")
        # print the message containing all the menu items the diner ordered
        for item in self.__order:
            print("-", end=" ")
            print(item)

    def calculateMealCost(self):
        # return a float representing the total cost of diner's meal
        totalCost = 0
        for item in self.__order:
            totalCost += item.getPrice()
        return totalCost

    # Print message
    def __str__(self):
        msg = "Diner " + self.__name + " is currently "
        msg += Diner.STATUSES[self.__status]
        return msg
