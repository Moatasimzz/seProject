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


