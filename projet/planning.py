import random
import csv
from datetime import datetime, date, timedelta


def jourJ():
    with open('jourJ.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            return row["Date"]


def newJourJ():
    newdate = datetime.today()
    formatted_date = newdate.strftime('%d-%m-%Y')
    with open('jourJ.csv', 'w') as csvfile:
        fieldnames = ['Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'Date': "Date"})
        writer.writerow({'Date': formatted_date})


def changement_planning(lundi,mardi,mercredi,jeudi,vendredi,samedi,dimanche):
    with open('planning.csv', 'w') as csvfile:
        fieldnames = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(
            {'lundi': 'lundi', 'mardi': 'mardi', 'mercredi': 'mercredi', 'jeudi': 'jeudi', 'vendredi': 'vendredi',
             'samedi': 'samedi', 'dimanche': 'dimanche'})
        writer.writerow({'lundi': lundi, 'mardi': mardi, 'mercredi': mercredi, 'jeudi': jeudi, 'vendredi': vendredi,
                         'samedi': samedi, 'dimanche': dimanche})


def planning():
    today = datetime.today()
    ecart = today - jourJ
    if ecart.days >= 7:
        newJourJ()
        print("Un changement dans le planning a eu lieu")
        if len(etudiants) >= 7:
            # Choisir 7 étudiants au hasard
            etudiants_choisis = random.sample(etudiants, 7)
            # Mélanger les étudiants choisis
            random.shuffle(etudiants_choisis)
        else:
            etudiants_choisis = etudiants

        # Répartir les étudiants sur les différents jours de la semaine
        if len(etudiants_choisis) == 1:
            lundi = etudiants_choisis[0]
            mardi = etudiants_choisis[0]
            mercredi = etudiants_choisis[0]
            jeudi = etudiants_choisis[0]
            vendredi = etudiants_choisis[0]
            samedi = etudiants_choisis[0]
            dimanche = etudiants_choisis[0]
        if len(etudiants_choisis) == 2:
            lundi = etudiants_choisis[0]
            mardi = etudiants_choisis[1]
            mercredi = etudiants_choisis[0]
            jeudi = etudiants_choisis[1]
            vendredi = etudiants_choisis[0]
            samedi = etudiants_choisis[1]
            dimanche = etudiants_choisis[0]
        if len(etudiants_choisis) == 3:
            lundi = etudiants_choisis[0]
            mardi = etudiants_choisis[1]
            mercredi = etudiants_choisis[2]
            jeudi = etudiants_choisis[0]
            vendredi = etudiants_choisis[1]
            samedi = etudiants_choisis[2]
            dimanche = etudiants_choisis[0]
        if len(etudiants_choisis) == 4:
            lundi = etudiants_choisis[0]
            mardi = etudiants_choisis[1]
            mercredi = etudiants_choisis[2]
            jeudi = etudiants_choisis[3]
            vendredi = etudiants_choisis[0]
            samedi = etudiants_choisis[1]
            dimanche = etudiants_choisis[2]
        if len(etudiants_choisis) == 5:
            lundi = etudiants_choisis[0]
            mardi = etudiants_choisis[1]
            mercredi = etudiants_choisis[2]
            jeudi = etudiants_choisis[3]
            vendredi = etudiants_choisis[4]
            samedi = etudiants_choisis[0]
            dimanche = etudiants_choisis[1]
        if len(etudiants_choisis) == 6:
            lundi = etudiants_choisis[1]
            mardi = etudiants_choisis[0]
            mercredi = etudiants_choisis[3]
            jeudi = etudiants_choisis[2]
            vendredi = etudiants_choisis[5]
            samedi = etudiants_choisis[4]
            dimanche = etudiants_choisis[0]
        if len(etudiants_choisis) > 6:
            lundi = etudiants_choisis[0]
            mardi = etudiants_choisis[1]
            mercredi = etudiants_choisis[2]
            jeudi = etudiants_choisis[3]
            vendredi = etudiants_choisis[4]
            samedi = etudiants_choisis[5]
            dimanche = etudiants_choisis[6]
        changement_planning(lundi,mardi,mercredi,jeudi,vendredi,samedi,dimanche)
    else:
        print("cbon")
        pass


etudiants = ["Etudiant 1", "Etudiant 2", "Etudiant 3", "Etudiant 4", "Etudiant 5"]
jourJ = datetime.strptime(jourJ(), "%d-%m-%Y")

planning()
