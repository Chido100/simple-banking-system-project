class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []

    def __str__(self):
        return f"Account[{self.account_number}] - Holder: {self.account_holder} - Balance: £{self.balance}"

