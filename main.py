from car_sales_system import CarSalesSystem


system = CarSalesSystem()


while True:

    print("\n======================================")
    print("      CAR SALES MANAGEMENT SYSTEM")
    print("======================================")

    print("1. Add Car")
    print("2. View Cars")
    print("3. Search Car")
    print("4. Update Car Price")
    print("5. Update Car Quantity")
    print("6. Delete Car")
    print("7. Add Customer")
    print("8. View Customers")
    print("9. Search Customer")
    print("10. Update Customer")
    print("11. Delete Customer")
    print("12. Sell Car")
    print("13. View Sales")
    print("14. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":

        system.add_car()


    elif choice == "2":

        system.view_cars()


    elif choice == "3":

        system.search_car()


    elif choice == "4":

        system.update_car_price()


    elif choice == "5":

        system.update_car_quantity()


    elif choice == "6":

        system.delete_car()


    elif choice == "7":

        system.add_customer()


    elif choice == "8":

        system.view_customers()


    elif choice == "9":

        system.search_customer()


    elif choice == "10":

        system.update_customer()


    elif choice == "11":

        system.delete_customer()


    elif choice == "12":

        system.sell_car()


    elif choice == "13":

        system.view_sales()


    elif choice == "14":

        print("Thank you for using Car Sales Management System!")
        break


    else:

        print("Invalid choice. Please try again.")