from getpass import getpass
from user import Users
from meal import Meal as Meal
import file_interactions
from bill import Bill
import planning

path_user = "database/users.csv"
path_meal = "database/meal.csv"
path_bill = "database/bill.csv"
path_planning = "database/planning.csv"
user_list = file_interactions.read_file_user(path_user)
meal_list = file_interactions.read_file_meal(path_meal)
bill_list = file_interactions.read_file_bill(path_bill)
planning_list = planning.init_planning(path_planning)


def connection():
    """This function allows the user to connect of his page
    PRE: the introduction() function was started before
    POST: connect user on page  user_connected(username) or restart the introduction()
    """
    print("------ login-----")
    user_connexion = input("Type your username\n")
    user_connexion_pwd = getpass("Type your password\n")
    ask_user = input(
        "Type:\n 1 log in as user.\n 2 log in as cooker.\n")
    while ask_user != "1" and ask_user != "2":
        ask_user = input(
            "Type:\n 1 log in as user.\n 2 log in as cooker.\n")
    if len(user_list) > 0:
        flag_found = False
        for user in user_list:
            if user_connexion != user.username:
                continue
            flag_found = True
            if user.is_correct_password(user_connexion_pwd) and ask_user == "2":
                print("cooker connected")
                cooker_connected(user.username)
            elif user.is_correct_password(user_connexion_pwd) and ask_user == "1":
                print("user connected")
                user_connected(user.username)
            else:
                print("invalid pwd or user")
                introduction()
        if flag_found is False:
            print("invalid pwd or user")
            introduction()
    else:
        print("you don't have an account yet please register")
        introduction()


def registration():
    """This function allows to register a user on database
    PRE: the introduction() function was started before
    POST: create user on database or restart the introduction()
    """
    print("------registration-----")
    user_registration = str(input("Type a username\n"))
    user_registration_pwd = getpass("Type a password\n")
    user_registration_pwd_confirmation = getpass("Retype the password to confirm\n")
    if user_registration_pwd == user_registration_pwd_confirmation:
        tmp_user_registration = Users(user_registration)
        tmp_user_registration.change_password(user_registration_pwd)
        file_interactions.add_user_database(tmp_user_registration, user_list)
        file_interactions.write_file_user(path_user, user_list)
        introduction()
    else:
        print("you did not enter the same password")
        introduction()


def delete_user():
    """This function allows to delete a user on database
    PRE: the introduction() function was started before
    POST: delete user on database or restart the introduction()
    """
    user_to_delete = str(input("Type the username of the account you want to delete\n"))
    user_to_delete_pwd = str(input("Are you sure to delete your account ? Type your password to delete it\n"))
    for user in user_list:
        if user.username == user_to_delete and user.is_correct_password(user_to_delete_pwd):
            file_interactions.delete_user_database(Users(user_to_delete), user_list)
            file_interactions.write_file_user(path_user, user_list)
            print("your account has been deleted")
            introduction()
    else:
        print("wrong password")
        introduction()


def introduction():
    """This function is the introduction at the launch of the program
    PRE: The user launched the program
    POST: initiate login, registration, delete a user or exit program
    """
    print("-----Welcome on user connexion-----")
    introduction_connexion = input(
        "Type:\n 1 log in.\n 2 register.\n 3 delete account\n 4 reset invoices to 0.\n 5 exit the program.\n")
    while introduction_connexion != "1" and introduction_connexion != "2" and introduction_connexion != "3" \
            and introduction_connexion != "4" and introduction_connexion != "5":
        introduction_connexion = input(
            "Type:\n 1 log in.\n 2 register.\n 3 delete account\n 4 reset invoices to 0.\n 5 exit the program.\n")
    if introduction_connexion == "1":
        connection()
    elif introduction_connexion == "2":
        registration()
    elif introduction_connexion == "3":
        delete_user()
    elif introduction_connexion == "4":
        for bill_in in bill_list:
            bill_in.price = 0
            bill_in.payBill()
        file_interactions.write_file_bill(path_bill, bill_list)
        print("the invoices have been reset to 0")
        introduction()
    elif introduction_connexion == "5":
        exit()


