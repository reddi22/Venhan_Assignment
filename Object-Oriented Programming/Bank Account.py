class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def withdraw(self, withdrawal_amount):
        if self.balance >= withdrawal_amount:
            self.balance -= withdrawal_amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

# Example usage
bank_details = BankAccount('9640739947', 'Ramu')

bank_details.deposit(150.0)
print(bank_details.get_balance())  # Output: 150.0

bank_details.withdraw(70.0)
print(bank_details.get_balance())  # Output: 80.0
