# The Bank Account class

class Bank_Account:
    acct_limit = 1000.00
    balance  = 0
    def __init__(self, name, acct_no, credit, debit):
        self.name = name
        self.acct_no = acct_no
        self.credit = credit
        self.debit = debit

    def deposit(self):
        return f"Your balance is: {self.credit + int(self.balance)}"
    
    def debit_acct(self):
        return f"{self.debit - int(self.balance)} :was deducted from your account"

    def withdraw_limit(self):
        if self.balance < self.acct_limit:
            return f"Insufficient funds"
        else:
            return f"This is your balance: {self.balance}"


customer_1 = Bank_Account("Temitope", 111120, 2000, 10)
print(customer_1.deposit())
print(customer_1.debit_acct())
print(customer_1.withdraw_limit())



        
        