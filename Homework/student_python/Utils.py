import os

def takeInput(min, max):
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice < min or choice > max:
                raise ValueError
            return choice
        except ValueError:
            print("Invalid input. Please try again.")

def mainMenu():
    os.system('cls')
    print("-"*45)
    print("Welcome to the FCIT Management System")
    print("-"*45)
    print("1. Faculty")
    print("2. Student")
    print("3. Exit")
    print("-"*45)
    return takeInput(1, 3)


def subMenu(stORfac):
    os.system('cls')
    print("-"*45)
    if stORfac.lower() == "student":
        print("Welcome to the Student Menu")
    elif stORfac.lower() == "faculty":
        print("Welcome to the Faculty Menu")
    print("-"*45)
    print("1. Login")
    print("2. Register")
    print("3. Back")
    print("-"*45)
    return takeInput(1, 3)


def loggedInMenu(stORfac, username):
    print("-"*45)
    if stORfac.lower() == "student":
        print(f"Welcome to the Student Portal, {username}")
    elif stORfac.lower() == "faculty":
        print(f"Welcome to the Faculty Portal, {username}")
    print("-"*45)
    print("1. View Profile")
    print("2. Edit Profile")
    print("3. Delete Profile")
    print("4. Logout")
    print("-"*45)
    return takeInput(1, 4)