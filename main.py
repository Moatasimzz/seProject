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

def driver_menu(drivers, cities):
    while True:
        print("Enter:")
        print("1- To view all the drivers")
        print("2- To add a driver")
        print("3- To go back to main menu")
        choice = input("Your choice: ")

        if choice == "1":
            view_drivers(drivers)
        elif choice == "2":
            add_driver(drivers, cities)
        elif choice == "3":
            print("Going back to main menu")
            break
        else:
            print("Invalid input !!, please try again")


def cities_menu(drivers, cities):
    while True:
        print("CITIES MENU")
        print("Enter:")
        print("1- To show all cities")
        print("2- To print neighboring cities")
        print("3- To print drivers delivering to a city")
        print("4- To go back to main menu")
        choice = input("Your choice: ")

        if choice == "1":
            show_cities(cities)
        elif choice == "2":
            print_neighboring_cities(cities)
        elif choice == "3":
            print_drivers_delivering_to_city(drivers, cities)
        elif choice == "4":
            print("Going back to main menu...")
            break
        else:
            print("Invalid input !!, please try again :")

            