def user_connected(username):
    """allows the user when he is connected to interact with the program: see the calendar, register or
    unsubscribe for the meal of the day, see your bill, change your password or disconnect
    PRE: the user has been connected using the connection() function
    :username, the username of the logged-in user (string)
    POST: the user can interact with the program
    """
    # get index of User object in list to work on it
    index_user = 0
    for user in user_list:
        if username == user.username:
            index_user = user_list.index(user)

    file_interactions.add_bill_database(Bill(username, 0), bill_list)
    file_interactions.write_file_bill(path_bill, bill_list)

    index_bill = 0
    for bill in bill_list:
        if username == bill.username:
            index_bill = bill_list.index(bill)

    print("-----Welcome on dining kot manager-----")
    choice_task = input(
        "Type:\n 1 see the schedule.\n 2 register for a meal.\n 3 unsubscribe to a meal."
        "\n 4 see invoice.\n 5 change password.\n 6 Sign out.\n")
    while choice_task != "1" and choice_task != "2" and choice_task != "3" \
            and choice_task != "4" and choice_task != "5" and choice_task != "6":
        choice_task = input(
            "Type:\n 1 see the schedule.\n 2 register for a meal.\n 3 unsubscribe to meal of the day."
            "\n 4 see invoice.\n 5 change password.\n 6 Sign out.\n")
    if choice_task == "1":
        # see the schedule of cooker
        if len(planning_list) > 0:
            print("------Planning of the Week------")
            for plan in planning_list:
                print("Cooker : " + plan.username + " | Date : " + plan.date)
        else:
            print("There is no planning for now")
        user_connected(username)
    elif choice_task == "2":
        # register for a meal
        meal_date = input("Enter the date of the meal you want to attend (dd-mm-yyyy)\n")
        if len(meal_list) > 0:
            for meal_in in meal_list:
                if meal_in.date == meal_date and user_list[index_user].username not in meal_in.participants:
                    print(f"here is the meal: {meal_in._description}")
                    confirm_meal = input("are you sure to participate, Type 'yes' to confirm or other to quit\n")
                    if confirm_meal == "yes":
                        if user_list[index_user].username not in meal_in.participants:
                            bill_list[index_bill].price = int(bill_list[index_bill].price) - int(meal_in.price_by_user)
                            index_cooker = 0
                            for bill in bill_list:
                                if meal_in.cooker == bill.username:
                                    index_cooker = bill_list.index(bill)
                            bill_list[index_cooker].price = \
                                int(bill_list[index_cooker].price) + int(meal_in.price_by_user)
                        else:
                            print("You are already registered")
                            user_connected(username)
                        meal_in.subscribe(user_list[index_user])
                        file_interactions.write_file_meal(path_meal, meal_list)
                        file_interactions.write_file_bill(path_bill, bill_list)
                        print("you have been registered")
                        user_connected(username)
                        user_connected(username)
                    else:
                        user_connected(username)
                else:
                    print("invalid date")
                    user_connected(username)
            print("no meals have been registered yet")
            user_connected(username)

    elif choice_task == "3":
        # unsubscribe to a meal
        if len(meal_list) > 0:
            for meal_in in meal_list:
                meal_date = input("Enter the date of the meal you want to unsubscribe (dd-mm-yyyy)")
                if meal_in.date == meal_date and user_list[index_user].username not in meal_in.participants:
                    if user_list[index_user].username not in meal_in.participants:
                        bill_list[index_bill].price = int(bill_list[index_bill].price) + int(meal_in.price_by_user)
                    index_cooker = 0
                    for bill in bill_list:
                        if meal_in.cooker == bill.username:
                            index_cooker = bill_list.index(bill)
                    bill_list[index_cooker].price = int(bill_list[index_cooker].price) - int(meal_in.price_by_user)
                    meal_in.unsubscribe(user_list[index_user])
                    file_interactions.write_file_meal(path_meal, meal_list)
                    file_interactions.write_file_bill(path_bill, bill_list)
                else:
                    print("you are already registered or the meal does not exist")
        user_connected(username)

    elif choice_task == "4":
        bill_list[index_bill].get_bill()
        user_connected(username)
    elif choice_task == "5":
        # change the user's password if he confirms with his old password
        user_old_pwd = str(input("Type the old password\n"))
        if user_list[index_user].is_correct_password(user_old_pwd):
            pass
        else:
            print(f"invalid pwd for {user_list[index_user].username}")
        user_new_pwd = str(input("Type the new password \n"))
        confirm = str(input("Type yes to confirm or something else to quit\n"))
        if confirm == "yes":
            user_list[index_user].change_password(user_new_pwd, user_old_pwd)
            file_interactions.write_file_user(path_user, user_list)
            print("The password has been changed")
            user_connected(username)
        else:
            user_connected(username)
    elif choice_task == "6":
        # relaunches the introduction function
        introduction()


