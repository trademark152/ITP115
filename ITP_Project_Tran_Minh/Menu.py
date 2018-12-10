"""
Menu Class
This class makes use of MenuItem objects
This class represents the restaurants's menu
    which contains four different categories of menu items diners can order from
Class variable: MENU_ITEM_TYPES
Instance attributes: menuItemDictionary: a dict containing all the menu items form the menu
    keys are strings rep types of menu items, values are a list of MenuItem objects
"""

from MenuItem import MenuItem

class Menu(object):
    # Class variable
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]

    # Constructor
    def __init__(self, csvFileName): # CSV file that contains info abt the menu items
        # initialize the single instance attribute to an empty dictionary
        self.__menuItemDictionary = {}

        # Open and read the csv file
        # Import CSV file:
        fileIn = open(csvFileName, "r")
        delimiter = ","

        # Create a blank list containing all objects
        allItems = []

        # Create objects out of CSV file
        for line in fileIn:
            line = line.strip()  # remove junks

            # create a list containing info of each item in the CSV
            eachItemInfo = line.split(delimiter)

            # create an object using MenuItem (name, type, price, desc)
            eachItem = MenuItem(eachItemInfo[0], eachItemInfo[1], eachItemInfo[2], eachItemInfo[3])

            # append items to list
            # self.__menuItemDictionary[eachItemInfo[1]] = eachItem
            allItems.append(eachItem)

        # Close the file
        fileIn.close()

        # append items to the menu, using its type as the key
        # each menu type will have a list of values-objects
        for item in allItems:
            if item.getType() not in self.__menuItemDictionary:
                # append the new item to the existing menu type
                self.__menuItemDictionary[item.getType()] = [item]
            else:
                # create a new menu type in this slot
                self.__menuItemDictionary[item.getType()].append(item)

    # getMenuItemType:
    # inputs are a STRING (a type of menu)
    # return all MenuItem objects in that type
    def getMenu(self, menuItemType):
        if menuItemType in Menu.MENU_ITEM_TYPES:
            return self.__menuItemDictionary[menuItemType]
        else:
            return "Menu Item Type not valid"

    # getMenuItem
    # inputs are a STRING (a type of menu)
    # and an INT (index position of a menu item in the object list of each menu type)
    # return a MenuItem object from the dict
    def getMenuItem(self, menuItemType, idx):
        if menuItemType in Menu.MENU_ITEM_TYPES:
            return self.__menuItemDictionary[menuItemType][idx-1]
        else:
            return "Menu Item Type not valid"

    # printMenuItemsByType
    # input is a STRING (a type of menu item, one of the four listed)
    # return none
    def printMenuItemsByType(self, menuItemType):
        # check to make sure input is valid
        if menuItemType in Menu.MENU_ITEM_TYPES:
            # print a header with the type of menu items
            print("----" + menuItemType.capitalize() + "----")

            # for numbering purposes
            num = 0

            # loop through items in each menu type and print info
            for item in self.__menuItemDictionary[menuItemType]:
                num += 1
                print(str(num) + ") " + str(item))

        else:
            return "Menu Item Type not valid"

    # getNumMenuItemsByType
    # inputs are a STRING (a type of menu item, one of the four listed)
    # return an int representing the number of MenuItems of the input type
    def getNumMenuItemsByType(self, menuItemType):
        if menuItemType in Menu.MENU_ITEM_TYPES:
            return len(self.__menuItemDictionary[menuItemType])
        else:
            return "Menu Item Type not valid"

    # Print message
    def __str__(self):
        keyList = list(self.__menuItemDictionary.keys())
        objectList = list(self.__menuItemDictionary.values())
        msg = str(keyList)
        for objects in objectList:
            for object in objects:
                msg += " \n" + str(object.getName())
        return msg