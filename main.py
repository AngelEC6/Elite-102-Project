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

def new_acount_menu():
    print(top_logo)
    create_acount = input("\n\n\n\nWould you like to open a new acount?: ")
    if create_acount == "yes":
        create_new_acount_menu()
    elif create_acount == "back":
        return "null"
    else:
        while True:
            print(top_logo)
            create_acount = input("\n\n\nThat is not a valid input.Please try again.\nWould you like to open a new acount?: ")
            if create_acount == "yes":
                create_new_acount_menu()
                break
            elif create_acount == "back":
                return "null"

def create_new_acount_menu():
    user_name = get_user_name()
    pin = get_user_pin()
    new_acount_info = create_new_acount(user_name,pin)
    print(top_logo)
    input("\n\nYour acount has been succesfully created.\nYour acount details are:\nAcount Number: " + str(new_acount_info[0][0]) + "\nPin: " + str(new_acount_info[0][1]) + "\nBalance: " + str(new_acount_info[0][2]) + "\nName: " + new_acount_info[0][3] + "\nPress enter when you're ready to move on.")

def create_new_acount(new_user_name,new_user_pin):
    create_new_acount_cursor = connection.cursor()
    create_new_acount_code = ("INSERT INTO acountinfo (pin,amount,username) VALUES ('" + str(new_user_pin) + "', 0, '" + new_user_name + "')")
    create_new_acount_cursor.execute(create_new_acount_code)
    create_new_acount_cursor.close()
    check_new_acount_cursor = connection.cursor()
    check_new_acount_code = ("SELECT * FROM acountinfo WHERE pin = " + str(new_user_pin))
    check_new_acount_cursor.execute(check_new_acount_code)
    new_acount_info = check_new_acount_cursor.fetchall()
    check_new_acount_cursor.close()
    return new_acount_info


def get_user_name():
    print(top_logo)
    new_user_name = input("\n\n\n\nEnter your name: ")
    return new_user_name

def get_user_pin():
    while True:
        try:
            print(top_logo)
            new_user_password = int(input("\n\n\n\nEnter your pin: "))
            break
        except ValueError:
            print(top_logo)
            print("\n\n\n\nThat's not a number please try again.")
    return new_user_password


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
        pin_menu(user_id_input)
    elif user_id_input == "Back":
        return "null"
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
        pin_menu(user_id_input)
    
def pin_menu(acount_number):
    while True:
        try:
            print(top_logo)
            user_pin_input = input("\n\n\n\nPin: ")
            if user_pin_input == "back":
                return "null"
            user_pin_input = int(user_pin_input)
            passed = check_pin(user_pin_input,acount_number)
            if passed == True:
                existing_user_menu(acount_number)
                return "void"
        except ValueError:
            print(top_logo)
            print("\n\n\n\nThat's not a number please try again")
    while True:
        try:
            if passed != True:
                while True:
                    print(top_logo)
                    user_pin_input = input("\n\n\nThat pin was incorrect.Please Try again.\nPin: ")
                    if user_pin_input == "back":
                        return "null"
                    user_pin_input = int(user_pin_input)
                    passed = check_pin(user_pin_input,acount_number)
                    if passed == True:
                        break
                existing_user_menu(acount_number)
                return "null"
        except ValueError:
            print(top_logo)
            print("\n\n\n\nThat's not a number please try again.")

def existing_user_menu(acount_number):
    while True:
        print(top_logo)
        user_choice = input("\n\n\n\nWhat would you like to do (deposit,withdrawal,check balance,)?: ")
        if user_choice == "deposit":
            user_deposit_menu(acount_number)
        elif user_choice == "withdrawal":
            user_withdrawal_menu(acount_number)
        elif user_choice == "check balance":
            user_check_balance_menu(acount_number)
        elif user_choice == "back":
            break
        else:
            while True:
                print(top_logo)
                user_choice = input("\n\n\nSorry that is not a valid option. Please try again.\nWhat would you like to do (deposit,withdrawal,check balance,)?: ")
                if user_choice == "deposit":
                    user_deposit_menu(acount_number)
                    break
                elif user_choice == "withdrawal":
                    user_withdrawal_menu(acount_number)
                    break
                elif user_choice == "check balance":
                    user_check_balance_menu(acount_number)
                    break
                elif user_choice == "back":
                    return "null"

def user_deposit_menu(acount_number):
    while True:
        try:
            print(top_logo)
            user_deposit_input = input("\n\n\n\nHow much money would you like to deposit?: ")
            if user_deposit_input == "back":
                return "null"
            user_deposit_input = float(user_deposit_input)
            break
        except ValueError:
            print(top_logo)
            print("\n\n\n\nThat is not a valid input. Please try again.")
    deposit(user_deposit_input,acount_number)

def deposit(amount,acount_number):
    acount_balance = check_balance(acount_number)
    new_balance = float(acount_balance) + amount
    deposit_cursor = connection.cursor()
    deposit_amount = ("UPDATE acountinfo SET amount = " + str(new_balance) + " WHERE idnumber = " + str(acount_number))
    deposit_cursor.execute(deposit_amount)
    deposit_cursor.close()



def user_withdrawal_menu(acount_number):
    while True:
        try:
            print(top_logo)
            user_withdrawal_input = input("\n\n\n\nHow much money would you like to withdrawal?: ")
            if user_withdrawal_input == "back":
                return "null"
            user_withdrawal_input = float(user_withdrawal_input)
            break
        except ValueError:
            print(top_logo)
            print("\n\n\n\nThat is not a valid input. Please try again.")
    withdrawal(user_withdrawal_input,acount_number)

def withdrawal(amount,acount_number):
    acount_balance = check_balance(acount_number)
    new_balance = float(acount_balance) - amount
    withdrawal_cursor = connection.cursor()
    withdrawal_amount = ("UPDATE acountinfo SET amount = " + str(new_balance) + " WHERE idnumber = " + str(acount_number))
    withdrawal_cursor.execute(withdrawal_amount)
    withdrawal_cursor.close()

def user_check_balance_menu(acount_number):
    print(top_logo)
    balance = check_balance(acount_number)
    print("\n\n\n\nYou current balance is " + str(balance))
    input("When you would like to go back type 'back': ")

def check_balance(acount_number):
    check_balance_cursor = connection.cursor()
    get_acount_balance = ("SELECT amount FROM acountinfo WHERE idnumber = " + str(acount_number))
    check_balance_cursor.execute(get_acount_balance)
    acount_balance = check_balance_cursor.fetchall()
    check_balance_cursor.close()
    print(type(acount_balance[0][0]))
    return acount_balance[0][0]

    
def check_pin(user_input,acount_number):
    check_pin_cursor = connection.cursor()
    get_pin = ("SELECT pin FROM acountinfo WHERE idnumber = " + str(acount_number))
    check_pin_cursor.execute(get_pin)
    pin = check_pin_cursor.fetchall()
    if pin[0][0] == user_input:
        check_pin_cursor.close()
        return True
    else:
        check_pin_cursor.close()
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
        admin_menu()
    elif next_menu == "user":
        user_type = check_user_type()
        if user_type == "new":
            new_acount_menu()
        elif user_type == "existing":
            existing_acount_number_menu()
    else:
        print(top_logo)


connection.close()