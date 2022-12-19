import random
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




def planning(students):
    today = datetime.today()
    today_date = today.strftime('%d-%m-%Y')
    difference = today - DDay
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
            day1 = [selected_students[0],today]
            day2 = [selected_students[0],today+timedelta(days=1)]
            day3 = [selected_students[0],today+timedelta(days=2)]
            day4 = [selected_students[0],today+timedelta(days=3)]
            day5 = [selected_students[0],today+timedelta(days=4)]
            day6 = [selected_students[0],today+timedelta(days=5)]
            day7 = [selected_students[0],today+timedelta(days=6)]
            week = [day1,day2,day3,day4,day5,day6,day7]
        if len(selected_students) == 2:
            day1 = [selected_students[0], today]
            day2 = [selected_students[1], today + timedelta(days=1)]
            day3 = [selected_students[0], today + timedelta(days=2)]
            day4 = [selected_students[1], today + timedelta(days=3)]
            day5 = [selected_students[0], today + timedelta(days=4)]
            day6 = [selected_students[1], today + timedelta(days=5)]
            day7 = [selected_students[0], today + timedelta(days=6)]
            week = [day1, day2, day3, day4, day5, day6, day7]
        if len(selected_students) == 3:
            day1 = [selected_students[0], today]
            day2 = [selected_students[1], today + timedelta(days=1)]
            day3 = [selected_students[2], today + timedelta(days=2)]
            day4 = [selected_students[0], today + timedelta(days=3)]
            day5 = [selected_students[1], today + timedelta(days=4)]
            day6 = [selected_students[2], today + timedelta(days=5)]
            day7 = [selected_students[0], today + timedelta(days=6)]
            week = [day1, day2, day3, day4, day5, day6, day7]
        if len(selected_students) == 4:
            day1 = [selected_students[0], today]
            day2 = [selected_students[1], today + timedelta(days=1)]
            day3 = [selected_students[2], today + timedelta(days=2)]
            day4 = [selected_students[3], today + timedelta(days=3)]
            day5 = [selected_students[0], today + timedelta(days=4)]
            day6 = [selected_students[1], today + timedelta(days=5)]
            day7 = [selected_students[2], today + timedelta(days=6)]
            week = [day1, day2, day3, day4, day5, day6, day7]
        if len(selected_students) == 5:
            day1 = [selected_students[0], today]
            day2 = [selected_students[1], today + timedelta(days=1)]
            day3 = [selected_students[3], today + timedelta(days=2)]
            day4 = [selected_students[4], today + timedelta(days=3)]
            day5 = [selected_students[2], today + timedelta(days=4)]
            day6 = [selected_students[1], today + timedelta(days=5)]
            day7 = [selected_students[3], today + timedelta(days=6)]
            week = [day1, day2, day3, day4, day5, day6, day7]
        if len(selected_students) == 6:
            day1 = [selected_students[0], today]
            day2 = [selected_students[4], today + timedelta(days=1)]
            day3 = [selected_students[1], today + timedelta(days=2)]
            day4 = [selected_students[2], today + timedelta(days=3)]
            day5 = [selected_students[5], today + timedelta(days=4)]
            day6 = [selected_students[3], today + timedelta(days=5)]
            day7 = [selected_students[0], today + timedelta(days=6)]
            week = [day1, day2, day3, day4, day5, day6, day7]
        if len(selected_students) > 6:
            day1 = [selected_students[0], today]
            day2 = [selected_students[1], today + timedelta(days=1)]
            day3 = [selected_students[2], today + timedelta(days=2)]
            day4 = [selected_students[3], today + timedelta(days=3)]
            day5 = [selected_students[4], today + timedelta(days=4)]
            day6 = [selected_students[5], today + timedelta(days=5)]
            day7 = [selected_students[6], today + timedelta(days=6)]
            week = [day1, day2, day3, day4, day5, day6, day7]
        change_planning(week)
    else:
        pass



DDay = DDay()

# test
etudiants = ["Etudiant 1", "Etudiant 2", "Etudiant 3", "Etudiant 4", "Etudiant 5"]
planning(etudiants)
