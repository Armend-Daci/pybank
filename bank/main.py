from bank.accounts import *

def initialize():
    list = []
    check1 = Checking(8000)
    bank1 = Bank(10000, check1, None)
    customer1 = ("Armend", "Daci", "1", bank1)

    check2 = Checking(6000)
    bank2 = Bank(10000, check2, None)
    customer2 = ("Mersim", "Daci", "1", bank2)

    check3 = Checking(1000)
    bank3 = Bank(10000, check3, None)
    customer3 = ("John", "Wick", "1", bank3)

    check4 = Checking(84000)
    bank4 = Bank(10000, check4, None)
    customer4 = ("Arny", "Schwartz", "1", bank4)

    check5 = Checking(4700)
    bank5 = Bank(10000, check5, None)
    customer5 = ("Melvin", "Donovan", "1", bank5)

    list.append(customer1)
    list.append(customer2)
    list.append(customer3)
    list.append(customer4)
    list.append(customer5)
    print(list)

if __name__ == '__main__':
    initialize()
