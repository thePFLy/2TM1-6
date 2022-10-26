class Users:
    def __init__(self, fname, surname, password, inthekitchen=False):
        self.fname = fname
        self.surname = surname
        self.password = password
        self.inthekitchen = inthekitchen


"""liste contenant tous les users"""
allUsers = []

"""
Cette fonction se lancera au début du programme
tous se fera par des prompt , mais ça ne sera pas définitif
en attendant de pouvoir le faire directement par un interface 
graphique
"""

def connection():
    print("-Bienvenue sur le gestionnaire de repas-")
    intro = int(input("Si vous souhaitez vous inscrire taper 1, si vous avez déja un compte tapez 2"))
    while intro != 1 and intro != 2:
        intro = int(input("Si vous souhaitez vous inscrire taper 1, si vous avez déja un compte tapez 2"))
    if intro == 1:
        print("----inscription----")
        nom = input("Veuillez entrez votre nom : ")
        prenom = input("Veuillez entrez votre prénom : ")
        print("Vous devez maintenant entrer un mot de passe")
        password = input("")
        print("Confirmez le mot de passe")
        verif = input("")
        while verif != password:
            verif = input("Erreur, veuillez reentrez le mot de passe : ")
        allUsers.append(Users(nom, prenom, password))
        return allUsers[len(allUsers)-1]
    else:
        if intro == 2:
            while True:
                print("----connection----")
                nom = input("Veuillez entrez votre nom : ")
                password = input("Veuillez entrez votre mot de passe : ")
                for user in allUsers:
                    if nom == user.name:
                        if password == user.password:
                            return user
                        else:
                            print("Erreur l'identifiant/motdepasse ne correspond pas")
                print("Erreur votre nom ne se trouve pas dans la base de données")

def main():
    user = connection()

    if user.inthekitchen == False:
        print("Bienvenue "+user.fname+" !")
    else:
        print("Bienvenue chef "+user.fname+" !")


main()