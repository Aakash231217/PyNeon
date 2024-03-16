class Payment:
    initial_balance = 1000
    def __init__(self,recipient,amount):
        self.recipient = recipient
        self.amount = amount
    def check_balance(self, initial):
        return Payment.initial - self.amount
    @classmethod
    def update_initial_balance(cls,new_balance):
        cls.initial_balance = new_balance
    @staticmethod
    def check_valid_transaction(hour):
        if hour>=8 and hour <= 17:
            return True
        return False
transaction1 = Payment("A",25)
Payment.update_initial_balance(800)
print(transaction1.initial_balance)
print(Payment.initial_balance)
print(transaction1.check_valid_transaction(25));