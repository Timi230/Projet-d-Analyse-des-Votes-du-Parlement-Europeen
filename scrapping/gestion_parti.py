from lib import *


def traitement_parti(fichier, parti):

    bords = []

    for i in range(1,len(fichier)):

        verif = 0
        nom_parti = fichier[i][6]

        for j in range(len(parti)):

            if nom_parti == parti[j][1]: 
                bords.append(parti[j][2])
                verif = 1
                break
            
        if verif == 0:
            print("Bord du parti", fichier[i][6], "non trouver pays :", fichier[i][5])
            saisie = input("Bord du parti : ")
            bords.append(saisie)
            
        print(i,"/",len(fichier))
    
    return bords

def clean_data_parti(bords):
    
    for i in range(0,len(bords)):

        if (bords[i][:12] == "Centre-droit" or bords[i][:12] == "centre-droit" or bords[i][:12] == "centre-Droit" or bords[i][:12] == "Centre-Droit") and (len(bords[i])!=12):
            bords[i] = "Centre-droit"

        elif bords[i][:6] == "Droite" or bords[i][:6] == "droite":
            bords[i] = "Droite"

        elif (bords[i][:13] == "Centre-gauche" or bords[i][:13] == "centre-gauche" or bords[i][:13] == "centre-Gauche" or bords[i][:13] == "Centre-Gauche") :
            bords[i] = "Centre-droit"

        elif bords[i][:6] == "Gauche" or bords[i][:6] == "gauche":
            bords[i] = "Gauche"

        elif (bords[i][:5] != "Centre-" or bords[i][:5] != "centre-") and bords[i][:2] != "NA":
            bords[i] = "Centre"
    
    return bords


if __name__ == '__main__':

    fichier = load_csv("scrapping/data/EP9_RCVs_2022_06_22.csv")
    parti = load_csv("scrapping/data/parti.csv")


    bords = traitement_parti(fichier, parti)
    bords_clean = clean_data_parti(bords)
    print(bords_clean)
    

    charger_csv(bords_clean,"scrapping/data/EP9_RCVs_2022_06_22.csv")