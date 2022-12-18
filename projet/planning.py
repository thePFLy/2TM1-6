import random
import csv
from datetime import datetime, date, timedelta
import logging


def DDay():
    try:
        with open('database/DDay.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                return row["Date"]
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



def change_planning(day1,day2,day3,day4,day5,day6,day7):
    try:
        with open('database/planning.csv', 'w') as csvfile:
            fieldnames = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(
                {'Day 1': 'Day 1', 'Day 2': 'Day 2', 'Day 3': 'Day 3', 'Day 4': 'Day 4', 'Day 5': 'Day 5',
                 'Day 6': 'Day 6', 'Day 7': 'Day 7'})
            writer.writerow({'Day 1': day1, 'Day 2': day2, 'Day 3': day3, 'Day 4': day4, 'Day 5': day5,
                             'Day 6': day6, 'Day 7': day7})
    except OSError as e:
        print(type(e), e)




def planning(students):
    today = datetime.today()
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
            day1 = selected_students[0]
            day2 = selected_students[0]
            day3 = selected_students[0]
            day4 = selected_students[0]
            day5 = selected_students[0]
            day6 = selected_students[0]
            day7 = selected_students[0]
        if len(selected_students) == 2:
            day1 = selected_students[0]
            day2 = selected_students[1]
            day3 = selected_students[0]
            day4 = selected_students[1]
            day5 = selected_students[0]
            day6 = selected_students[1]
            day7 = selected_students[0]
        if len(selected_students) == 3:
            day1 = selected_students[0]
            day2 = selected_students[1]
            day3 = selected_students[2]
            day4 = selected_students[0]
            day5 = selected_students[1]
            day6 = selected_students[2]
            day7 = selected_students[0]
        if len(selected_students) == 4:
            day1 = selected_students[0]
            day2 = selected_students[1]
            day3 = selected_students[2]
            day4 = selected_students[3]
            day5 = selected_students[0]
            day6 = selected_students[1]
            day7 = selected_students[2]
        if len(selected_students) == 5:
            day1 = selected_students[0]
            day2 = selected_students[1]
            day3 = selected_students[2]
            day4 = selected_students[3]
            day5 = selected_students[4]
            day6 = selected_students[0]
            day7 = selected_students[1]
        if len(selected_students) == 6:
            day1 = selected_students[1]
            day2 = selected_students[0]
            day3 = selected_students[3]
            day4 = selected_students[2]
            day5 = selected_students[5]
            day6 = selected_students[4]
            day7 = selected_students[0]
        if len(selected_students) > 6:
            day1 = selected_students[0]
            day2 = selected_students[1]
            day3 = selected_students[2]
            day4 = selected_students[3]
            day5 = selected_students[4]
            day6 = selected_students[5]
            day7 = selected_students[6]
        change_planning(day1,day2,day3,day4,day5,day6,day7)
    else:
        pass


DDay = datetime.strptime(DDay(), "%d-%m-%Y")

# test
etudiants = ["Etudiant 1", "Etudiant 2", "Etudiant 3", "Etudiant 4", "Etudiant 5"]
planning(etudiants)
