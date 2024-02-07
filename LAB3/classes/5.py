class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successful! New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Successful! New balance: ${self.balance}")
        else:
            print("Not enough funds.")


account = Account(owner="Hello World", balance=1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  
account.deposit(300)
