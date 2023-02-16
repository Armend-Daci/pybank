class Checking:
    def __init__(self, deposit):
        self.balance = deposit

    def deposit(self, deposit):
        self.balanace += deposit

    def getBalance(self):
        return self.balance

class Savings:
    def __init__(self, deposit):
        self.balance = deposit

    def deposit(self, deposit):
        self.balance += deposit

    def getBalance(self):
        return self.balance

class Bank:
    def __init__(self, accountnum, checking, savings):
        self.accountnum = accountnum
        self.checking = checking
        self.savings = savings


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
        self.lname = fname
        self.lname = lname
        self.password = password
        self.bank = bank

    def __str__(self):
        pass

    def getPassword(self):
        return self.password

    def getBank(self):
        return self.bank
