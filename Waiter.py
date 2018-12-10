"""
Waiter Class
This class represents the restaurant's waiter. The waiter maintains a list of the diners
    it is currently taking care of, and progresses them through the different stages
    of the restaurant. The waiter repeats multiple cycles of attending to the diners.
    In each cycle, the waiter will seat a new diner, take order if needed and give diners the bill
    according to each diner's status
This class makes use of Menu and Diner objects
Class variable: STATUSES
Instance attributes: name, order status
"""

from Menu import Menu
from Diner import Diner
# Graphical user interface
from tkinter import *
from Application import Application

class Waiter(object):
    # Constructor
    def __init__(self, menu):
        # a Menu object representing the restaurant's menu
        self.__menu = menu
        # a list of Diner objects the waiter is attending to
        self.__diners = []

    def addDiner(self, diner):
        # add the new Diner object to the waiter's list of diners:
        self.__diners.append(diner)

    def getNumDiners(self):
        # return the number of diners the waiter is currently keeping track of
        return len(self.__diners)

    def printDinerStatuses(self):
        # print all the diners the waiter is keeping track of, grouped by their statuses

        # # create an empty dictionary to catalog diner and status
        # catalogDiner = {}
        #
        # # loop through each diner
        # for diner in self.__diners:
        #     # extract diner's status and add it to dictionary
        #     if diner.getStatus() not in catalogDiner:
        #         # add new status as key
        #         catalogDiner[diner.getStatus()] = [diner]
        #         # if status exists, append
        #     else:
        #         catalogDiner[diner.getStatus()].append(diner)

        # loop through possible statuses:
        for status in Diner.STATUSES:
            print("Diners who are " + status + ":")
            # loop through each diner
            for diner in self.__diners:
                if Diner.STATUSES[diner.getStatus()] == status.lower():
                    # print("\t" + diner.getName())
                    print("\t", diner)


    def takeOrders(self):
        # loop through diner and check if diner's status is "ordering"
        for diner in self.__diners:
            if Diner.STATUSES[diner.getStatus()] == "ordering":

                # for each diner that is ordering, loop through the different menu type
                numOrder = 0

                for type in Menu.MENU_ITEM_TYPES:

                    # with each menu type, print the menu items of that type
                    self.__menu.printMenuItemsByType(type)

                    # ask the diner to order a menu item
                    print()
                    userChoice = int(input(diner.getName() + ", please select a " + type + " menu item number? (select a number) "))
                    print()

                    # Error checking
                    while userChoice <= 0 or userChoice > self.__menu.getNumMenuItemsByType(type):
                        userChoice = int(input("Invalid choice. " + diner.getName() + ", please select a " + type + " menu item number? (select a number)"))
                        print()

                    # After the diner selected a menu item, add the item to the diner:
                    diner.setOrder(self.__menu.getMenuItem(type, userChoice))
                    numOrder += 1

                # make sure each diner must order exactly one item of each type
                if numOrder == len(Menu.MENU_ITEM_TYPES):
                    # Once the diner orders one menu item of each type, print the diner's order
                    diner.printOrder()
                else:
                    print(diner.getName() + " did not order enough items")
                    break




    def ringUpDiners(self):
        # loop through the list of diners and check if diner's status is "Paying"
        for diner in self.__diners:
            if Diner.STATUSES[diner.getStatus()] == "paying":
                # Calculate the meal cost:
                diner.calculateMealCost()

                # Print it out a message to the diner
                print()
                print(diner.getName(), end=", ")
                print("Your meal cost $" + str(diner.calculateMealCost()))
                print()

    def removeDoneDiners(self):
        # loop through the list of diners and check if diner's status is "leaving"
        for diner in self.__diners:
            if Diner.STATUSES[diner.getStatus()] == "leaving":
                # Print a thank you message to the diner
                print()
                print(diner.getName() + ", thank you for dining with us! Coma again soon!")
                print()
                # remove the "leaving" diners
                self.__diners.remove(diner)

    def advanceDiners(self):
        # this method allows the waiter to attend to the diners at their various srages
        # as well as move each diner on to the next stage
        print()
        self.printDinerStatuses()
        print()
        self.takeOrders()
        print()
        self.ringUpDiners()
        print()
        self.removeDoneDiners()
        print()
        # update each diner's status
        for diner in self.__diners:
            diner.updateStatus()