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
meta <- meta_SNP %>%
  mutate(eff_se = sqrt(EFF_var))

result <- robu(eff_se ~ 1, meta, studynum = SNP_id, var.eff.size = EFF_var, rho = 0.8, small = TRUE)
result

png(file='./examples/static/plots/forestplot.png')
forest.robu(result, es.lab = "SNP_id", study.lab = "entryId",
            "Effect Size" = eff_se)
dev.off()
#}