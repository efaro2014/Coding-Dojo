class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.account_balance)
        # return self
    def  transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
user1 = User('Efrem', 'efrem@gmail')
user2 = User('Ben', 'ben@gmail.com')
user3 = User('guido', 'guido@gmail.com')
user3.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()