def cooker_connected(username):
    """allows the cooker when he is connected to interact with the program: see the calendar, register or
    unsubscribe for the meal of the day, see your bill, change your password or disconnect
    PRE: the user has been connected using the connection() function
    :username, the username of the logged-in cooker (string)
    POST: the cooker can interact with the program
    """
    # get index of User object in list to work on it
    index_user = 0
    for user in user_list:
        if username == user.username:
            index_user = user_list.index(user)

    index_bill_cooker = 0
    for bill in bill_list:
        if username == bill.username:
            index_bill_cooker = bill_list.index(bill)

    file_interactions.add_bill_database(Bill(user_list[index_user].username, 0), bill_list)
    for bill in bill_list:
        print(bill.username)
    file_interactions.write_file_bill(path_bill, bill_list)

    print("-----Welcome on dining kot manager-----")
    choice_task = input(
        "Type:\n 1 see the schedule.\n 2 Define the meal (price and description).\n "
        "3 see invoice.\n 4 change password.\n 5 Sign out.\n")
    while choice_task != "1" and choice_task != "2" and choice_task != "3" \
            and choice_task != "4" and choice_task != "5":
        choice_task = input(
            "Type:\n 1 see the schedule.\n 2 Define the meal of the day (price and description).\n "
            "3 see invoice.\n 4 change password.\n 5 Sign out.\n")
    if choice_task == "1":
        # see the schedule of cooker
        if len(planning_list) > 0:
            print("------Planning of the Week------")
            for plan in planning_list:
                print("Cooker : " + plan.username + " | Date : " + plan.date)
        else:
            print("There is no planning for now")
        cooker_connected(username)
    elif choice_task == "2":
        #  Define the meal
        tmp_planning_list = []
        print("------Meal-----")
        if len(planning_list) < 1:
            define_schedule = input("Are you sure to create a schedule ? Type 'yes' to create a schedule based on users"
                                    "already created \n")
            if define_schedule == "yes":
                d_day = planning.DDay()
                planning.get_planning(user_list, planning_list, d_day)
                tmp_planning_list = planning.init_planning(path_planning)
            else:
                cooker_connected(username)
        tmp_user_cooker = []
        for plan_cook in tmp_planning_list:
            tmp_user_cooker.append(plan_cook.username)
        if user_list[index_user].username not in tmp_user_cooker and len(tmp_user_cooker) > 0:
            print("you are not cooked this week come back another time")
            introduction()
        meal_description = input("Type the description of the meal\n")
        meal_price = int(input("Type the price of the meal\n"))
        date_cooker = ""
        number_meal = 0
        tmp_planning = planning.init_planning(path_planning)
        for date_planning in tmp_planning_list:
            if len(tmp_planning) < 1:
                print("no definite schedule yet")
            else:
                if user_list[index_user].username == date_planning.username:
                    number_meal += 1
        if number_meal > 1:
            print("you are a cook several times, for what date do you want to define the meal ? Here the planning:")
            print("------Planning of the Week------")
            for plan in tmp_planning:
                print("Cooker : " + plan.username + " | Date : " + plan.date)
            choice_date_cooker = input("Type the date of the meal to define (dd-mm-yyyy): \n")
            tmp_user_date = []
            for plan_by_user in tmp_planning_list:
                if plan_by_user.username == user_list[index_user].username:
                    tmp_user_date.append(plan_by_user.date)
            while choice_date_cooker not in tmp_user_date:
                choice_date_cooker = input(
                    "Type the date of the meal to define (dd-mm-yyyy): \n")
            tmp_meal_definition = Meal(meal_description, choice_date_cooker, user_list[index_user].username, meal_price)
            file_interactions.add_meal_database(tmp_meal_definition, meal_list)
            file_interactions.write_file_meal(path_meal, meal_list)
            cooker_connected(username)
        else:
            for date_planning in tmp_planning:
                date_cooker = date_planning.date
            tmp_meal_definition = Meal(meal_description, date_cooker, user_list[index_user].username, meal_price)
            file_interactions.add_meal_database(tmp_meal_definition, meal_list)
            file_interactions.write_file_meal(path_meal, meal_list)
            cooker_connected(username)
    elif choice_task == "3":
        # print the bill
        bill_list[index_bill_cooker].get_bill()
        cooker_connected(username)
    elif choice_task == "4":
        # change cooker password
        user_old_pwd = str(input("Type the old password\n"))
        if user_list[index_user].is_correct_password(user_old_pwd):
            pass
        else:
            print(f"invalid pwd for {user_list[index_user].username}")
        user_new_pwd = str(input("Type the new password \n"))
        confirm = str(input("Type yes to confirm or something else to quit\n"))
        if confirm == "yes":
            user_list[index_user].change_password(user_new_pwd, user_old_pwd)
            file_interactions.write_file_user(path_user, user_list)
            print("The password has been changed")
            introduction()
        else:
            cooker_connected(username)
    elif choice_task == "5":
        # Sign out
        introduction()


if __name__ == '__main__':
    introduction()
