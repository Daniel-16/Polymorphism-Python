from account import Account

class SavingsAccount(Account):
    def __init__(self):
        super().__init__()
        self.withdraw_count = 0
    def withdraw(self, amount):
        if self.withdraw_count >= 10:
            return "You have reached your daily withdrawal limit"
        elif amount > 5000:
            return "You are trying to spend above your daily limit"
        else:
            self.withdraw_count += 1
            return super().withdraw(amount)

amount = int(input("Enter an amount to withdraw "))
savingsAccount = SavingsAccount()
print(savingsAccount.withdraw(amount))