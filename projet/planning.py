import random
from user import Users
import csv
from datetime import datetime, date, timedelta
import logging


def DDay():
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
    newdate = datetime.today()
    formatted_date = newdate.strftime('%d-%m-%Y')
    try:
        with open('database/DDay.csv', 'w') as csvfile:
            fieldnames = ['Date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Date': "Date"})
            writer.writerow({'Date': formatted_date})
    except OSError as e:
        print(type(e), e)

def init_planning():
    try:
        planning = []
        with open('database/planning.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sous_plan = []
                sous_plan.append(datetime.strptime(row["Day"], "%d-%m-%Y"))
                sous_plan.append(row["Name"])
                planning.append(sous_plan)
        return planning
    except IOError:
        logging.exception('')
    if not reader:
        raise ValueError('No data available')

def change_planning(week):
    try:
        with open('database/planning.csv', 'w') as csvfile:
            fieldnames = ['Day', 'Name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(
                {'Day': 'Day', 'Name': 'Name'})
            for i in week:
                writer.writerow({'Day': i[1].strftime('%d-%m-%Y'), 'Name': i[0]})
    except OSError as e:
        print(type(e), e)




def get_planning(students,planning):
    today = datetime.today()
    today_date = today.strftime('%d-%m-%Y')
    difference = today - DDay
    #if there is already a cooker, it delete his cooker status (cooker = False)
    for day in the_planning:
        for student in etudiants:
            if day[1] == student.username:
                if student._cooker == True:
                    student._cooker = False

    for day in the_planning:
        for student in etudiants:
            if day[0] == DDay:
                if day[1] == student.username:
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

        # Spreading the students over the different days of the week
        if len(selected_students) == 1:
            day1 = [selected_students[0].username,today]
            day2 = [selected_students[0].username,today+timedelta(days=1)]
            day3 = [selected_students[0].username,today+timedelta(days=2)]
            day4 = [selected_students[0].username,today+timedelta(days=3)]
            day5 = [selected_students[0].username,today+timedelta(days=4)]
            day6 = [selected_students[0].username,today+timedelta(days=5)]
            day7 = [selected_students[0].username,today+timedelta(days=6)]
            week = [day1,day2,day3,day4,day5,day6,day7]
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
        change_planning(week)
    else:
        pass



DDay = DDay()
the_planning = init_planning()

# test
user1 = Users('brice', '0000')
user2 = Users('ronald', '0001')
user3 = Users('toto', '0002')
user4 = Users('tata', '0003')
etudiants = [user1,user2,user3,user4]
get_planning(etudiants,the_planning)
    """
    for day in the_planning:
        for student in etudiants:
            if day[1] == student.username:
                if student._cooker == True:
                    student._cooker = False
    
    for day in the_planning:
        for student in etudiants:
            if day[0] == DDay:
                if day[1] == student.username:
                    student._cooker = True
    
    for i in etudiants:
        print(i._cooker)
    """
