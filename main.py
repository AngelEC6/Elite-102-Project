import mysql.connector
import os

connection = mysql.connector.connect(user="root",database = "elite 102 project",password = "JacktHepuG6")
connection.autocommit = True

top_logo = "=============================================================\n                   Ficticious Bank\n============================================================="
def main_menu():
    print(top_logo)
    next_menu = input("\n\n\n\nAre you a user or an administrator?: ")
    os.system('cls')
    return next_menu

def check_user_type():
    print(top_logo)
    user_type_input = input("\n\n\n\nAre you an existing or new user?: ")
    os.system('cls')
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

def admin_ID_menu():
    while True:
        try:
            print(top_logo)
            admin_id_input = input("\n\n\n\nID Number: ")
            os.system('cls')
            if admin_id_input == "Back" or admin_id_input == "back":
                return admin_id_input
            admin_id_input = int(admin_id_input)
            if type(admin_id_input) == int:
                break
        except ValueError:
            print(top_logo)
            print("\n\n\n\nThat wasn't a number please try again.")
            os.system('cls')
    passed = check_id(admin_id_input,"admin")
    os.system('cls')
    if passed == True:
        admin_pin_menu(user_id_input)
    elif user_id_input == "Back":
        return "null"
    else:
        while True:
            try:
                print(top_logo)
                admin_id_input = input("\n\n\nThat ID doesn't exist.Please try again.\nID Number: ")
                os.system('cls')
                if admin_id_input == "back":
                    return "null"
                admin_id_input = int(admin_id_input)
                passed = check_id(admin_id_input,"admin")
                os.system('cls')
                if passed == True:
                    break   
            except ValueError:
                print(top_logo)
                print("\n\n\n\nThat wasn't a number please try again.")
                os.system('cls')
        admin_pin_menu(admin_id_input)

def admin_pin_menu():
    while True:
        try:
            print(top_logo)
            admin_pin_input = input("\n\n\n\nPin: ")
            os.system('cls')
            if admin_pin_input == "back":
                return "null"
            admin_pin_input = int(admin_pin_input)
            passed = check_pin(admin_pin_input,000000,"admin")
            if passed == True:
                admin_menu()
                return "void"
            elif passed == False:
                break
        except ValueError:
            print(top_logo)
            print("\n\n\n\nThat's not a number please try again")
            os.system('cls')
    while True:
        try:
            if passed != True:
                while True:
                    print(top_logo)
                    admin_pin_input = input("\n\n\nThat pin was incorrect.Please Try again.\nPin: ")
                    os.system('cls')
                    if admin_pin_input == "back":
                        return "null"
                    admin_pin_input = int(admin_pin_input)
                    passed = check_pin(admin_pin_input,000000,"admin")
                    print(passed)
                    if passed == True:
                        break
                admin_menu()
                return "null"
        except ValueError:
            print(top_logo)
            print("\n\n\n\nThat's not a number please try again.")
            os.system('cls')

def admin_menu():
    while True:
        print(top_logo)
        admin_choice = input("\n\n\n\nWhat would you like to do (open, close, or modify an acount)?: ")
        os.system('cls')
        if admin_choice == "open":
            create_new_acount_menu("admin")
        elif admin_choice == "close":
            admin_close_menu()
        elif admin_choice == "modify":
            admin_acount_choice_modify_menu()
        elif admin_choice == "back":
            break
        else:
            while True:
                print(top_logo)
                admin_choice = input("\n\n\nSorry that is not a valid option. Please try again.\nWhat would you like to do (open, close, or modify an acount)?: ")
                os.system('cls')
                if admin_choice == "open":
                    create_new_acount_menu("admin")
                    break
                elif admin_choice == "close":
                    admin_close_menu()
                    break
                elif admin_choice == "modify":
                    admin_acount_choice_modify_menu()
                    break
                elif admin_choice == "back":
                    return "null"

