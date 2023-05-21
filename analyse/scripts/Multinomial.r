library(readr)
library(dplyr)
library(tidyverse)
library(caret)
library(nnet)

library(nnet)

# Charger les données
donnees <- read_csv("analyse/data/vote_3.csv")
test <- read_csv("analyse/data/vote_4.csv")

# Création du modele mutlinomial
modele <- multinom(factor(Vote) ~ ., data = donnees)
summary(modele)

# test du rapport de vraissemblance 

modele_null <- multinom(factor(Vote) ~ 1, data = donnees)

dev <- modele_null$deviance - modele$deviance
deg <- modele$edf - modele_null$edf

print(paste('Stat de test =', dev))
print(paste('Deg de liberté = ', deg))
print(paste('p-value = ', pchisq(dev, deg, lower.tail = FALSE)))



# Prediciton 
prediction <- predict(modele, test)
test$Prediction <- prediction
xtab <- table(test$Prediction, test$Vote)

table(prediction)

# Matrice de confusion 

confusionMatrix(xtab)
