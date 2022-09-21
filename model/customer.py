class Customer:
    def __init__(self, c_id, customername, first_name, last_name, customer_phone, username):
        self.id = c_id,
        self.customername = customername,
        self.first_name = first_name,
        self.last_name = last_name,
        self.customer_phone = customer_phone,
        self.username = username

    def to_dict(self):
        return {
        "id": self.id,
        "customername": self.customername,
        "first_name": self.first_name,
        "last_name": self.last_name,
        "customer_phone": self.customer_phone,
        "username": self.username,
        }