def admin_close_menu():
    while True:
        try:
            print(top_logo)
            acount_to_be_delted = input("\n\n\n\nWhat is the number of the acount you would like to delete?: ")
            os.system('cls')
            if acount_to_be_delted == "back":
                return "null"
            acount_to_be_delted = int(acount_to_be_delted)
            if type(acount_to_be_delted) == int:
                break
        except ValueError:
            print(top_logo)
            print("/n/n/n/nThat is not a number please try again.")
            os.system('cls')
    passed = check_id(acount_to_be_delted,"user")
    if passed == True:
        delete_acount(acount_to_be_delted)
    elif passed != True:
        while True:
            try:
                print(top_logo)
                user_id_input = input("\n\n\nThat acount doesn't exist.Please try again.\nWhat is the number of the acount you would like to delete?: ")
                os.system('cls')
                if acount_to_be_delted == "back":
                    return "null"
                acount_to_be_delted = int(acount_to_be_delted)
                passed = check_id(acount_to_be_delted,"user")
                #os.system('cls')
                if passed == True:
                    break
            except ValueError:
                print(top_logo)
                print("\n\n\n\nThat wasn't a number please try again.")
                os.system('cls')
        delete_acount(acount_to_be_delted)

def delete_acount(acount_number):
    delete_acount_cursor = connection.cursor()
    delete_acount_code = ("DELETE FROM acountinfo WHERE idnumber = " + str(acount_number))
    delete_acount_cursor.execute(delete_acount_code)
    delete_acount_cursor.close()

def admin_acount_choice_modify_menu():
    while True:
        try:
            print(top_logo)
            acount_to_be_modified = input("\n\n\n\nWhat is the number of the acount you would like to modify?: ")
            os.system('cls')
            if acount_to_be_modified == "back":
                return "null"
            acount_to_be_modified = int(acount_to_be_modified)
            if type(acount_to_be_modified) == int:
                break
        except ValueError:
            print(top_logo)
            print("/n/n/n/nThat is not a number please try again.")
            os.system('cls')
    passed = check_id(acount_to_be_modified,"user")
    if passed == True:
        modify_acount_menu(acount_to_be_modified)
    elif passed != True:
        while True:
            try:
                print(top_logo)
                user_id_input = input("\n\n\nThat acount doesn't exist.Please try again.\nWhat is the number of the acount you would like to modify?: ")
                os.system('cls')
                if acount_to_be_modified == "back":
                    return "null"
                acount_to_be_modified = int(acount_to_be_modified)
                passed = check_id(acount_to_be_modified,"user")
                #os.system('cls')
                if passed == True:
                    break
            except ValueError:
                print(top_logo)
                print("\n\n\n\nThat wasn't a number please try again.")
                os.system('cls')
        modify_acount_menu(acount_to_be_modified)

def modify_acount_menu(acount_number):
    print(top_logo)
    modify_type = input("\n\n\n\nWhat detail would you like to modify on this acount (acount number, pin or name)?: ")
    os.system('cls')
    if modify_type == "acount number":
        modify_acount_number_menu(acount_number)
    elif modify_type == "pin":
        modify_pin_menu(acount_number)
    elif modify_type == "name":
        modify_name_menu(acount_number)
    else:
        while modify_type != "name" and modify_type != "pin" and modify_type != "acount number":
            print(top_logo)
            modify_type = input("\n\n\nSorry that isn't a valid option. Please try again.\nWhat detail would you like to modify on this acount (acount number, pin or name)?: ")
            os.system('cls')
            if modify_type == "acount number":
                modify_acount_number_menu(acount_number)
            elif modify_type == "pin":
                modify_pin_menu(acount_number)
            elif modify_type == "name":
                modify_name_menu(acount_number)

def modify_acount_number_menu(acount_number):
    while True:
        try:
            print(top_logo)
            new_acount_number = int(input("\n\n\n\nWhat would you like the acount's new number to be?: "))
            os.system('cls')
            break
        except ValueError:
            print(top_logo)
            print("\n\n\n\nThat is not a number please try again.")
            os.system('cls')
    modify_acount_number(acount_number,new_acount_number)
    print(top_logo)
    input("\n\n\n\nThe acount has been modified succesfuly please press enter once you're done: ")
    os.system('cls')

def modify_acount_number(acount_number,new_acount_number):
    modify_acount_number_cursor = connection.cursor()
    modify_acount_number_code = ("UPDATE acountinfo SET idnumber = " + str(new_acount_number) + " WHERE idnumber = " + str(acount_number))
    modify_acount_number_cursor.execute(modify_acount_number_code)
    modify_acount_number_cursor.close()

