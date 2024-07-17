def main_menu(drivers, cities):
    while True:
        print("Hello! Please enter:")
        print("1- To go to the drivers menu")
        print("2- To go to the cities menu")
        print("3- To exit the system")

        choice = input("Enter your choice: ")
        if choice == "1":
            driver_menu(drivers, cities)
        elif choice == "2":
            cities_menu(drivers, cities)
        elif choice == "3":
            print("Exiting")
            break
        else:
            print("Invalid input !!, please try again :")


