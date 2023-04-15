import mysql.connector
import os

connection = mysql.connector.connect(user="root",database = "elite 102 project",password = "JacktHepuG6")


top_logo = "=============================================================\n                   Ficticious Bank\n============================================================="
def main_menu():
    print(top_logo)
    next_menu = input("\n\n\n\nAre you a user or an administrator? : ")
    return next_menu
    
def user_menu():
    print(top_logo)
    user_id_input = input("\n\n\n\nAcount Number: ")
    passed = check_id(user_id_input)
    #os.system('cls')
    if passed == True:
        password_menu()
    elif user_id_input == "Back":
        print("")
    else:
        while True:
            print(top_logo)
            user_id_input = input("\n\n\nThat acount doesn't exist.Please try again.\nAcount Number: ")
            passed = check_id(user_id_input)
            #os.system('cls')
            if passed == True:
                break
        print("tried again")
    
def password_menu():
    print("password menu")


def check_id(user_input):
    check_number = connection.cursor()
    get_number = ("SELECT idnumber FROM acountinfo")
    check_number.execute(get_number)
    acount_number = check_number.fetchall()
    for number in acount_number:
        print(number)
        if number[0] == int(user_input):
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
        user_menu()
    else:
        print(top_logo)


connection.close()