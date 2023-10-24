#BANK ACCOUNT

class BankAccount:
    def _init_(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print('Deposited {}. New balance: {}'.format(amount, self.__account_balance))
        else:
            print('Invalid deposit amount. Please deposit a positive amount.')

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print('Withdraw {}. New balance: {}'.format(amount, self.__account_balance))
        else:
            print('Invalid withdraw amount or insufficient balance.')
account = BankAccount("300304", "HARISH", 1000.0)
account.deposit(500)
account.withdraw(200)