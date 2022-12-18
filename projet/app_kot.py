from getpass import getpass
import user as user_class
# import meal
# import Ingredient
# import bill
# import planning

path_database = "database/users.csv"
user_list = user_class.read_file(path_database)
user_online = ""


def connection():
    print("------ login-----")
    user_connexion = str(input("Type your username\n"))
    user_connexion_pwd = str(getpass("Type your password\n"))
    for user in user_list:
        if user.username == user_connexion and user.is_correct_password(user_connexion_pwd):
            print("connected")
            user_connected(user.username)
        else:
            print("invalid pwd or user")
            introduction()


def registration():
    print("------registration-----")
    user_registration = str(input("Type a username\n"))
    user_registration_pwd = str(getpass("Type a password\n"))
    user_registration_pwd_confirmation = str(getpass("Retype the password to confirm\n"))
    if user_registration_pwd == user_registration_pwd_confirmation:
        tmp_user_registration = user_class.Users(user_registration)
        tmp_user_registration.change_password(user_registration_pwd)
        user_class.add_user_database(tmp_user_registration, user_list)
        user_class.write_file(path_database, user_list)
    else:
        print("you did not enter the same password")
        introduction()


def delete_user():
    user_to_delete = str(input("Type the username of the account you want to delete\n"))
    user_to_delete_pwd = str(input("Are you sure to delete your account ? Type your password to delete it\n"))
    if user_class.Users(user_to_delete).is_correct_password(user_to_delete_pwd):
        user_class.delete_user_database(user_class.Users(user_to_delete), user_list)


def introduction():
    print("-----Welcome on user connexion-----")
    introduction_connexion = int(input(
        "Type:\n  1 log in.\n  2 register.\n  3 delete account.\n 4 exit the program.\n"))
    while introduction_connexion != 1 and introduction_connexion != 2 and introduction_connexion != 3 \
            and introduction_connexion != 4:
        introduction_connexion = int(input(
            "Type:\n  1 log in.\n  2 register.\n  3 exit the program\n"))
    if introduction_connexion == 1:
        connection()
    elif introduction_connexion == 2:
        registration()
    elif introduction_connexion == 3:
        delete_user()
    elif introduction_connexion == 4:
        exit()


def user_connected(username):
    index_user = 0
    for user in user_list:
        if username == user.username:
            index_user = user_list.index(user)
    print(user_list[index_user].username)
    print("-----Welcome on dining kot manager-----")
    choice_task = int(input(
        "Type:\n  1 see the schedule.\n  2 register for the meal of the day.\n  3 unsubscribe to meal of the day."
        "\n 4 see invoice.\n 5 change password.\n 6 Sign out.\n"))
    while 1 > choice_task > 8:
        choice_task = int(input(
             "Type:\n  1 see the schedule.\n  2 register for the meal of the day.\n  3 unsubscribe to meal of the day."
             "\n 4 see invoice.\n 5 change password.\n 6 Sign out.\n"))
    if choice_task == 1:
        pass
    elif choice_task == 2:
        pass
    elif choice_task == 3:
        pass
    elif choice_task == 4:
        pass
    elif choice_task == 5:
        user_old_pwd = str(input("Type the old password\n"))
        if user_list[index_user].is_correct_password(user_old_pwd):
            pass
        else:
            print(f"invalid pwd for {user_list[index_user].username}")
        user_new_pwd = str(input("Type the new password \n"))
        confirm = str(input("Type yes to confirm or something else to quit\n"))
        if confirm == "yes":
            user_list[index_user].change_password(user_new_pwd, user_old_pwd)
            user_class.write_file(path_database, user_list)
        else:
            user_connected(username)
    elif choice_task == 6:
        introduction()


if __name__ == '__main__':
    introduction()