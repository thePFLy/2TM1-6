import random
import csv
from datetime import datetime, timedelta
import logging
from class_plan import Planning


def DDay():
    """
    initiate the date stored in DDay.csv
    PRE : csv file DDay.csv
    POST : the date in DDay.csv
    RAISE : ValueError if the csv is empty
    """
    try:
        with open('database/DDay.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                return datetime.strptime(row["Date"], "%d-%m-%Y")
    except IOError:
        logging.exception('')
    if not reader:
        raise ValueError('No data available')


def newDDay():
    """
    change the date stored in DDay.csv with the date of today
    PRE : csv file DDay.csv
    POST : new date stored in DDay.csv
    """
    new_date = datetime.today()
    formatted_date = new_date.strftime('%d-%m-%Y')
    try:
        with open('database/DDay.csv', 'w') as csvfile:
            fieldnames = ['Date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Date': "Date"})
            writer.writerow({'Date': formatted_date})
    except OSError as e:
        print(type(e), e)


def init_planning(path: str):
    """
    initialise a list of Day associated with a User
    to determine the day of cooking
    PRE :
    :path, string path a csv file planning.csv
    POST : a list of list with day and the name of the user
    RAISE : ValueError if the csv is empty
    """
    try:
        planning = []
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                day = Planning(row["Name"], row["Day"])
                planning.append(day)
        return planning
    except IOError:
        logging.exception('')
    if not reader:
        raise ValueError('No data available')


def change_planning(week_plan):
    """
    change the current planning in the planning.csv file with a new planning
    PRE :
    :week_plan, list of day and user
    POST : a new planning in the planning.csv file
    """
    try:
        with open('database/planning.csv', 'w') as csvfile:
            fieldnames = ['Day', 'Name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(
                {'Day': 'Day', 'Name': 'Name'})
            for i in week_plan:
                writer.writerow({'Day': i[1].strftime('%d-%m-%Y'), 'Name': i[0]})
    except OSError as e:
        print(type(e), e)


def get_planning(students, planning, day):
    """
    a function that creates a schedule, selects 7 students or fewer, and spreads them over 7 days starting today
    PRE :
    :students, list of object User
    :planning, list of day with User
    :day, a date
    POST : create a planning
    RAISE : Exception if the list of object user is empty
    """
    global week
    today = datetime.today()
    difference = today - day
    # if there is already a cooker, it deletes his cooker status (cooker = False)
    for day in planning:
        for student in students:
            if day.username == student.username:
                if student._cooker:
                    student._cooker = False

    for day in planning:
        for student in students:
            if day.date == day:
                if day.username == student.username:
                    student._cooker = True

    if difference.days >= 7:
        newDDay()
        print("A change in the schedule has taken place")
        if len(students) >= 7:
            # Choose 7 random students
            selected_students = random.sample(students, 7)
            # Mixing selected students
            random.shuffle(selected_students)
        else:
            selected_students = students

        if len(students) == 0:
            raise Exception("Error : The list of users is empty")
        # Spreading the students over the different days of the week
        if len(selected_students) == 1:
            day1 = [selected_students[0].username, today]
            day2 = [selected_students[0].username, today + timedelta(days=1)]
            day3 = [selected_students[0].username, today + timedelta(days=2)]
            day4 = [selected_students[0].username, today + timedelta(days=3)]
            day5 = [selected_students[0].username, today + timedelta(days=4)]
            day6 = [selected_students[0].username, today + timedelta(days=5)]
            day7 = [selected_students[0].username, today + timedelta(days=6)]
            week = [day1, day2, day3, day4, day5, day6, day7]
        if len(selected_students) == 2:
            day1 = [selected_students[0].username, today]
            day2 = [selected_students[1].username, today + timedelta(days=1)]
            day3 = [selected_students[0].username, today + timedelta(days=2)]
            day4 = [selected_students[1].username, today + timedelta(days=3)]
            day5 = [selected_students[0].username, today + timedelta(days=4)]
            day6 = [selected_students[1].username, today + timedelta(days=5)]
            day7 = [selected_students[0].username, today + timedelta(days=6)]
            week = [day1, day2, day3, day4, day5, day6, day7]
        if len(selected_students) == 3:
            day1 = [selected_students[0].username, today]
            day2 = [selected_students[1].username, today + timedelta(days=1)]
            day3 = [selected_students[2].username, today + timedelta(days=2)]
            day4 = [selected_students[0].username, today + timedelta(days=3)]
            day5 = [selected_students[1].username, today + timedelta(days=4)]
            day6 = [selected_students[2].username, today + timedelta(days=5)]
            day7 = [selected_students[0].username, today + timedelta(days=6)]
            week = [day1, day2, day3, day4, day5, day6, day7]
        if len(selected_students) == 4:
            day1 = [selected_students[0].username, today]
            day2 = [selected_students[1].username, today + timedelta(days=1)]
            day3 = [selected_students[2].username, today + timedelta(days=2)]
            day4 = [selected_students[3].username, today + timedelta(days=3)]
            day5 = [selected_students[0].username, today + timedelta(days=4)]
            day6 = [selected_students[1].username, today + timedelta(days=5)]
            day7 = [selected_students[2].username, today + timedelta(days=6)]
            week = [day1, day2, day3, day4, day5, day6, day7]
        if len(selected_students) == 5:
            day1 = [selected_students[0].username, today]
            day2 = [selected_students[1].username, today + timedelta(days=1)]
            day3 = [selected_students[3].username, today + timedelta(days=2)]
            day4 = [selected_students[4].username, today + timedelta(days=3)]
            day5 = [selected_students[2].username, today + timedelta(days=4)]
            day6 = [selected_students[1].username, today + timedelta(days=5)]
            day7 = [selected_students[3].username, today + timedelta(days=6)]
            week = [day1, day2, day3, day4, day5, day6, day7]
        if len(selected_students) == 6:
            day1 = [selected_students[0].username, today]
            day2 = [selected_students[4].username, today + timedelta(days=1)]
            day3 = [selected_students[1].username, today + timedelta(days=2)]
            day4 = [selected_students[2].username, today + timedelta(days=3)]
            day5 = [selected_students[5].username, today + timedelta(days=4)]
            day6 = [selected_students[3].username, today + timedelta(days=5)]
            day7 = [selected_students[0].username, today + timedelta(days=6)]
            week = [day1, day2, day3, day4, day5, day6, day7]
        if len(selected_students) > 6:
            day1 = [selected_students[0].username, today]
            day2 = [selected_students[1].username, today + timedelta(days=1)]
            day3 = [selected_students[2].username, today + timedelta(days=2)]
            day4 = [selected_students[3].username, today + timedelta(days=3)]
            day5 = [selected_students[4].username, today + timedelta(days=4)]
            day6 = [selected_students[5].username, today + timedelta(days=5)]
            day7 = [selected_students[6].username, today + timedelta(days=6)]
            week = [day1, day2, day3, day4, day5, day6, day7]
        students[0]._cooker = True
        change_planning(week)
    else:
        pass
