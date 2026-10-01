import MySQLdb

from database import DatabaseConnection
from car import Car
from customer import Customer
from sale import Sale


class CarSalesSystem:

    def __init__(self):
        self.db = DatabaseConnection()

    # ==========================================================
    # CAR OPERATIONS
    # ==========================================================

    def add_car(self):

        try:
            brand = input("Enter car brand: ")
            model = input("Enter car model: ")
            price = float(input("Enter car price: "))
            quantity = int(input("Enter available quantity: "))

            if price <= 0 or quantity < 0:
                print("Invalid price or quantity.")
                return

            car = Car(0, brand, model, price, quantity)

            con = self.db.connect()

            if con:

                try:
                    cursor = con.cursor()

                    sql = """
                    INSERT INTO cars
                    (brand, model, price, available_quantity)
                    VALUES (%s, %s, %s, %s)
                    """

                    values = (
                        car.brand,
                        car.model,
                        car.price,
                        car.available_quantity
                    )

                    cursor.execute(sql, values)
                    con.commit()

                    print("Car added successfully!")

                except MySQLdb.Error as e:
                    print("Database Error:", e)

                finally:
                    con.close()

        except ValueError:
            print("Please enter valid numeric values.")


    def view_cars(self):

        con = self.db.connect()

        if con:

            try:
                cursor = con.cursor()

                sql = "SELECT * FROM cars"

                cursor.execute(sql)

                records = cursor.fetchall()

                if records:

                    print("\n========== ALL CARS ==========")

                    for row in records:

                        print("Car ID:", row[0])
                        print("Brand:", row[1])
                        print("Model:", row[2])
                        print("Price:", row[3])
                        print("Available Quantity:", row[4])
                        print("------------------------------")

                else:
                    print("No cars found.")

            except MySQLdb.Error as e:
                print("Database Error:", e)

            finally:
                con.close()


    def search_car(self):

        search = input("Enter car brand or model to search: ")

        con = self.db.connect()

        if con:

            try:
                cursor = con.cursor()

                sql = """
                SELECT * FROM cars
                WHERE brand LIKE %s OR model LIKE %s
                """

                value = "%" + search + "%"

                cursor.execute(sql, (value, value))

                records = cursor.fetchall()

                if records:

                    print("\n========== SEARCH RESULTS ==========")

                    for row in records:

                        print("Car ID:", row[0])
                        print("Brand:", row[1])
                        print("Model:", row[2])
                        print("Price:", row[3])
                        print("Available Quantity:", row[4])
                        print("------------------------------------")

                else:
                    print("Car not found.")

            except MySQLdb.Error as e:
                print("Database Error:", e)

            finally:
                con.close()


    def update_car_price(self):

        try:
            car_id = int(input("Enter car ID: "))
            new_price = float(input("Enter new price: "))

            if new_price <= 0:
                print("Invalid price.")
                return

            con = self.db.connect()

            if con:

                try:
                    cursor = con.cursor()

                    sql = """
                    UPDATE cars
                    SET price = %s
                    WHERE car_id = %s
                    """

                    cursor.execute(sql, (new_price, car_id))

                    if cursor.rowcount > 0:
                        con.commit()
                        print("Car price updated successfully!")
                    else:
                        print("Car not found.")

                except MySQLdb.Error as e:
                    print("Database Error:", e)

                finally:
                    con.close()

        except ValueError:
            print("Please enter valid values.")


    def update_car_quantity(self):

        try:
            car_id = int(input("Enter car ID: "))
            quantity = int(input("Enter new available quantity: "))

            if quantity < 0:
                print("Invalid quantity.")
                return

            con = self.db.connect()

            if con:

                try:
                    cursor = con.cursor()

                    sql = """
                    UPDATE cars
                    SET available_quantity = %s
                    WHERE car_id = %s
                    """

                    cursor.execute(sql, (quantity, car_id))

                    if cursor.rowcount > 0:
                        con.commit()
                        print("Car quantity updated successfully!")
                    else:
                        print("Car not found.")

                except MySQLdb.Error as e:
                    print("Database Error:", e)

                finally:
                    con.close()

        except ValueError:
            print("Please enter valid values.")


    def delete_car(self):

        try:
            car_id = int(input("Enter car ID to delete: "))

            con = self.db.connect()

            if con:

                try:
                    cursor = con.cursor()

                    sql = """
                    DELETE FROM cars
                    WHERE car_id = %s
                    """

                    cursor.execute(sql, (car_id,))

                    if cursor.rowcount > 0:
                        con.commit()
                        print("Car deleted successfully!")
                    else:
                        print("Car not found.")

                except MySQLdb.Error as e:

                    print("Unable to delete car.")
                    print("Error:", e)

                finally:
                    con.close()

        except ValueError:
            print("Please enter a valid car ID.")


    # ==========================================================
    # CUSTOMER OPERATIONS
    # ==========================================================

    def add_customer(self):

        name = input("Enter customer name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        customer = Customer(0, name, phone, email)

        con = self.db.connect()

        if con:

            try:
                cursor = con.cursor()

                sql = """
                INSERT INTO customers
                (name, phone, email)
                VALUES (%s, %s, %s)
                """

                values = (
                    customer.name,
                    customer.phone,
                    customer.email
                )

                cursor.execute(sql, values)

                con.commit()

                print("Customer added successfully!")

            except MySQLdb.Error as e:

                print("Database Error:", e)

            finally:
                con.close()


    def view_customers(self):

        con = self.db.connect()

        if con:

            try:
                cursor = con.cursor()

                sql = "SELECT * FROM customers"

                cursor.execute(sql)

                records = cursor.fetchall()

                if records:

                    print("\n========== ALL CUSTOMERS ==========")

                    for row in records:

                        print("Customer ID:", row[0])
                        print("Name:", row[1])
                        print("Phone:", row[2])
                        print("Email:", row[3])
                        print("-----------------------------------")

                else:
                    print("No customers found.")

            except MySQLdb.Error as e:

                print("Database Error:", e)

            finally:
                con.close()


    def search_customer(self):

        search = input("Enter customer name or phone: ")

        con = self.db.connect()

        if con:

            try:
                cursor = con.cursor()

                sql = """
                SELECT * FROM customers
                WHERE name LIKE %s OR phone LIKE %s
                """

                value = "%" + search + "%"

                cursor.execute(sql, (value, value))

                records = cursor.fetchall()

                if records:

                    print("\n========== SEARCH RESULTS ==========")

                    for row in records:

                        print("Customer ID:", row[0])
                        print("Name:", row[1])
                        print("Phone:", row[2])
                        print("Email:", row[3])
                        print("------------------------------------")

                else:
                    print("Customer not found.")

            except MySQLdb.Error as e:

                print("Database Error:", e)

            finally:
                con.close()


    def update_customer(self):

        try:
            customer_id = int(input("Enter customer ID: "))

            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")

            con = self.db.connect()

            if con:

                try:
                    cursor = con.cursor()

                    sql = """
                    UPDATE customers
                    SET name = %s,
                        phone = %s,
                        email = %s
                    WHERE customer_id = %s
                    """

                    values = (
                        name,
                        phone,
                        email,
                        customer_id
                    )

                    cursor.execute(sql, values)

                    if cursor.rowcount > 0:
                        con.commit()
                        print("Customer updated successfully!")
                    else:
                        print("Customer not found.")

                except MySQLdb.Error as e:

                    print("Database Error:", e)

                finally:
                    con.close()

        except ValueError:
            print("Please enter a valid customer ID.")


    def delete_customer(self):

        try:
            customer_id = int(input("Enter customer ID to delete: "))

            con = self.db.connect()

            if con:

                try:
                    cursor = con.cursor()

                    sql = """
                    DELETE FROM customers
                    WHERE customer_id = %s
                    """

                    cursor.execute(sql, (customer_id,))

                    if cursor.rowcount > 0:
                        con.commit()
                        print("Customer deleted successfully!")
                    else:
                        print("Customer not found.")

                except MySQLdb.Error as e:

                    print("Database Error:", e)

                finally:
                    con.close()

        except ValueError:
            print("Please enter a valid customer ID.")


    # ==========================================================
    # SELL CAR
    # ==========================================================

    def sell_car(self):

        try:
            customer_id = int(input("Enter customer ID: "))
            car_id = int(input("Enter car ID: "))

            con = self.db.connect()

            if con:

                try:
                    cursor = con.cursor()

                    # Check customer
                    sql = """
                    SELECT * FROM customers
                    WHERE customer_id = %s
                    """

                    cursor.execute(sql, (customer_id,))

                    customer = cursor.fetchone()

                    if customer is None:
                        print("Customer not found.")
                        return

                    # Check car
                    sql = """
                    SELECT * FROM cars
                    WHERE car_id = %s
                    """

                    cursor.execute(sql, (car_id,))

                    car = cursor.fetchone()

                    if car is None:
                        print("Car not found.")
                        return

                    # Check quantity
                    available_quantity = car[4]

                    if available_quantity <= 0:
                        print("Car is currently unavailable.")
                        return

                    sale_price = car[3]

                    # Create sale
                    sql = """
                    INSERT INTO sales
                    (car_id, customer_id, sale_date, sale_price)
                    VALUES (%s, %s, CURDATE(), %s)
                    """

                    cursor.execute(
                        sql,
                        (car_id, customer_id, sale_price)
                    )

                    # Reduce quantity
                    sql = """
                    UPDATE cars
                    SET available_quantity = available_quantity - 1
                    WHERE car_id = %s
                    """

                    cursor.execute(sql, (car_id,))

                    con.commit()

                    print("\nCar sold successfully!")
                    print("Sale Price:", sale_price)
                    print("Remaining Quantity:", available_quantity - 1)

                except MySQLdb.Error as e:

                    con.rollback()
                    print("Sale failed:", e)

                finally:
                    con.close()

        except ValueError:
            print("Please enter valid IDs.")


    # ==========================================================
    # VIEW SALES
    # ==========================================================

    def view_sales(self):

        con = self.db.connect()

        if con:

            try:
                cursor = con.cursor()

                sql = """
                SELECT
                    s.sale_id,
                    c.name,
                    ca.brand,
                    ca.model,
                    s.sale_price,
                    s.sale_date
                FROM sales s
                JOIN customers c
                    ON s.customer_id = c.customer_id
                JOIN cars ca
                    ON s.car_id = ca.car_id
                """

                cursor.execute(sql)

                records = cursor.fetchall()

                if records:

                    print("\n================ SALES DETAILS ================")

                    for row in records:

                        print("Sale ID:", row[0])
                        print("Customer:", row[1])
                        print("Car:", row[2], row[3])
                        print("Sale Price:", row[4])
                        print("Sale Date:", row[5])
                        print("----------------------------------------------")

                else:
                    print("No sales found.")

            except MySQLdb.Error as e:

                print("Database Error:", e)

            finally:
                con.close()