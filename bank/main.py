from bank.accounts import *
from datetime import datetime
import time


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
                reactivateamount = float(input(f"Please enter the amount you would like to deposit: (Must be greater than {user['checking'].getBalance()}"))
                if reactivateamount + user['checking'].getBalance() >= 0:
                    user['checking'].deposit(reactivateamount)
                else:
                    print(f"Invalid amount, please make a deposit of at least: {user['checking'].getBalance()}")
                print("Success, your account has been reactivated!")

        print(
            f"Hello {user['first_name']} {user['last_name']}, the balance for Checking account #{num} is {user['checking'].getBalance()}")
        choice = input("Would you like to deposit, withdraw, or transfer?").upper()

    elif type == "S":
        if user['savings'].isActive == False:
            print(f"Your account is currently disabled, please deposit a minimum of ${user['savings'].getBalance()} to reactivate your account.")
            while user['savings'].getBalance() < 0:
                reactivateamount = float(input(f"Please enter the amount you would like to deposit: (Must be greater than {user['savings'].getBalance()}"))
                if reactivateamount + user['savings'].getBalance() >= 0:
                    user['savings'].deposit(reactivateamount)
                else:
                    print(f"Invalid amount, please make a deposit of at least: {user['savings'].getBalance()}")
                print("Success, your account has been reactivated!")
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
            if user['checking'].isActive == False:
                print(
                    f"Your account is currently disabled, please deposit a minimum of ${user['checking'].getBalance()} to reactivate your account.")
                while user['checking'].getBalance() < 0:
                    reactivateamount = float(input(
                        f"Please enter the amount you would like to deposit: (Must be greater than {user['checking'].getBalance()}"))
                    if reactivateamount + user['checking'].getBalance() >= 0:
                        user['checking'].deposit(reactivateamount)
                    else:
                        print(f"Invalid amount, please make a deposit of at least: {user['checking'].getBalance()}")
                    print("Success, your account has been reactivated!")

            print(
                f"Hello {user['first_name']} {user['last_name']}, the balance for Checking account #{num} is {user['checking'].getBalance()}")
            choice = input("Would you like to deposit, withdraw, or transfer?").upper()
            checking = user['checking']
        elif dualaccount == "S":
            if user['savings'].isActive == False:
                print(
                    f"Your account is currently disabled, please deposit a minimum of ${user['savings'].getBalance()} to reactivate your account.")
                while user['savings'].getBalance() < 0:
                    reactivateamount = float(input(
                        f"Please enter the amount you would like to deposit: (Must be greater than {user['savings'].getBalance()}"))
                    if reactivateamount + user['savings'].getBalance() >= 0:
                        user['savings'].deposit(reactivateamount)
                    else:
                        print(f"Invalid amount, please make a deposit of at least: {user['savings'].getBalance()}")
                    print("Success, your account has been reactivated!")

            print(
                f"Hello {user['first_name']} {user['last_name']}, the balance for Savings account #{num} is {user['savings'].getBalance()}")
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
        b.data[num]['checking'] = user['checking']
    elif choice == "D" and type == "S" or dualaccount == "S" and type == "B" and choice == "D":
        print(choice,type,dualaccount,type)
        savings = user['savings']
        print("How much would you like to deposit in your Savings Account?")
        print(f"Current Balance: {savings}")
        amount = float(input())
        savings.deposit(amount)
        print(savings.getBalance())
        b.data[num]['savings'] = user['savings']
    elif choice == "W" and type == "C" or dualaccount == "C" and type == "B" and choice == "W":
        print("How much would you like to withdraw from your Checking Account?")
        print(f"Current Balance: {user['checking'].getBalance()}")
        run = 0
        while run == 0 or amount - user['checking'].getBalance() > -100:
            run += 1
            amount = float(input())
            checking.withdraw(amount)
            viewer(user, num, type)
            # if list[num].getBalance() - amount < -100:
            #   print("Amount entered is too large! You do not have sufficient funds.")
    elif choice == "W" and type == "S" or dualaccount == "S" and type == "B" and choice == "W":
        print("How much would you like to withdraw from your Savings Account?")
        print(f"Current Balance: {user['savings'].getBalance()}")
        run = 0
        while run == 0 or amount - savings.getBalance() > -100:
            run += 1
            amount = float(input())
            user['savings'].withdraw(amount)
            viewer(user, num, type)
    elif choice == "T" and type == "C" or dualaccount == "C" and choice == "T":
        if type == "B":
            print("Would you like to transfer to your Savings Account? Y/N")
            transferself = input().upper()
            if transferself == "Y":
                print("How much would you like to transfer from your Checking Account to your Savings Account?")
                print(f"Checking Account: ${user['checking'].getBalance()}")
                print(f"Savings Account: ${user['savings'].getBalance()}")
                amount = float(input())
                if amount <= user['checking'].getBalance():
                    user['checking'].withdraw(amount)
                    user['savings'].deposit(amount)
                    print(f"${amount} has been successfully transferred from your Checking Account to your Savings Account!")
                else:
                    print("Amount input is invalid! Please try again.")
        if type != "B" or transferself == "N":
            print("What is the account number you would like to transfer money to?")
            target = int(input("Account#"))

            accounttype = ""
            if isinstance(b.data[target]['checking'].getBalance(), str):
                accounttype = 'savings'
            elif isinstance(b.data[target]['savings'].getBalance(), str):
                accounttype = 'checking'
            else:
                print("Would you like to transfer to the users Checking or Savings Account? (C/S)")
                temp = input().upper()
                if temp == "C":
                    accounttype = 'checking'
                elif temp == "S":
                    accounttype = 'savings'

            if target in b.data and target != num and b.data[target]['checking'] != "NO_CHECKING":
                print(f"How much would you like to transfer to Account#{target}?")
                targetamount = float(input())
                if targetamount > user['checking'].getBalance():
                    print("The amount you have entered is greater than what you currently have!")
                    print("Transaction did not occur!")
                else:
                    user['checking'].withdraw(targetamount)
                    b.data[target][accounttype].deposit(targetamount)
                    print(f"You have successfully transferred ${targetamount} from Account#{num} to Account#{target}")

            else:
                print("Incorrect account number, please try again!")
    elif choice == "T" and type == "S" or dualaccount == "S" and choice == "T":
        if type == "B":
            print("Would you like to transfer to your Checking Account? Y/N")
            transferself = input().upper()
            if transferself == "Y":
                print("How much would you like to transfer from your Savings Account to your Checking Account?")
                print(f"Savings Account: ${user['savings'].getBalance()}")
                print(f"Checking Account: ${user['checking'].getBalance()}")
                amount = float(input())
                if amount <= user['savings'].getBalance():
                    user['savings'].withdraw(amount)
                    user['checking'].deposit(amount)
                    print(
                        f"${amount} has been successfully transferred from your Checking Account to your Savings Account!")
                else:
                    print("Amount input is invalid! Please try again.")
        if type != "B" or transferself == "N":
            print("What is the account number you would like to transfer money to?")
            target = int(input("Account#"))

            accounttype = ""
            if isinstance(b.data[target]['checking'].getBalance(), str):
                accounttype = 'savings'
            elif isinstance(b.data[target]['savings'].getBalance(), str):
                accounttype = 'checking'
            else:
                print("Would you like to transfer to the users Checking or Savings Account? (C/S)")
                temp = input().upper()
                if temp == "C":
                    accounttype = 'checking'
                elif temp == "S":
                    accounttype = 'savings'

            if target in b.data and target != num and b.data[target]['checking'] != "NO_CHECKING":
                print(f"How much would you like to transfer to Account#{target}?")
                targetamount = float(input())
                if targetamount > user['savings'].getBalance():
                    print("The amount you have entered is greater than what you currently have!")
                    print("Transaction did not occur!")
                else:
                    user['savings'].withdraw(targetamount)
                    b.data[target][accounttype].deposit(targetamount)
                    print(f"You have successfully transferred ${targetamount} from Account#{num} to Account#{target}")

            else:
                print("Incorrect account number, please try again!")
    newchoice = ""
    while newchoice != "Y" and newchoice != "N":
        print("Would you like to do anything else?")
        newchoice = input().upper()
    if newchoice == "N":
        return 0
    elif newchoice == "Y":
        initialmenu()



