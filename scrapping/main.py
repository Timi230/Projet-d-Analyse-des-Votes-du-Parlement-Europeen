from bs4 import BeautifulSoup 
import requests
from lib import *



fichier = load_csv("./data/EP9_RCVs_2022_06_22.csv")

id_deputes = []

for i in range(1, len(fichier)):
    id_deputes.append(fichier[i][0])


url= "https://www.europarl.europa.eu/meps/fr/"


age = []
for i in range(0,len(id_deputes)):

    html_reponse = requests.get(url+id_deputes[i])
    html = html_reponse.content
    soup = BeautifulSoup(html, 'html.parser')
    
    try : 
        div_age = soup.find('time', {'class': 'sln-birth-date'})
        date = div_age["datetime"]
        age.append(date)
    
    except TypeError :
        age.append(' ')
    
    print(i+1,"/811")

print("\n Fin du scrapping et début de l'écriture")

charger_csv(age, './data/depute_date.csv')

print("\n Fin du programme")

#print(age)

