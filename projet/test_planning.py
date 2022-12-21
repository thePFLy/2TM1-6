import unittest
import planning
import csv
from user import Users
from datetime import datetime, timedelta
from class_plan import Planning


class TestPlanning(unittest.TestCase):

    def setUp(self):
        self.students = [
            Planning('John', datetime.strftime(datetime.today(), "%d-%m-%Y")),
            Planning('Jane', datetime.strftime(datetime.today() + timedelta(days=1), "%d-%m-%Y")),
            Planning('Bob', datetime.strftime(datetime.today() + timedelta(days=2), "%d-%m-%Y")),
            Planning('Alice', datetime.strftime(datetime.today() + timedelta(days=3), "%d-%m-%Y")),
            Planning('Eve', datetime.strftime(datetime.today() + timedelta(days=4), "%d-%m-%Y")),
            Planning('Adam', datetime.strftime(datetime.today() + timedelta(days=5), "%d-%m-%Y")),
            Planning('Alice', datetime.strftime(datetime.today() + timedelta(days=6), "%d-%m-%Y"))
        ]
        self.userss = [
            Users('John', '0111'),
            Users('Jane', '0111'),
            Users('Bob', '0111'),
            Users('Alice', '0111'),
            Users('Eve', '0111'),
            Users('Adam', '0111'),
            Users('Alice', '0111')
        ]
        self.day = datetime.strptime("01-01-2022", "%d-%m-%Y")

    def test_DDay(self):
        # On test la fonction DDay
        result = planning.DDay()
        if result == None:
            self.assertEqual(result, None)
        else:
            result = datetime.strftime(planning.DDay(), "%d-%m-%Y")
            today = datetime.today()
            expected = datetime.strftime(today, "%d-%m-%Y")
            self.assertEqual(result, expected)

    def test_newDDay(self):
        # On test la fonction newDDay
        planning.newDDay()
        with open('database/DDay.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                result = row["Date"]
        expected = datetime.strftime(datetime.today(), "%d-%m-%Y")
        self.assertEqual(result, expected)

    def test_init_planning(self):
        # On test la fonction init_planning
        plan = planning.init_planning('database/planning.csv')
        result = []
        expected = []
        for i in range(len(result)):
            result.append([result[i].date,result[i].username])
            result.append([self.students[i].date,self.students[i].username])
        self.assertEqual(result, expected)

    def test_change_planning(self):
        # On test la fonction change_planning
        week = []
        today = datetime.today()
        jour = -1
        for i in self.students:
            jour = jour + 1
            today = datetime.today() + timedelta(days=jour)
            name = i.username
            underweek = [name, today]
            week.append(underweek)
        planning.change_planning(week)
        with open('database/planning.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = [row for row in reader]
        result = [[row['Day'], row['Name']] for row in rows[0:]]
        expected = [[day.date, day.username] for day in self.students]
        self.assertEqual(result, expected)

    def test_get_planning(self):
        # On test la fonction get_planning
        week = []
        today = datetime.today()
        jour = -1
        for i in self.students:
            jour = jour + 1
            today = datetime.today() + timedelta(days=jour)
            name = i.username
            underweek = [name, today]
            week.append(underweek)
        result = planning.get_planning(self.userss, week, today)
        expected = self.students
        if result == None:
             self.assertEqual(result, None)
        else:
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
