library(readr)
library(dplyr)
library(tidyverse)
library(caret)
library(ggplot2)

vote1 <- read_csv("analyse/data_seul_VS_autre/vote_3.csv")
test <- read_csv("analyse/data_seul_VS_autre/vote_4.csv")



vote1 <- vote1[!is.na(vote1$Party),]
test <- test[!is.na(test$Party),]

# smp_size <- floor(0.75 * nrow(vote1))
# train_ind <- sample(seq_len(nrow(vote1)), size = smp_size)

# train <- vote1[train_ind, ]
# test <- vote1[-train_ind, ]




set.seed(222)

fitControl <- trainControl(method = "cv", number = 10, savePredictions = TRUE)

lr_model <- train(factor(Vote) ~ ., data = vote1, method = "glm", family =  binomial(), trControl = fitControl)
summary(lr_model)



# Modèle null test du rapport de vraisemblance

Lm <- logLik(lr_model$finalModel)

null_model <- glm(factor(Vote) ~ 1, data = vote1, family = binomial())
L0 <- logLik(null_model)

#calculer le R² de McFadden
R2_McFadden <- 1 - (Lm / L0)
print(R2_McFadden)



 
# Prédiciton
prediction_lr <- predict(lr_model, test)

test$Prediction <- prediction_lr

# matrice de confusion

xtab <- table(test$Prediction, test$Vote)
head(xtab)

conf_mat <- confusionMatrix(xtab)

scores <- conf_mat$byClass["Pos Pred Value"]

# Obtenir les vrais positifs et faux positifs pour différentes valeurs seuils
tvp <- numeric()
fpv <- numeric()
for (threshold in seq(0, 1, by = 0.01)) {
  TP <- conf_mat$table[2,2]
  FP <- conf_mat$table[1,2]
  TN <- conf_mat$table[1,1]
  FN <- conf_mat$table[2,1]
  TP <- TP * scores >= threshold
  FP <- FP * (1 - scores) >= threshold
  TN <- TN * scores >= threshold
  FN <- FN * (1 - scores) >= threshold
  tvp <- c(tvp, sum(TN) / (sum(TP) + sum(FN)))
  fpv <- c(fpv, sum(FN) / (sum(FP) + sum(TN)))
}

# Créer une courbe ROC
df <- data.frame(FPV = fpv, TVP = tvp)
ggplot(df, aes(x = FPV, y = TVP)) +
  geom_line() +
  geom_abline(intercept = 0, slope = 1, linetype = "dashed") +
  ggtitle("Courbe ROC") +
  xlab("Taux de faux positifs") +
  ylab("Taux de vrais positifs")
