from lib import *
import csv

def traitementVote(csv, fichier_vote , numeroVote):

    date_vote = fichier_vote[numeroVote][3]
    annee_vote = int(date_vote[-4:])  
    
    vote = []
    age = []
    pays = []
    parti = []
    bords = []
    parti_E = []

    for i in range(1,len(csv)):
        if csv[i][numeroVote+10] == "1" or csv[i][numeroVote+10] == "2" or csv[i][numeroVote+10] == "3" :

            vote.append(csv[i][numeroVote+10])
            
            age_depute = int(csv[i][4][:4])
            age.append(str(annee_vote-age_depute))
            
            pays.append(csv[i][5])

            # if (csv[i][6]=="") or (csv[i][6]==" ") :
            #     parti.append("None")
            # else :
            #     parti.append(csv[i][6])

            bords.append(csv[i][7])

            if (csv[i][8]=="") or (csv[i][8]==" ") :
                parti_E.append("None")
            else :
                parti_E.append(csv[i][8])
    
    return age, pays, bords, parti_E, vote

def format_csv(age, pays, parti, parti_E, vote, numeroVote):

    csv_vote = [["Age","Country","Party","EPG","Vote"]]

    new_line = []

    for i in range(len(age)):
       new_line = [age[i],pays[i],parti[i],parti_E[i], vote[i]]
       csv_vote.append(new_line)

    new_csv(csv_vote, numeroVote)        

def chargement_fichier_vote(csv, fichier_vote, numeroVote):
   
   age, pays, parti, parti_E, vote = traitementVote(csv,fichier_vote, numeroVote)

   format_csv(age, pays, parti, parti_E, vote,numeroVote)

if __name__ == "__main__":

    fichier = load_csv("scrapping/data/EP9_RCVs_2022_06_22.csv")
    fichier_vote = load_csv("scrapping/data/EP9_Voted.csv")

    repo_dir = "analyse/data"
    os.chdir(repo_dir)
    
    
    for i in range(1,len(fichier_vote)-1):
    
        chargement_fichier_vote(fichier,fichier_vote,i)
        
        print(str(i)+'/'+str(len(fichier_vote)-1))

    
    