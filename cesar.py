#!/usr/bin/env python3

# Chemin de fichier absolu si besoin
# U:\\Documents\\NSI\\Projet cesar\\
path = input("Chemin absolu (appuyez sur entrée pour automatique): ")
# Import de cesar_gui
import importlib.util
spec = importlib.util.spec_from_file_location("cesar_gui", path + "cesar_gui.py")
cesar_gui = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(cesar_gui)
except FileNotFoundError:
    print("--- ERREUR : Impossible de charger le module cesar_gui")
    raise SystemExit
# Tableau contenant les mots français
dico = []
def cesar(string, shift=1):
  # Chaîne de caractère finale
  final_str = ""
  for char in string:
    # Nouvel index
    new_index = ord(char) + shift
    # Si le nouvel index dépasse la plage des minuscules
    if (97 <= ord(char) <= 122):
        if (new_index < 97):
            new_index += 26
        if (new_index > 122):
            new_index -= 26
    # Si le nouvel index dépasse la plage des majuscules
    elif (65 <= ord(char) <= 90):
        if (new_index < 65):
            new_index += 26
        if (new_index > 90):
            new_index -= 26
    else:
        new_index = ord(char)
    # Récupération de la lettre décalée
    modified = chr(new_index)
    final_str += modified
  return final_str
  
def decrypt_cesar(string, shift):
    # Fonction césar inverse
    return cesar(string, -shift)
    
def open_dico_file():
  # Ouverture du fichier dictionnaire et enregistrement de chaque ligne (= mot) dans un tableau
  fp = open(path+"dico.txt", 'r')
  line = fp.readline()
  while line:
    dico.append(line)
    line = fp.readline()

def read_file(filename):
    # Lecture d'un fichier et enregistre dans un chaîne de caractère
    file = open(path+filename, 'r')
    string = file.read()
    return string

def save_to_file(name, data):
    # Ecris des données dans un fichier
    file = open(path+name, 'w')
    file.write(data)
    
def sort_dict(dict):
    # Trier le dictionnaire en mettant la valeur la plus haute en premier
    sorted_dict = sorted(dict.items(), key=lambda kv: kv[1])
    return sorted_dict[::-1]

def brute_force(encoded, s_range):
    # Charge le fichier
    open_dico_file()
    found = []
    biggest_shift = {}
    # Découpe la chaîne cryptée en mots séparés
    words = encoded.split()
    # Tri des mots par longueur
    words = sorted(words, key=len)[::-1]
    # Boucle de test de 0 à s_range : test des différents décalages
    for shift in range(-s_range, s_range):
        biggest_shift[str(shift)] = 0
        # Pour chaque mot de la chaine cryptée
        for word in words:
            # Décalage par la fonction césar
            moved = cesar(word, shift)
            # Pour chaque mot dans le dictionnaire
            for dicoWord in dico:
                # Si le mot existe, l'enregistrer dans un tableau
                # avec le décalage correspondant
                moved = moved.rstrip('\n').lower()
                dicoWordForm = dicoWord.rstrip('\n').lower()
                if (dicoWordForm == moved):
                    found.append([moved, -shift])
    # Afficher les mots trouvés avec leur décalage d'origine
    for i in range(len(found)):
        print("Le mot \"{}\" a été trouvé avec un décalage de {}".format(found[i][0], str(found[i][1])))
        biggest_shift[str(found[i][1])] += 1
    biggest_shift = sort_dict(biggest_shift)
    print("Le décalage le plus trouvé est {}".format(str(biggest_shift[0][0])))
    print("Phrase décryptée avec ce décalage: {}".format(cesar(encoded, -int(biggest_shift[0][0]))))
    
        
def separator():
     # Affiche le séparateur
    print("-------------------")
def back_menu():
    # Attend pour revenir au menu
    input("Appuyez sur Entrée pour continuer...")
def cli():
    choice = 0
    print("Bienvenu dans l'interface en ligne de commande")
    separator()
    # Tant que l'utilisateur n'entre pas quitter
    while choice < 8:
        print("Actions disponibles :")
        print("[1] Crypter un phrase avec césar")
        print("[2] Décrypter une phrase avec césar")
        print("[3] Crypter un fichier")
        print("[4] Décrypter un fichier")
        print("[5] Bruteforcer une phrase cryptée avec césar")
        print("[6] Bruteforcer une fichier (peut être long)")
        print("[7] Lancer l'interface graphique (beta et incomplète)")
        print("[8+] Quitter le programme")
        choice = int(input("Votre choix: "))
        separator()
        # Les différents choix
        if (choice == 1):
            # Crypter une phrase : récupération des infos
            string = input("Phrase à crypter: ")
            shift = int(input("Décalage: "))
            result = cesar(string, shift)
            print("La phrase cryptée est \"{}\"".format(result))
            separator()
            back_menu()
        elif (choice == 2):
            # Décrypter une phrase : récupération des infos
            string = input("Phrase à décrypter: ")
            shift = int(input("Décalage: "))
            result = decrypt_cesar(string, shift)
            print("La phrase décryptée est \"{}\"".format(result))
            separator()
            back_menu()
        elif (choice == 5):
            # Bruteforcer une phrase : récupération des infos
            string = input("Phrase cryptée à bruteforcer: ")
            s_range = int(input("Plage de recherche: "))
            brute_force(string, s_range)
            separator()
            back_menu()
        elif (choice == 3):
            # Crypter un fichier : récupération des infos
            filename = input("Nom du fichier: ")
            shift = int(input("Décalage: "))
            string = read_file(filename)
            result = cesar(string, shift)
            filename = input("Nom du fichier de sortie: ")
            save_to_file(filename, result)
            separator()
            back_menu()
        elif (choice == 4):
            # Décrypter un fichier : récupération des infos
            filename = input("Nom du fichier: ")
            shift = int(input("Décalage: "))
            string = read_file(filename)
            result = decrypt_cesar(string, shift)
            filename = input("Nom du fichier de sortie: ")
            save_to_file(filename, result)
            separator()
            back_menu()
        elif (choice == 6):
            # Bruteforcer un fichier : récupération des infos
            filename = input("Nom du fichier: ")
            string = read_file(filename)
            s_range = int(input("Plage de recherche: "))
            brute_force(string, s_range)
            separator()
            back_menu()
        elif (choice == 7):
            cesar_gui.start()
        separator()
# Programme principal
cli()