"""
Author: Aaron McCann
Project: Final Project
Due Date: 12/11/22
"""

# Dictionaries and Lists
database = {}

archived_database = {}

success = {}

fail = {}

state = []

counter = 0


# Function for adding to database
def add_to_database(name, street, city, location):
    global counter
    counter += 1

    database[name] = {"Street: ": street, "City: ": city, "State: ": location, "#: ": str(counter)}

    archived_database[str(counter)] = {"Name: ": name, "Street: ": street, "City: ": city, "State: ": location}


# Function for adding a celebrity to the successes database
def add_to_successes(name):
    success["Name: " + name] = {"Address Used: ": street + ", " + city + ", " + location}


# Function for adding a celebrity to the failures database
def add_to_failures(name):
    fail["Name: " + name] = {"Address Used: ": street + ", " + city + ", " + location}


# Function to display the database
def display_database():
    for main_key, main_value_pairings in database.items():
        print(main_key)

        for sub_key, sub_value in main_value_pairings.items():
            print(sub_key, sub_value)

        print()


# Function for displaying the successes in the 'success' database
def display_successes():
    for main_key, main_value_pairings in success.items():
        print(main_key)

        for sub_key, sub_value in main_value_pairings.items():
            print(sub_key, sub_value)

        print()


# Function for displaying the failures in the 'fail' database
def display_failures():
    for main_key, main_value_pairings in fail.items():
        print(main_key)

        for sub_key, sub_value in main_value_pairings.items():
            print(sub_key, sub_value)

        print()


# Function for displaying some stats regarding the database
def display_stats():
    print()

    print("Welcome to the 'Stats' section.")

    print()

    print("The amount of celebrities you sent to: " + str(len(archived_database.keys())))

    print("The amount of successes you have is: " + str(len(success.keys())))

    if len(fail.keys()) == 0:

        print("Congratulations! You have 0 failures.")

    elif len(fail.keys()) == 1:

        print("Unfortunately, you have 1 failure, that person being:")

        print()

        for main_key in fail.keys():
            print(main_key)

        print()

    elif len(fail.keys()) >= 2:

        print("Unfortunately, you have " + str(len(fail.keys())) + " failures.")

    print("You sent requests to all of these places: ")

    print()

    print(state)

    print()

    ending()


# Introduction
print("Welcome to the TTM Autograph Tracker!")

print("This program will allow you to add celebrities to your autograph database!")

print()

options = "Here are the available options below:"

print(options)

print()


# Function to add the ending to every menu option
def ending():
    print()

    print(options)

    print()

    menu_items()

    print()


# Menu Items Function
def menu_items():
    get_menu_items = ("About the Program", "Learn More About TTM and How To Do It", "Add Celebrity To Database",
                      "View Pending Database", "View or Add Successes", "View or Add Failures", "Stats", "Exit")
    for count, items in enumerate(get_menu_items, start=1):
        output = str(count) + "- " + str(items)
        print(output)


menu_items()

print()

