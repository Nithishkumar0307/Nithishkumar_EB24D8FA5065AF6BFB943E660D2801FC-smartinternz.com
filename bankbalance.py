class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

# Create an instance of the BankAccount class with an initial balance of $1000
account = BankAccount(1000)

# Deposit $500 into the account
if account.deposit(500):
    print("Deposited $500. New balance:", account.balance)
else:
    print("Invalid deposit amount")

# Withdraw $200 from the account
if account.withdraw(200):
    print("Withdrawn $200. New balance:", account.balance)
else:
    print("Insufficient funds")

# Try to withdraw $10000 (more than the balance)
if account.withdraw(10000):
    print("Withdrawn $10,000. New balance:", account.balance)
else:
    print("Insufficient fundsa")