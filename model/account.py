class Account:
    def __init__(self, a_id, account_type, balance, customer_id):
        self.a_id = a_id,
        self.account_type = account_type,
        self.balance = balance,
        self.customer_id = customer_id,

    def to_dict(self):
        return {
        "id": self.a_id,
        "account_type": self.account_type,
        "balance": self.balance,
        "customer_id": self.customer_id,
        }