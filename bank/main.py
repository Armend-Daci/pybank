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
    print(list[0][3].checking.getBalance())
    return list

def initialmenu():

    print("What would you like to do? 1- Log in. 2- Create a new account.")
    decision = int(input(""))

    accounttype = "T"

    if decision == 1:
        num = -1
        accountnum = -1
        """
        while num == -1 and accountnum < 10000:
            accountnum = int(input("What is your account number?"))
            pwd = input("What is your password?")
            num = login(list, accountnum, pwd)
        
        type = finder(list, num, accountnum)
        print(list)
        amount = 0
        print(list[num].getBalance())
        if list[num].isActive() is False and type == "C":
            print(
                f"Please add more money into Checking Account#{list[num].getAccount}, current balance: {list[num].getBalance()}")
            while amount + list[num].getBalance() < 0:
                amount = int(input())
            list[num].Deposit(amount)
            list[num].activate()
            success(list[num])
        elif list[num].isActive() is False and type == "S":
            print(
                f"Please add more money into Savings Account#{list[num].getAccount()}, current balance: {list[num].getBalance()}")
            while amount + list[num].getBalance() < 0:
                amount = int(input())
            list[num].Deposit(amount)
            list[num].activate()
            success(list[num])
        elif list[num].isActive() is False and type == "B" and list[num].accountType() == "C":
            print(
                f"Please add more money into Checking Account#{list[num].getAccount()}, current balance: {list[num].getBalance()}")
            # print(amount, type(list[num].getBalance()))
            while amount + list[num].getBalance() < 0:
                print(f"Please enter a number greater than {list[num].getBalance()}")
                amount = int(input())
            list[num].Deposit(amount)
            list[num].activate()
            success(list[num])
        elif list[num].isActive() is False and type == "B" and list[num].accountType() == "S":
            print(
                f"Please add more money into Savings Account#{list[num].getAccount()}, current balance: {list[num].getBalance()}")
            # print(amount, type(list[num].getBalance()))
            while amount + list[num].getBalance() < 0:
                print(f"Please enter a number greater than {list[num].getBalance()}")
                amount = int(input())
            list[num].Deposit(amount)
            list[num].activate()
            success(list[num])
            # print(f"Please add more money into Savings Account#{list[num].getAccount()}")
        if type == "B":
            viewer(list, num, type)
        elif type == "C":
            viewer(list, num, type)
        elif type == "S":
            viewer(list, num, type)
        """
    elif decision == 2:
        print("Do you have an account? Y/N")
        exists = input().upper()
        if exists == "N":
            fname = input("What is your first name?")
            lname = input("What is your last name?")
            pwd = input("Please enter your password.")
            deposit = -1
            while accounttype != "C" and accounttype != "S" and deposit < 0:
                accounttype = (input("What type of account would you like to create C/S?")).upper()
                deposit = int(input("How much would you like to deposit?"))

            if accounttype == "C":
                accountnum = accountcreator(list)

                check = Checking(deposit)
                bank = Bank(accountnum, check, None)
                customer = (fname, lname, pwd, bank)

                list.append(customer)
                print(
                    f"Success {fname} {lname} has created account number {accountnum} with a total balance of {deposit}!")


            elif accounttype == "S":
                accountnum = accountcreator(list)

                savings = Savings(deposit)
                bank = Bank(accountnum, None, savings)
                customer = (fname, lname, pwd, bank)

                list.append(customer)
                print(
                    f"Success {fname} {lname} has created account number {accountnum} with a total balance of {deposit}!")

        """
        elif exists == "Y":
            num = -1
            accountnum = -1
            while num == -1 and accountnum < 10000:
                accountnum = int(input("What is your account number?"))
                pwd = input("What is your password?")
                num = login(list, accountnum, pwd)
            type = finder(list, num, accountnum)
            print(type)
            if type == "C":
                print("How much would you like to deposit into your new Savings Account?")
                deposit = int(input())
                list.append(
                    Savings(list[num].getFName(), list[num].getLName(), list[num].getPassword(), list[num].getAccount(),
                            deposit))
                print(f"Success account#{list[num].getAccount()} now has a Savings Account with a balance of {deposit}")
                print("Taking you to main menu...")
                main()
            elif type == "S":
                print("How much would you like to deposit into your new Checking Account?")
                deposit = int(input())
                list.append(Checking(list[num].getFName(), list[num].getLName(), list[num].getPassword(),
                                     list[num].getAccount(), deposit))
                print(
                    f"Success account#{list[num].getAccount()} now has a Checking Account with a balance of {deposit}")
                print("Taking you to main menu...")
                main()
            elif type == "B":
                print("You already have two accounts!")
                print("Taking you to main menu...")
                main()
                """

def accountcreator(list):
    num = 10000

    return num

if __name__ == '__main__':
    list = initialize()
    initialmenu()
