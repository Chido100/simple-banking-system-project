from bank_account import BankAccount
import random







# User can create account
def create_account():
    account_number = input("Enter bank account number: ")
    account_holder = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, account_holder, initial_balance)


def perform_deposit(account):
    amount = float(input("Enter amount to deposit: "))
    account.deposit(amount)

def perform_withdrawal(account):
    amount = float(input("Enter amount to withdraw: "))
    account.withdraw(amount)

def check_balance(account):
    account.check_balance()

def view_transactions(account):
    account.view_transactions()