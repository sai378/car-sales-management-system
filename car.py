class Car:

    def __init__(self, car_id, brand, model, price, available_quantity):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.price = price
        self.available_quantity = available_quantity

if __name__ == "__main__":

    car = Car(1, "Toyota", "Fortuner", 3500000, 5)

    print("Car ID:", car.car_id)
    print("Brand:", car.brand)
    print("Model:", car.model)
    print("Price:", car.price)
    print("Available Quantity:", car.available_quantity)