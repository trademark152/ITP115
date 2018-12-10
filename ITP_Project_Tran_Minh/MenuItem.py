"""
MenuItem Class
This class represents a single item that a diner can order from the restaurant's menu
Instance attributes: (private) name (STRING), type (STRING), price (FLOAT), description (STRING)
Instance methods: init, str, getter, setter
"""

class MenuItem(object):
    # Constructor
    def __init__(self, name, type, price, description):
        self.__name = name
        self.__type = type
        self.__price = price
        self.__description = description

    # Setter and getter methods
    def getType(self):
        return self.__type

    def setType(self, type):
        self.__type = type

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getPrice(self):
        return float(self.__price)

    def setPrice(self, price):
        self.__price = price

    def getDescription(self):
        return self.__description

    def setDescription(self, description):
        self.__description = description

    # Print message
    def __str__(self):
        msg = self.__name + " (" + self.__type + "): $" + str(self.__price)
        msg += "\n\t" + self.__description
        return msg
