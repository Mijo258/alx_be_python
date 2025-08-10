#!/usr/bin/python3
"""
This module defines the BankAccount class for simple banking operations.
"""


class BankAccount:
    """A class to represent a simple bank account."""

    def __init__(self, account_balance=0):
        """Initializes a new BankAccount instance."""
        self.account_balance = int(account_balance)

    def deposit(self, amount):
        """Adds a specified amount to the account balance."""
        self.account_balance += int(amount)
        # It's good practice to return the new balance
        return f"Current Balance:{self.account_balance}"

    def withdraw(self, amount):
        """
        Withdraws a specified amount if funds are sufficient.
        Returns True for success, False for failure.
        """
        if int(amount) > self.account_balance:
            return False
        else:
            self.account_balance -= int(amount)
            return True

    def display_balance(self):
        """Returns the current account balance."""
        return self.account_balance