def menu():
    print("=============================================================")
    next_menu = input("\n\n\n\n           Are you a user or an administrator: ")
    return next_menu
    


while True:
    next_menu = menu()
    cls
    if next_menu == "administrator":
        print("=============================================================")
        admin_username = input("\n\n\n\n             Username: ")
        if type(admin_username) == str:
            break
    elif next_menu == "administrator":
        print("=============================================================")
        user_username = input("\n\n\n\n             Username: ")
        if type(user_username) == str:
            break
