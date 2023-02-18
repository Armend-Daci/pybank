from bank.accounts import *


def initialmenu():
    print("What would you like to do? 1- Log in. 2- Create a new account.")
    decision = int(input(""))

    accounttype = "T"

    if decision == 1:
        num = -1
        accountnum = -1

        while num == -1 and accountnum < 10000:
            accountnum = int(input("What is your account number?"))
            pwd = input("What is your password?")
            num = login(b.data, accountnum, pwd)  # login function provides element in array of account

        user = {}
        user = b.data[num]
        print(user)
        #type = finder(list, num, accountnum)  # finder checks for if you have a C, S or B
        #print(list)
        amount = 0
        # print(list.getBank().getBalance())
        """
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
        """

        if type == "B":
            viewer(list, num, type)
        elif type == "C":
            viewer(list, num, type)
        elif type == "S":
            viewer(list, num, type)

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
                accountnum = accountcreator(b.data, accounttype)

                check = Checking(deposit)
                bank = Bank(accountnum, check, None)
                customer = (fname, lname, pwd, bank)

                list.append(customer)
                print(
                    f"Success {fname} {lname} has created account number {accountnum} with a total balance of {deposit}!")


            elif accounttype == "S":
                accountnum = accountcreator(b.data, accounttype)

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


def accountcreator(list, accounttype):
    first = 10000
    accounts = []

    for key, values in enumerate(list):
        print(key, values)
        accounts.append(values)

    b = True
    try:
        while b is True:
            print(accounts.index(first), first, accounts)
            if first in accounts == False:
                # numbers.index(first) != True:
                b = False
            first += 1
            print(first)
    except ValueError:
        print("test")
    finally:
        print(first)
        return first


def login(data, accountnum, pwd):
    # temp = []
    if accountnum in data and data[accountnum]['password'] == pwd:
        return accountnum
    else:
        print("Account not found!")
        return -1


def finder(list, num, accountnum):
    total = 0
    #print(list[0].getBank().getAccountType)
    for key, values in enumerate(list):
        print(values.getBank().getAccount(), accountnum)
        if values.getBank().getAccount() == accountnum:
            if values.getBank().getAccountType() == "C":
                type = "C"
            else:
                type = "S"
            total += 1
        if total == 2:
            return "B"
    print(type)
    return type


def viewer(list, num, type):
    bankaccount = list[num].getBank()
    dualaccount = ""
    if type == "C":
        print(
            f"Hello {list[num].getFName()} {list[num].getLName()}, the balance for Checking account #{list[num].getBank().getAccount()} is {list[num].getBank().getChecking().getBalance()}")
        choice = input("Would you like to deposit, withdraw, or transfer?").upper()
        checking = bankaccount.getChecking()
    elif type == "S":
        print(
            f"Hello {list[num].getFName()} {list[num].getLName()}, the balance for Savings account #{list[num].getBank().getAccount()} is {list[num].getBank().getSavings().getBalance()}")
        choice = input("Would you like to deposit, withdraw, or transfer?").upper()
        savings = bankaccount.getSavings()
    elif type == "B":
        dualaccount = "A"
        while dualaccount != "C" and dualaccount != "S":
            print(f"Currently using Checking Account#{bankaccount.getAccount()}")
            print("Would you like to switch to your Savings Account?(Y/N)")
            dualaccount = input().upper()
            if dualaccount == "Y":
                dualaccount = "S"
            elif dualaccount == "N":
                dualaccount = "C"

        if dualaccount == "C":
            print(
                f"Hello {list[num].getFName()} {list[num].getLName()}, the balance for Checking account #{list[num].getBank().getAccount()} is {list[num].getBank().getChecking().getBalance()}")
            choice = input("Would you like to deposit, withdraw, or transfer?").upper()
            checking = bankaccount.getChecking()
        elif dualaccount == "S":
            print(
                f"Hello {list[num].getFName()} {list[num].getLName()}, the balance for Checking account #{list[num].getBank().getAccount()} is {list[num].getBank().getChecking().getBalance()}")
            choice = input("Would you like to deposit, withdraw, or transfer?").upper()
            savings = bankaccount.getSavings()

    print(choice)
    if choice == "D" and type == "C" or dualaccount == "C" and type == "B" and choice == "D":
        print("How much would you like to deposit in your Checking Account?")
        print(f"Current Balance: {checking.getBalance()}")
        amount = int(input())
        bankaccount.getChecking().deposit(amount)
    elif choice == "D" and type == "S" or dualaccount == "S" and type == "B":
        print("How much would you like to deposit in your Savings Account?")
        print(f"Current Balance: {savings.getBalance()}")
        amount = int(input())
        bankaccount.getSavings().deposit(amount)
    elif choice == "W" and type == "C" or dualaccount == "C" and type == "B" and choice == "W":
        print("How much would you like to withdraw from your Checking Account?")
        print(f"Current Balance: {checking.getBalance()}")
        run = 0
        while run == 0 or amount - checking.getBalance() > -100:
            run += 1
            amount = int(input())
            checking.withdraw(amount)
            viewer(list, num, type)
            # if list[num].getBalance() - amount < -100:
            #   print("Amount entered is too large! You do not have sufficient funds.")
    elif choice == "W" and type == "S" or dualaccount == "S":
        print("How much would you like to withdraw from your Savings Account?")
        print(f"Current Balance: {savings.getBalance()}")
        run = 0
        while run == 0 or amount - savings.getBalance() > -100:
            run += 1
            amount = int(input())
            savings.withdraw(amount)
            viewer(list, num, type)



if __name__ == '__main__':
    b = Bank()
    initialmenu()