if __name__ == '__main__':
    tempdict= {}
    temp1 = {
        1000: {
            "t": 100
        }
    }
    tempdict.update(temp1)
    temp2 = {
        1000: [tempdict[1000],
        {
            "t": 300
        }]
    }
    #tempdict[1000].append(temp)
    tempdict.update(temp2)
    print(tempdict)


    input()


    testtransaction = {
        10000: [
            {
                'transaction': "D",
                'amount': 400,
                'time': "time"
            },
            {
                'transaction': "W",
                'amount': 400,
                'time': "time"
            },
            {
                'transaction': "T+",
                'amount': 400,
                'time': "time",
                'targetaccount': "target"
            }
        ],
    }
    #print(testtransaction[10000][2])
    b = Bank()
    t = TransactionView()

    t.addDeposit(10008, 200, b.data[10008].get b)
    t.addDeposit(10001, 450, b)
    print(t.transactions, 1)
    t.addDeposit(10008, 100.34, b)
    print(t.transactions, 2)
    #t.addWithdraw(10008, 300, b)
    t.addDeposit(10001, 500, b)
    t.addDeposit(10001, 1000.23, b)
    t.addDeposit(10008, 20000, b)
    t.addDeposit(10008, 530.40, b)
    t.addDeposit(10008, 4058.34, b)
    #t.addTransfer(10008, 400, 10006, b, "checking", "savings")

    print(t.transactions, 1)
    t.printAccount(10008)
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)"""

    input()
    initialmenu()

