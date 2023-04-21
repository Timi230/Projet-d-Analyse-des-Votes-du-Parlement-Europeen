import csv 
import os

def load_csv (path) :

    file = open(path, 'r')
    lines = file.readlines()
    file.close()

    csv = []

    for line in lines :

        line = line[:-1]
        data = line.split(sep=';')
        csv.append(data)

    return csv

def charger_csv(data, path):
    fichier = load_csv(path)

    for i in range(1, len(fichier)):
        fichier[i][4] = data[i-1]

    with open(path, mode='w', newline='') as  fichier_csv:

        # Création d'un objet écrivain CSV
        ecrivain_csv = csv.writer(fichier_csv)

        # Écriture de la liste dans le fichier CSV
        for ligne in fichier:
            ecrivain_csv.writerow(ligne)

def new_csv(data, numeroVote):

    # Nom du fichier CSV à créer
    nom_fichier = "vote_" + str(numeroVote) + ".csv"

    

    # Ouvrir le fichier CSV en mode écriture
    fichier_csv = open(nom_fichier, mode='w', newline='')

    # Créer un objet writer CSV
    writer = csv.writer(fichier_csv)

    # Écrire les données dans le fichier CSV
    for ligne in data:
        writer.writerow(ligne)

    # Fermer le fichier CSV
    fichier_csv.close()
    