def modify_pin_menu(acount_number):
    while True:
        try:
            print(top_logo)
            new_acount_pin = int(input("\n\n\n\nWhat would you like the acount's new pin to be?: "))
            os.system('cls')
            break
        except ValueError:
            print(top_logo)
            print("\n\n\n\nThat is not a number please try again.")
            os.system('cls')
    modify_acount_pin(acount_number,new_acount_pin)
    print(top_logo)
    input("\n\n\n\nThe acount has been modified succesfuly please press enter once you're done: ")
    os.system('cls')

def modify_acount_pin(acount_number,new_acount_pin):
    modify_acount_pin_cursor = connection.cursor()
    modify_acount_pin_code = ("UPDATE acountinfo SET pin = " + str(new_acount_pin) + " WHERE idnumber = " + str(acount_number))
    modify_acount_pin_cursor.execute(modify_acount_pin_code)
    modify_acount_pin_cursor.close()

def modify_name_menu(acount_number):
    print(top_logo)
    new_acount_name = input("\n\n\n\nWhat would you like the acount's new name to be?: ")
    os.system('cls')
    modify_acount_name(acount_number,new_acount_name)
    print(top_logo)
    input("\n\n\n\nThe acount has been modified succesfuly please press enter once you're done: ")
    os.system('cls')

def modify_acount_name(acount_number,new_acount_name):
    modify_acount_name_cursor = connection.cursor()
    modify_acount_name_code = ("UPDATE acountinfo SET username = '" + new_acount_name + "' WHERE idnumber = " + str(acount_number))
    modify_acount_name_cursor.execute(modify_acount_name_code)
    modify_acount_name_cursor.close()

def new_acount_menu():
    print(top_logo)
    create_acount = input("\n\n\n\nWould you like to open a new acount?: ")
    os.system('cls')
    if create_acount == "yes":
        create_new_acount_menu("user")
    elif create_acount == "back":
        return "null"
    else:
        while True:
            print(top_logo)
            create_acount = input("\n\n\nThat is not a valid input.Please try again.\nWould you like to open a new acount?: ")
            os.system('cls')
            if create_acount == "yes":
                create_new_acount_menu("user")
                break
            elif create_acount == "back":
                return "null"

def create_new_acount_menu(menu_type):
    user_name = get_user_name(menu_type)
    pin = get_user_pin(menu_type)
    new_acount_info = create_new_acount(user_name,pin)
    print(top_logo)
    input("\n\nYour acount has been succesfully created.\nYour acount details are:\nAcount Number: " + str(new_acount_info[0][0]) + "\nPin: " + str(new_acount_info[0][1]) + "\nBalance: " + str(new_acount_info[0][2]) + "\nName: " + new_acount_info[0][3] + "\nPress enter when you're ready to move on.")
    os.system('cls')

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


def get_user_name(menu_type):
    if menu_type == "user":
        print(top_logo)
        new_user_name = input("\n\n\n\nEnter your name: ")
        os.system('cls')
        return new_user_name
    elif menu_type == "admin":
        print(top_logo)
        new_user_name = input("\n\n\n\nEnter the name the acount will be under: ")
        os.system('cls')
        return new_user_name

def get_user_pin(menu_type):
    if menu_type == "user":
        while True:
            try:
                print(top_logo)
                new_user_password = int(input("\n\n\n\nEnter your pin: "))
                os.system('cls')
                break
            except ValueError:
                print(top_logo)
                print("\n\n\n\nThat's not a number please try again.")
                os.system('cls')
        return new_user_password
    elif menu_type == "admin":
        while True:
            try:
                print(top_logo)
                new_user_password = int(input("\n\n\n\nEnter the acount's pin: "))
                os.system('cls')
                break
            except ValueError:
                print(top_logo)
                print("\n\n\n\nThat's not a number please try again.")
                os.system('cls')
        return new_user_password


def existing_acount_number_menu():
    while True:
        try:
            print(top_logo)
            user_id_input = input("\n\n\n\nAcount Number: ")
            os.system('cls')
            if user_id_input == "Back" or user_id_input == "back":
                return user_id_input
            user_id_input = int(user_id_input)
            if type(user_id_input) == int:
                break
        except ValueError:
            print(top_logo)
            print("\n\n\n\nThat wasn't a number please try again.")
            os.system('cls')
    passed = check_id(user_id_input,"user")
    #os.system('cls')
    if passed == True:
        user_pin_menu(user_id_input)
    elif user_id_input == "Back":
        return "null"
    else:
        while True:
            try:
                print(top_logo)
                user_id_input = input("\n\n\nThat acount doesn't exist.Please try again.\nAcount Number: ")
                os.system('cls')
                if user_id_input == "back":
                    return "null"
                user_id_input = int(user_id_input)
                passed = check_id(user_id_input,"user")
                #os.system('cls')
                if passed == True:
                    break
            except ValueError:
                print(top_logo)
                print("\n\n\n\nThat wasn't a number please try again.")
                os.system('cls')
        user_pin_menu(user_id_input)
    
