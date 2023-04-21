donnees <- read.csv("analyse/data/vote_1.csv", header = TRUE)
head(donnees)


# Chargement du package nnet
library(nnet)

# Modèle de régression logistique multinomiale
modele <- multinom(Vote ~ Age + Country + Party + EPG, data = donnees)

summary(modele)

# Nouvelles données à prédire
#nouvelles_donnees <- data.frame(Age = 25, Country = "France", Party = "PS", EPG = "oui")

# Prévision des résultats
#predict(modele, nouvelles_donnees, type = "class")
