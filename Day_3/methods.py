class BankAccount:
    interest_rate = 0.05  # Class variable for interest rate
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")
    @classmethod
    def set_rate(cls, rate):
        cls.set_rate_rate = rate
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

acc = BankAccount("Harsha", 1000)
acc.deposit(500)
BankAccount.set_rate(0.03)
print(BankAccount.is_valid_amount(100))
    