def user_pin_menu(acount_number):
    while True:
        try:
            print(top_logo)
            user_pin_input = input("\n\n\n\nPin: ")
            os.system('cls')
            if user_pin_input == "back":
                return "null"
            user_pin_input = int(user_pin_input)
            passed = check_pin(user_pin_input,acount_number,"user")
            if passed == True:
                existing_user_menu(acount_number)
                return "void"
        except ValueError:
            print(top_logo)
            print("\n\n\n\nThat's not a number please try again")
            os.system('cls')
    while True:
        try:
            if passed != True:
                while True:
                    print(top_logo)
                    user_pin_input = input("\n\n\nThat pin was incorrect.Please Try again.\nPin: ")
                    os.system('cls')
                    if user_pin_input == "back":
                        return "null"
                    user_pin_input = int(user_pin_input)
                    passed = check_pin(user_pin_input,acount_number,"user")
                    if passed == True:
                        break
                existing_user_menu(acount_number)
                return "null"
        except ValueError:
            print(top_logo)
            print("\n\n\n\nThat's not a number please try again.")
            os.system('cls')

def existing_user_menu(acount_number):
    while True:
        print(top_logo)
        user_choice = input("\n\n\n\nWhat would you like to do (deposit,withdrawal,check balance,)?: ")
        os.system('cls')
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
                os.system('cls')
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
            os.system('cls')
            if user_deposit_input == "back":
                return "null"
            user_deposit_input = float(user_deposit_input)
            break
        except ValueError:
            print(top_logo)
            print("\n\n\n\nThat is not a valid input. Please try again.")
            os.system('cls')
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
            os.system('cls')
            if user_withdrawal_input == "back":
                return "null"
            user_withdrawal_input = float(user_withdrawal_input)
            break
        except ValueError:
            print(top_logo)
            print("\n\n\n\nThat is not a valid input. Please try again.")
            os.system('cls')
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
    os.system('cls')

def check_balance(acount_number):
    check_balance_cursor = connection.cursor()
    get_acount_balance = ("SELECT amount FROM acountinfo WHERE idnumber = " + str(acount_number))
    check_balance_cursor.execute(get_acount_balance)
    acount_balance = check_balance_cursor.fetchall()
    check_balance_cursor.close()
    return acount_balance[0][0]

    
def check_pin(user_input,acount_number,check_type):
    if check_type == "user":
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
    elif check_type == "admin":
        check_pin_cursor = connection.cursor()
        get_pin = ("SELECT pin FROM acountinfo WHERE idnumber = 23568")
        check_pin_cursor.execute(get_pin)
        pin = check_pin_cursor.fetchall()
        if pin[0][0] == user_input:
            check_pin_cursor.close()
            return True
        else:
            check_pin_cursor.close()
            return False
    

def check_id(user_input,check_type):
    if check_type == "user":
        check_number = connection.cursor()
        get_numbers = ("SELECT idnumber FROM acountinfo")
        check_number.execute(get_numbers)
        acount_numbers = check_number.fetchall()    
        for number in acount_numbers:
            if number[0] == user_input:
                check_number.close()
                return True
        check_number.close()
        return False
    if check_type == "admin":
        check_number = connection.cursor()
        get_number = ("SELECT idnumber FROM acountinfo WHERE id = 23568")
        check_number.execute(get_number)
        acount_number = check_number.fetchall()
        if acount_number[0][0] == user_input:
            check_number.close()
            return True
        elif acount_number[0][0] != user_input:
            check_number.close()
            return False 
        

while True:
    next_menu = main_menu()
    #os.system('cls')
    if next_menu == "administrator":
        admin_pin_menu()
    elif next_menu == "user":
        user_type = check_user_type()
        if user_type == "new":
            new_acount_menu()
        elif user_type == "existing":
            existing_acount_number_menu()
    elif next_menu == "back":
        break


connection.close()