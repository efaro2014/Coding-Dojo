class BankAccount:
    def __init__(self, interest, balance):
        self.interest = interest
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
    def display_account_info(self):
        print('Balance: $', self.balance)

    def yield_interest(self):
        self.balance *= self.interest
    def transfer(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
efrem = BankAccount(1.2, 10)
biniam = BankAccount(.3, 200)
efrem.deposit(250)
efrem.yield_interest()
efrem.withdraw(50)
biniam.transfer(efrem, 100)
efrem.display_account_info()
biniam.display_account_info()
