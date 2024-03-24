class BankAccount:
    def __init__(self, account_number, initial_balance):
        self._account_number = account_number
        self._balance = initial_balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance