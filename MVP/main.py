import getpass
import csv

'''
but: 
- s'inscrire/désinscrire à un repas matin-midi-soir 
- avec nom + prenom + choix de quel repas
- fichier csv avec les différents repas du jour et qui y participe
'''

breakfast_participant = []
lunch_participant = []
dinner_participant = []


def update_table(repas_list, file):
    with open(file, mode="r") as csvfile:
        spamreader = csv.reader(csvfile)
        for lines in spamreader:
            repas_list.append(lines)


def write_csv(repas_list, file):
	file = open(file, 'w', newline='')
	with file:
		write = csv.writer(file)
		write.writerows(repas_list)


def registration(lastname, firstname, repas):
	if repas == "all":
		try:
			breakfast_participant.append((lastname + " " + firstname).split())
			lunch_participant.append((lastname + " " + firstname).split())
			dinner_participant.append((lastname + " " + firstname).split())
		except ValueError:
			pass
	else:
		if (lastname + " " + firstname).split() in repas:
			print("already registered")
		else:
			repas.append((lastname + " " + firstname).split())
			print("you are now registered")
			print("there are now " + str(len(repas)) +" people who have registered for this meal")
	write_csv(breakfast_participant, "files/breakfast_participant.csv")
	write_csv(lunch_participant, "files/lunch_participant.csv")
	write_csv(dinner_participant, "files/dinner_participant.csv")


def unsubscribe(lastname, firstname, repas):
	if repas == "all":
		try:
			breakfast_participant.remove((lastname + " " + firstname).split())
			lunch_participant.remove((lastname + " " + firstname).split())
			dinner_participant.remove((lastname + " " + firstname).split())
		except ValueError:
			pass
	else:
		try:
			repas.remove((lastname + " " + firstname).split()) 
			print("you are unsubscribed")
		except ValueError:
			print("it looks like you were not registered")
			pass	
	write_csv(breakfast_participant, "files/breakfast_participant.csv")
	write_csv(lunch_participant, "files/lunch_participant.csv")
	write_csv(dinner_participant, "files/dinner_participant.csv")


def introduction():
	print("-----Welcome on the dining manager-----")
	lastname = input("Type your last name: ")
	firstname = input("type your first name: ")
	intro = int(input("Type:\n  1 to register for a daily meal.\n  2 to unsubscribe to a meal of the day.\n  3 to exit the program\n"))
	while intro != 1 and intro != 2 and intro != 3:
		intro = int(input("Type:\n  1 to register for a daily meal.\n  2 to unsubscribe to a meal of the day.\n  3 to exit the program\n"))

	if intro == 1:
		print("------registration-----")
		choice_registration = int(input("Type to register for:\n  1 breakfast.\n  2 lunch\n  3 dinner.\n  4 all meals of the day\n"))
		if choice_registration == 1:
			registration(lastname, firstname, breakfast_participant)
		elif choice_registration == 2:
			registration(lastname, firstname, lunch_participant)
		elif choice_registration == 3:
			registration(lastname, firstname, dinner_participant)
		elif choice_registration == 4:
			registration(lastname, firstname, "all")

	elif intro == 2:
		print("------unsubscribe-----")
		choice_unsubscribe = int(input("Type to unsubscribe for:\n  1 breakfast.\n  2 lunch\n  3 dinner.\n  4 all meals of the day\n"))
		if choice_unsubscribe == 1:
			unsubscribe(lastname, firstname, breakfast_participant)
		elif choice_unsubscribe == 2:
			unsubscribe(lastname, firstname, lunch_participant)
		elif choice_unsubscribe == 3:
			unsubscribe(lastname, firstname, dinner_participant)
		elif choice_unsubscribe == 4:
			unsubscribe(lastname, firstname, "all")

	elif intro == 3:
		exit()
	else:
		print("erreur inconnue")



def main():
	update_table(breakfast_participant, "files/breakfast_participant.csv")
	update_table(lunch_participant, "files/lunch_participant.csv")
	update_table(dinner_participant, "files/dinner_participant.csv")
	introduction()


if __name__ == '__main__':
	parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
	description='''
	MVP Help description
	----------------------
	1. Enter your name and first name
	2. Make a choice between 1,2,3 (1 subscribre, 2 unsubscribe, 3 exit)
	3. If you take 1 or 2, choose between the meal time (1 breakfast,2 lunch,3 dinner,4 all)
	3a. You cannot unsucribe a meal time when you are not subscribe
	''')
	parser.print_help()
	main()
