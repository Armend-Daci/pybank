class Checking:
    def __init__(self, deposit):
        self.balance = float(0)
        if deposit != "NO_CHECKING":
            print(deposit)
            deposit = float(deposit)
        self.balance = deposit
        self.overdraft = 0
        self.isActive = True

    def __str__(self):
        if self.balance == 'NO_CHECKING':
            return str("NO_CHECKING")
        else:
            return str(self.balance)

    def deposit(self, deposit):
        self.balance += deposit
        if self.isActive == False:
            self.isActive == True
            self.overdraft = 0

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Transaction successful. New balance is: {self.balance}")
        elif amount > self.balance and self.balance - amount > -100:
            self.balance = self.balance - amount - 35
            print(f"You have withdrawn more than your current balance, so an overdraft fee of $35 has been applied.")
            print(f"New balance is: {self.balance}")
            self.overdraft += 1
            if self.overdraft == 2:
                self.isActive = False
        elif self.balance - amount < -100:
            print(f"The amount you have selected is too big! Transaction Failed")


class Savings:
    def __init__(self, deposit):
        self.balance = float(0)
        if "NO_SAVINGS" not in deposit:
            print(deposit)
            deposit = float(deposit)
        self.balance = deposit
        self.overdraft = 0
        self.isActive = True

    def __str__(self):
        if self.balance == 'NO_SAVINGS':
            return str("NO_SAVINGS")
        else:
            return str(self.balance)

    def deposit(self, deposit):
        self.balance += deposit
        if self.isActive == False:
            self.isActive == True
            self.overdraft = 0

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Transaction successful. New balance is: {self.balance}")
        elif amount > self.balance and self.balance - amount > -100:
            self.balance = self.balance - amount - 35
            print(f"You have withdrawn more than your current balance, so an overdraft fee of $35 has been applied.")
            print(f"New balance is: {self.balance}")
            self.overdraft += 1
            if self.overdraft == 2:
                self.isActive = False
        elif self.balance - amount < -100:
            print(f"The amount you have selected is too big! Transaction Failed")


class Bank:
    data = {}

    def __init__(self):
        Bank.__read_data()

    @classmethod
    def __read_data(cls):
        print(1)
        file = open("bank/bank.csv", "r")
        for line in file:
            row = line.split(';')
            Bank.data[int(row[0])] = {
                'first_name': row[1],
                'last_name': row[2],
                'password': row[3],
                'checking': Checking(row[4]),
                'savings': Savings(row[5])
            }
        file.close()

    def test(self):
        return 5

    def getAccount(self):
        return self.accountnum

    def getAccountType(self):
        if self.checking and self.savings:
            return "B"
        elif self.checking and not self.savings:
            return "C"
        elif self.savings and not self.savings:
            return "S"

    def getChecking(self):
        return self.checking

    def getSavings(self):
        return self.savings


class CustomerAccount:
    def __init__(self, fname, lname, password, bank):
        self.fname = fname
        self.lname = lname
        self.password = password
        self.bank = bank

    def __init__(self):
        pass

    def __str__(self):
        pass

    def getFName(self):
        return self.fname

    def getLName(self):
        return self.lname

    def getPassword(self):
        return self.password

    def getBank(self):
        return self.bank


class TransactionView:

    def __init__(self):
        self.transactions = {}

    def addDeposit(self, num, amount):
        print(type(self.transactions))
        if self.transactions == {}:
            self.transactions = {
                    num: [{
                    'transaction_type': "D",
                    'amount': amount,
                    'time': "time"
                }]
            }
            print("True")
        else:
            self.transactions[num].append(
                {
                    'transaction_type': "D",
                    'amount': amount,
                    'time': "time"
                }
            )
        print(self.transactions, "Done")


    def addWithdraw(self):
        pass

    def addTransfer(self):
        pass

"""
    accountnum: {
        transactiontype: D
        time: time
        amount: amount
    }
"""