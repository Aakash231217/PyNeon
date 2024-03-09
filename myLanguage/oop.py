class Payment:
    initial_balance = 1000
    def __init__(self,recipient,amount):
        self.recipient = recipient
        self.amount = amount
    def check_balance(self, initial):
        return Payment.initial - self.amount
        
transaction1 = Payment("A",25)

