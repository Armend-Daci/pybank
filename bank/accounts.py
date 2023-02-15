class Checking:
    pass


class Savings:
    pass


class Bank:
    def __init__(self, accountnum, checking, savings):
        self.accountnum = accountnum
        self.checking = checking
        self.savings = savings


class CustomerAccount:
    def __init__(self, fname, lname, bank):
        self.lname = fname
        self.lname = lname
        self.bank = bank
