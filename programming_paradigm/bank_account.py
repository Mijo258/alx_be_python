class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = int(account_balance)

    def deposit(self, amount):
        self.account_balance += int(amount)

    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        else:
            self.account_balance -= int(amount)
            return True
    def display_balance(self):
            return self.account_balance
