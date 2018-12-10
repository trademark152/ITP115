from Menu import Menu
from MenuItem import MenuItem
from Diner import Diner
from Waiter import Waiter

def main():
    # Create the menu object
    menu = Menu("menu.csv")
    print(menu)

    diner1 = Diner("John")
    print(diner1)


    for item in menu.getMenu("Dessert"):
        print(item)
        diner1.setOrder(item)

    diner1.updateStatus()
    print(diner1)
    print(diner1.printOrder())

    for item in diner1.getOrder():
        print(item)

    print(diner1.calculateMealCost())


    diner2 = Diner("Henry")

    waiter = Waiter(menu)
    waiter.addDiner(diner1)
    waiter.addDiner(diner2)

    print(waiter.getNumDiners())

    waiter.printDinerStatuses()

    print(range(5, 1, 1))
main()

# menu = Menu("menu.csv")  # TODO 2: uncomment this once the Menu class is implemented
# print(menu)