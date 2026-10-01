class Sale:

    def __init__(self, sale_id, car_id, customer_id, sale_date, sale_price):
        self.sale_id = sale_id
        self.car_id = car_id
        self.customer_id = customer_id
        self.sale_date = sale_date
        self.sale_price = sale_price

if __name__ == "__main__":

    sale = Sale(
        1,
        1,
        1,
        "2026-10-01",
        3500000
    )

    print("Sale ID:", sale.sale_id)
    print("Car ID:", sale.car_id)
    print("Customer ID:", sale.customer_id)
    print("Sale Date:", sale.sale_date)
    print("Sale Price:", sale.sale_price)