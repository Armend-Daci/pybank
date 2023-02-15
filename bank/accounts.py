class Checking:
    def __init__(self, deposit):
        self.balance = deposit


class Savings:
    def __init__(self, deposit):
        self.balance = deposit


class Bank:
    def __init__(self, accountnum, checking, savings):
        self.accountnum = accountnum
        self.checking = checking
        self.savings = savings


class CustomerAccount:
    def __init__(self, fname, lname, password, bank):
        self.lname = fname
        self.lname = lname
        self.password = password
        self.bank = bank
