"""
ITP 115, SP17 Final project
Run this file in order to start the restaurant simulation program
"""
import datetime
import time

# TODO 0: uncomment the following 3 import statements when you create these files
from Menu import Menu
from Waiter import Waiter
from RestaurantHelper import RestaurantHelper

# Graphical user interface
from tkinter import *
from Application import Application

def main():
    RESTAURANT_NAME = "VietFamily"  # TODO 1: add your own restaurant name in the quotes
    restaurantTime = datetime.datetime(2017, 5, 1, 5, 0)

    # Create the menu object
    menu = Menu("menu.csv")  # TODO 2: uncomment this once the Menu class is implemented

    # Test the menu object
    # print(menu.getMenuItem("Dessert", 0))
    # print(menu.printMenuItemsByType("Entree"))
    # print(menu.getNumMenuItemsByType("Dessert"))
    # print(menu)

    # create the waiter object using the created Menu we just created
    waiter = Waiter(menu)  # TODO 4: uncomment this one the Waiter class is implemented

    print("Welcome to " + RESTAURANT_NAME + "!")
    print(RESTAURANT_NAME + " is now open for dinner.\n")
    #
    for i in range(21):
        print("\n~~~ It is currently", restaurantTime.strftime("%H:%M PM"), "~~~")
        restaurantTime += datetime.timedelta(minutes=15)

        # TODO 3: uncomment the following 3 lines once the Diner class is implemented
        potentialDiner = RestaurantHelper.randomDinerGenerator()
        if potentialDiner is not None:
            print(
                "\n" + potentialDiner.getName() + " welcome, please be seated!")  # we have a diner to add to the waiter's list of diners

            # TODO 4: uncomment the following 2 lines once the Waiter class is implemented
            waiter.addDiner(potentialDiner)
        waiter.advanceDiners()
        time.sleep(2)

    print("\n~~~ ", RESTAURANT_NAME, "is now closed. ~~~")

    # After the restaurant is closed, progress any diners until everyone has left
    # TODO 5: uncomment the following 5 lines once the Waiter class is implemented
    while waiter.getNumDiners():
        print("\n~~~ It is currently", restaurantTime.strftime("%H:%M PM"), "~~~")
        restaurantTime += datetime.timedelta(minutes=15)
        waiter.advanceDiners()
        time.sleep(2)

    print("Goodbye!")


main()
