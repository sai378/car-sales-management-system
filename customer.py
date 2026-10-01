class Customer:

    def __init__(self, customer_id, name, phone, email):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email

if __name__ == "__main__":

    customer = Customer(
        1,
        "Rahul",
        "9876543210",
        "rahul@gmail.com"
    )

    print("Customer ID:", customer.customer_id)
    print("Name:", customer.name)
    print("Phone:", customer.phone)
    print("Email:", customer.email)