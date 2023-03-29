import csv 

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