library(readxl)
suppressMessages({library(dplyr)
  library(meta)
  library(readxl)
  library(robumeta)
  library(grid)
  library(irr)})
library('RPostgreSQL')
library(forestplot)


meta_study <- read_excel("./geneData.xlsx", 
                         sheet = "studyData", na = ".")

meta_SNP <- read_excel("./geneData.xlsx", 
                       sheet = "SNP_entryData", na = ".")

meta_SNP$SNP_id <- as.character(meta_SNP$SNP_id)
meta_SNP$SNP_id <- as.factor(meta_SNP$SNP_id)
meta_SNP$SNP_id <- as.character(meta_SNP$study_id)
meta_SNP$SNP_id <- as.factor(meta_SNP$study_id)

meta_SNP$author <- as.character(meta_SNP$author)
meta_SNP$year <- as.character(meta_SNP$year)
author_year = paste(author, year)
#meta <- meta_SNP %>%
#  mutate(eff_se = sqrt(EFF_var))

result <- robu(EFF_score ~ 1, meta_SNP, studynum = study_id, var.eff.size = EFF_var, rho = 0.8, small = TRUE)
result

png(file='./examples/static/plots/forestplot.png')
forest.robu(result, es.lab = "SNP_id", study.lab = "entryId",
            "Effect Size" = EFF_score)
dev.off()