# While loop for the menu inputs
while True:

    while True:

        askmenu = str(input("Please type the number of the option you would like to see: "))

        # About menu option
        if askmenu == "1":

            print()

            print("Welcome to the 'About the Program' section.")

            print()

            print("This program allows you to add celebrities to your TTM database. This includes \
their name, as well as address.")

            print("You can also add celebrities to your successes or failures, and view stats such \
as most common state sent to.")

            print("Successes means that you got your photo or item back signed.")

            print("Failures means you got your photo or item back unsigned or returned to sender.")

            ending()

        # TTM menu option
        elif askmenu == "2":

            print()

            print("Welcome to the 'Learn More About TTM and How To Do It' section.")

            print()

            print("TTM stands for 'Through the Mail'. This means sending fanmail to celebrities and asking \
for their autographs.")

            print()

            print("1. Look-up the celebrity you want to send fanmail to on websites like 'fanmail.biz' \
or 'startiger.com' which will provide a potential address to send the mail to.")

            print()

            print("2. After finding an address, find a picture of the celebrity you like and get it printed, \
ideally from a photo lab and not a home printer.")

            print()

            print("3. After getting the photo, find two envelopes that will fit the photo without bending it.")

            print()

            print("4. Write a genuine letter to the celebrity, and include your request for their autograph in there.")

            print()

            print("5. On one envelope, write your name and address on it, and put 2-3 stamps on it, \
depending on the weight of the included items. Then fold it in half.")

            print()

            print("6. On the other envelope, write your name and address on top left corner, \
and celebrities name and address in the middle, and put 3 stamps on it.")

            print()

            print("7. Take the folded envelope, as well as the photo and letter, and put it in the envelope with the \
celebrities name on it.")

            print()

            print("8. Seal the envelope and mail it.")

            print()

            print("9. Now wait until you see your envelope arrive back to you in your mailbox.")

            print()

            print("I hope this provides some useful information on TTM.")

            ending()

        # Add celebrity menu option
        elif askmenu == "3":

            print()

            print("Welcome to the 'Add Celebrity to Database' section.")

            print()

            print("Follow the directions below to continue.")

            print()

            while True:

                name = str(input("What is the celebrities name: ")).strip().title()

                street = str(input("What is the street address you are sending to: ")).strip().title()

                city = str(input("What is the city you are sending to: ")).strip().title()

                location = str(input("What is the state you are sending to: ")).strip().upper()

                add_to_database(name, street, city, location)

                state.append(location)

                print()

                if len(name.strip()) + len(street.strip()) + len(city.strip()) + len(location.strip()) == 0:

                    print("Fields left blank. Please try again")

                    del database[name]

                    counter -= 1

                    del archived_database[str(counter)]

                    print()

                elif len(name.strip()) + len(street.strip()) + len(city.strip()) + len(location.strip()) >= 0:

                    while True:

                        another = str(input("Would you like to add another celebrity to the database? Please type \
'yes' or 'no': ")).strip().lower()

                        if another == "yes":

                            print()

                            name = str(input("What is the celebrities name: ")).strip().title()

                            street = str(input("What is the street address you are sending to: ")).strip().title()

                            city = str(input("What is the city you are sending to: ")).strip().title()

                            location = str(input("What is the state you are sending to: ")).strip().upper()

                            add_to_database(name, street, city, location)

                            state.append(location)

                            print()

                            if len(name.strip()) + len(street.strip()) + len(city.strip()) + len(location.strip()) == 0:

                                counter -= 1

                                print("Fields left blank. Please try again")

                                del database[name]

                                del archived_database[str(counter)]

                                print()

                        elif another == "no":

                            ending()

                            break

                    break

        # Display pending database menu option
        elif askmenu == "4":

            print()

            print("Welcome to the 'View Pending Database' section.")

            if len(database.keys()) == 0:

                print()

                print("There are no celebrities in the pending database. Please add a celebrity to continue.")

                ending()

                continue

            elif len(database.keys()) >= 1:

                print()

                display_database()

                ending()

        # View or add successes menu option
        elif askmenu == "5":

            print()

            print("Welcome to the 'View or Add Successes' section.")

            print()

            if len(archived_database.keys()) == 0:

                print("There are no celebrities in database. Please come back later.")

                ending()

            elif len(archived_database.keys()) >= 1:

                while True:

                    ask5 = str(input("Would you like to view or add successes? Please type \
'view' or 'add': ")).strip().lower()

                    if ask5 == "view":

                        if len(success.keys()) == 0:

                            print()

                            print("There are currently no recorded successes. Please add a success to continue.")

                            ending()

                            break

                        elif len(success.keys()) >= 1:

                            print()

                            display_successes()

                            ending()

                            break

                    elif ask5 == "add":

                        while True:

                            name = str(input("Please type the celebrities name: ")).strip().title()

                            while True:

                                if name not in database.keys():

                                    print()

                                    print("Invalid name. Please try again.")

                                    ending()

                                    break

                                elif name in database.keys():

                                    print()

                                    print(name + " successfully added to successes.")

                                    add_to_successes(name)

                                    del database[name]

                                    print()

                                    while True:

                                        another = str(input("Would you like to add another celebrity to the successes? \
Please type 'yes' or 'no': ")).strip().lower()

                                        if another == "yes":

                                            name = str(input("Please type the celebrities name: ")).strip().title()

                                            if name not in database.keys():

                                                print()

                                                print("Invalid name. Please try again.")

                                                ending()

                                                break

                                            elif name in database.keys():

                                                print()

                                                print(name + " successfully added to successes.")

                                                add_to_successes(name)

                                                del database[name]

                                                print()

                                                continue

                                        elif another == "no":

                                            ending()

                                            break

                                    break

                            break

                        break

        # View or add failures menu option
        elif askmenu == "6":

            print()

            print("Welcome to the 'View or Add Failures' section.")

            print()

            if len(archived_database.keys()) == 0:

                print("There are no celebrities in database. Please come back later.")

                ending()

            elif len(archived_database.keys()) >= 1:

                while True:

                    ask6 = str(input("Would you like to view or add Failures? Please type \
'view' or 'add': ")).strip().lower()

                    if ask6 == "view":

                        if len(fail.keys()) == 0:

                            print()

                            print("There are currently no recorded failures. Please add a success to continue.")

                            ending()

                            break

                        elif len(fail.keys()) >= 1:

                            print()

                            display_failures()

                            ending()

                            break

                    elif ask6 == "add":

                        while True:

                            name = str(input("Please type the celebrities name: ")).strip().title()

                            while True:

                                if name not in database.keys():

                                    print()

                                    print("Invalid name. Please try again.")

                                    ending()

                                    break

                                elif name in database.keys():

                                    print()

                                    print(name + " successfully added to failures.")

                                    add_to_failures(name)

                                    del database[name]

                                    print()

                                    while True:

                                        another = str(input("Would you like to add another celebrity to the successes? \
Please type 'yes' or 'no': ")).strip().lower()

                                        if another == "yes":

                                            name = str(input("Please type the celebrities name: ")).strip().title()

                                            if name not in database.keys():

                                                print()

                                                print("Invalid name. Please try again.")

                                                ending()

                                                break

                                            elif name in database.keys():

                                                print()

                                                print(name + " successfully added to failures.")

                                                add_to_failures(name)

                                                del database[name]

                                                print()

                                                continue

                                        elif another == "no":

                                            ending()

                                            break

                                    break

                            break

                        break

        # Stats menu option
        elif askmenu == "7":

            display_stats()

        # Exiting the program menu option
        elif askmenu == "8":

            print()

            print("Thank you for visiting the TTM Autograph Tracker. We hope you will use it again in the future!")

            break

    break
