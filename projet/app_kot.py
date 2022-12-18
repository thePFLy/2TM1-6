from getpass import getpass
import user as userclass
# import meal
# import Ingredient
# import bill

path_database = "database/users.csv"
user_list = userclass.read_file(path_database)


def user_connected():
    print("-----Welcome on dining kot manager-----")
    choice_task = int(input(
        "Type:\n  1 see the schedule.\n  2 register for the meal of the day.\n  3 unsubscribe to meal of the day.\n 4 see invoice.\n 5 change password.\n 6 Sign out.\n 7 Sign out.\n"))
    while choice_task < 1 and choice_task > 8:
        choice_task = int(input(
             "Type:\n  1 see the schedule.\n  2 register for the meal of the day.\n  3 unsubscribe to meal of the day.\n 4 see invoice.\n 5 change password.\n 6 Sign out.\n 7 Sign out.\n"))
    if choice_task == 1:
        connection()
    elif choice_task == 2:
        registration()
    elif choice_task == 3:
        delete_user()
    elif choice_task == 4:
        delete_user()
    elif choice_task == 5:
        delete_user()
    elif choice_task == 6:
        delete_user()
    elif choice_task == 7:
        delete_user()


def connection():
    print("------ login-----")
    user_connexion = str(input("Type your username\n"))
    user_connexion_pwd = str(input("Type your password\n"))
    for user in user_list:
        if user.username == user_connexion and user.is_correct_password(user_connexion_pwd):
            print("connected")
            user_connected()
        else:
            print("invalid pwd or user")
            introduction()


def registration():
    print("------registration-----")
    user_registration = str(input("Type a username\n"))
    user_registration_pwd = str(input("Type a password\n"))
    user_registration_pwd_confirmation = str(input("Retype the password to confirm\n"))
    if user_registration_pwd == user_registration_pwd_confirmation:
        tmp_user_registration = userclass.Users(user_registration)
        tmp_user_registration.change_password(user_registration_pwd)
        userclass.add_user_database(tmp_user_registration, user_list)
        userclass.write_file(path_database, user_list)
    else:
        print("you did not enter the same password")


def delete_user():
    user_to_delete = str(input("Type the username of the account you want to delete\n"))
    user_to_delete_pwd = str(input("Are you sure to delete your account ? Type your password to delete it\n"))
    if userclass.Users(user_to_delete).is_correct_password(user_to_delete_pwd):
        userclass.delete_user_database(userclass.Users(user_to_delete), user_list)


def introduction():
    print("-----Welcome on user connexion-----")
    introduction_connexion = int(input(
        "Type:\n  1 log in.\n  2 register.\n  3 delete account.\n 4 exit the program.\n"))
    while introduction_connexion != 1 and introduction_connexion != 2 and introduction_connexion != 3:
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


if __name__ == '__main__':
    introduction()
