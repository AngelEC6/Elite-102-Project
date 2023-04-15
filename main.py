import mysql.connector
import os

connection = mysql.connector.connect(user="root",database = "elite 102 project",password = "JacktHepuG6")


top_logo = "=============================================================\n                   Ficticious Bank\n============================================================="
def main_menu():
    print(top_logo)
    next_menu = input("\n\n\n\nAre you a user or an administrator?: ")
    return next_menu

def check_user_type():
    print(top_logo)
    user_type_input = input("\n\n\n\nAre you an existing or new user?: ")
    if user_type_input == "existing":
        return user_type_input
    elif user_type_input == "new":
        return user_type_input
    else:
        while True:
            print(top_logo)
            user_type_input = input("\n\n\nThat is not a valid response please try again. This time respond using either new or existing.\nAre you an existing or new user?: ")
            if user_type_input == "existing":
                return user_type_input
            elif user_type_input == "new":
                return user_type_input


def existing_acount_number_menu():
    while True:
        try:
            print(top_logo)
            user_id_input = input("\n\n\n\nAcount Number: ")
            if user_id_input == "Back" or user_id_input == "back":
                return user_id_input
            user_id_input = int(user_id_input)
            if type(user_id_input) == int:
                break
        except ValueError:
            print(top_logo)
            print("\n\n\n\nThat wasn't a number please try again.")
    passed = check_id(user_id_input)
    #os.system('cls')
    if passed == True:
        password_menu(user_id_input)
    elif user_id_input == "Back":
        return null
    else:
        while True:
            try:
                print(top_logo)
                user_id_input = int(input("\n\n\nThat acount doesn't exist.Please try again.\nAcount Number: "))
                passed = check_id(user_id_input)
                #os.system('cls')
                if passed == True:
                    break
            except ValueError:
                print(top_logo)
                print("\n\n\n\nThat wasn't a number please try again.")
        password_menu(user_id_input)
    
def password_menu(acount_number):
    print(top_logo)
    user_password_input = input("\n\n\n\nPassword: ")
    passed = check_password(user_password_input,acount_number)
    if passed == True:
        existing_user_menu()
    else:
        while True:
            print(top_logo)
            user_password_input = input("\n\n\nThat password was incorrect.Please Try again.\nPassword: ")
            passed = check_password(user_password_input,acount_number)
            if passed == True:
                break
        existing_user_menu()

def existing_user_menu():
    print("existing user menu")

    
def check_password(user_input,acount_number):
    check_password_cursor = connection.cursor()
    get_password = ("SELECT userpassword FROM acountinfo WHERE idnumber = " + str(acount_number))
    check_password_cursor.execute(get_password)
    password = check_password_cursor.fetchall()
    if password[0][0] == user_input:
        check_password_cursor.close()
        return True
    else:
        check_password_cursor.close()
        return False
    

def check_id(user_input):
    check_number = connection.cursor()
    get_numbers = ("SELECT idnumber FROM acountinfo")
    check_number.execute(get_numbers)
    acount_numbers = check_number.fetchall()    
    for number in acount_numbers:
        print(number)
        if number[0] == user_input:
            check_number.close()
            return True
    check_number.close()
    return False

while True:
    next_menu = main_menu()
    #os.system('cls')
    if next_menu == "administrator":
        print(top_logo)
        admin_username = input("\n\n\n\nUsername: ")
        if type(admin_username) == str:
            break
    elif next_menu == "user":
        user_type = check_user_type()
        if user_type == "new":
            print("new user menu")
        elif user_type == "existing":
            existing_acount_number_menu()
    else:
        print(top_logo)


connection.close()