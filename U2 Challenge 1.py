# Unit 2 - Challenge 1

class BankAccount:
    def __init__(self, acc_number, acc_holder_name, initial_balance=0.0):
        self.__account_number = acc_number
        self.__account_holder_name = acc_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}")


# Test the BankAccount class
account1 = BankAccount(123456, "John Doe", 1000.0)
account1.display_balance()
account1.deposit(500.0)
account1.withdraw(200.0)
account1.display_balance()
