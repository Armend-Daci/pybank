from bank.accounts import *


def initialmenu():
    print("What would you like to do? 1- Log in. 2- Create a new account.")
    decision = int(input(""))

    accounttype = "T"

    if decision == 1:
        num = -1
        accountnum = -1

        while num == -1 and accountnum < 10000:
            accountnum = float(input("What is your account number?"))
            pwd = input("What is your password?")
            num = login(b.data, accountnum, pwd)  # login function provides element in array of account

        user = {}
        user = b.data[num]


        if b.data[num] == user and "NO_CHECKING" in str(user['checking']):
            accounttype = "S"
        elif b.data[num] == user and "NO_SAVINGS" in str(user['savings']): #'== "NO_SAVINGS":
            accounttype = "C"
            print(1)
        elif b.data[num] == user and user['checking'].getBalance() != "NO_CHECKING" and user['savings'].getBalance() != "NO_SAVINGS":
            accounttype = "B"
        print(str(user['savings']))
        input()
        #type = finder(list, num, accountnum)  # finder checks for if you have a C, S or B
        amount = 0

        print(accounttype)
        if accounttype == "B":
            viewer(user, num, accounttype)
        elif accounttype == "C":
            viewer(user, num, accounttype)
        elif accounttype == "S":
            viewer(user, num, accounttype)

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
                deposit = float(input("How much would you like to deposit?"))

            if accounttype == "C":
                accountnum = accountcreator(b.data, accounttype)
                b.data[accountnum] = {
                        "first_name": fname,
                        "last_name": lname,
                        "password": pwd,
                        "checking": deposit,
                        "savings": "NO_SAVINGS"
                    }
                print(
                    f"Success {fname} {lname} has created a new checking account number {accountnum} with a total balance of {deposit}!")

            elif accounttype == "S":
                accountnum = accountcreator(b.data, accounttype)
                b.data[accountnum] = {
                    "first_name": fname,
                    "last_name": lname,
                    "password": pwd,
                    "checking": "NO_CHECKING",
                    "savings": deposit
                }
                print(
                    f"Success {fname} {lname} has created a new savings account number {accountnum} with a total balance of {deposit}!")


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
                #main()
            elif type == "S":
                print("How much would you like to deposit into your new Checking Account?")
                deposit = int(input())
                list.append(Checking(list[num].getFName(), list[num].getLName(), list[num].getPassword(),
                                     list[num].getAccount(), deposit))
                print(
                    f"Success account#{list[num].getAccount()} now has a Checking Account with a balance of {deposit}")
                print("Taking you to main menu...")
                #main()
            elif type == "B":
                print("You already have two accounts!")
                print("Taking you to main menu...")
                #main()
            initialmenu()


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


def viewer(user, num, type):
    dualaccount = ""
    print(type)

    if type == "C":
        if user['checking'].isActive == False:
            print(f"Your account is currently disabled, please deposit a minimum of ${user['checking'].getBalance()} to reactivate your account.")
            while user['checking'].getBalance() < 0:
                reactivateamount = input(f"Please enter the amount you would like to deposit: (Must be greater than {user['checking'].getBalance()}")
                if reactivateamount >= user['checking'].getBalance():
                    user['checking'].deposit(reactivateamount)
                else:
                    pass
                print("Success, your account has been reactivated!")

        print(
            f"Hello {user['first_name']} {user['last_name']}, the balance for Checking account #{num} is {user['checking'].getBalance()}")
        choice = input("Would you like to deposit, withdraw, or transfer?").upper()

    elif type == "S":
        if user['savings'].isActive == False:
            pass
        print(
            f"Hello {user['first_name']} {user['last_name']}, the balance for Savings account #{num} is {user['savings'].getBalance()}")
        choice = input("Would you like to deposit, withdraw, or transfer?").upper()

    elif type == "B":
        dualaccount = "A"
        while dualaccount != "C" and dualaccount != "S":
            print(f"Currently using Checking Account#{num}")
            print("Would you like to switch to your Savings Account?(Y/N)")
            dualaccount = input().upper()
            if dualaccount == "Y":
                dualaccount = "S"
            elif dualaccount == "N":
                dualaccount = "C"

        if dualaccount == "C":
            print(
                f"Hello {user['first_name']} {user['last_name']}, the balance for Checking account #{num} is {user['checking'].getBalance()}")
            choice = input("Would you like to deposit, withdraw, or transfer?").upper()
            checking = user['checking']
        elif dualaccount == "S":
            print(
                f"Hello {list[num].getFName()} {list[num].getLName()}, the balance for Checking account #{list[num].getBank().getAccount()} is {list[num].getBank().getChecking().getBalance()}")
            choice = input("Would you like to deposit, withdraw, or transfer?").upper()
            savings = user['savings']

    print(choice)
    if choice == "D" and type == "C" or dualaccount == "C" and type == "B" and choice == "D":
        checking = user["checking"]
        print("How much would you like to deposit in your Checking Account?")
        print(f"Current Balance: {checking}")
        amount = float(input())
        checking.deposit(amount)
        print(checking.getBalance())
    elif choice == "D" and type == "S" or dualaccount == "S" and type == "B":
        savings = user['savings']
        print("How much would you like to deposit in your Savings Account?")
        print(f"Current Balance: {savings}")
        amount = float(input())
        savings.deposit(amount)
        print(savings.getBalance())
    elif choice == "W" and type == "C" or dualaccount == "C" and type == "B" and choice == "W":
        print("How much would you like to withdraw from your Checking Account?")
        print(f"Current Balance: {checking.getBalance()}")
        run = 0
        while run == 0 or amount - checking.getBalance() > -100:
            run += 1
            amount = float(input())
            checking.withdraw(amount)
            viewer(user, num, type)
            # if list[num].getBalance() - amount < -100:
            #   print("Amount entered is too large! You do not have sufficient funds.")
    elif choice == "W" and type == "S" or dualaccount == "S":
        print("How much would you like to withdraw from your Savings Account?")
        print(f"Current Balance: {user['savings'].getBalance()}")
        run = 0
        while run == 0 or amount - savings.getBalance() > -100:
            run += 1
            amount = float(input())
            user['savings'].withdraw(amount)
            viewer(user, num, type)
    newchoice = ""
    while newchoice != "Y" and newchoice != "N":
        print("Would you like to do anything else?")
        newchoice = input().upper()
    if newchoice == "N":
        return 0
    elif newchoice == "Y":
        initialmenu()



if __name__ == '__main__':
    b = Bank()
    initialmenu()

