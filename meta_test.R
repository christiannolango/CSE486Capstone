#! C:\\Users\\camri\\OneDrive\\Desktop\\capstone\\CSE486Capstone\Rscript
suppressMessages({library(dplyr)
  library(meta)
  library(readxl)
  library(robumeta)
  library(grid)
  library(irr)})
library('RPostgreSQL')
library(forestplot)

con <- DBI::dbConnect(odbc::odbc(),
                      Driver   = "PostgreSQL Unicode(x64)",
                      Server   = "localhost",
                      Database = "capstone_database",
                      UID      = "research_database",
                      PWD      = "capstone!",
                      Port     = 5432)

meta <- dbGetQuery(con, "SELECT * from examples_snp_entry;")
meta$SNP_id <- as.character(meta$SNP_id)
meta$SNP_id <- as.factor(meta$SNP_id)
meta <- meta %>%
  mutate(eff_se = sqrt(EFF_var))

#d_to_g <- function(eff_d, n1, n2){
#  eff_d * (1 - (3 / (4 * (n1 + n2) - 9)))
#}
#meta <- meta %>%
#  mutate(eff_g = d_to_g(eff_size, cleft_n, compare_n))

con_m <- robu(eff_se ~ 1, meta, studynum = SNP_id, var.eff.size = EFF_var, rho = 0.8, small = TRUE)
con_m


#"C:\Users\camri\OneDrive\Desktop\capstone\CSE486Capstone\django\django_project\examples\static\plots\plot3.png", 
    
png(file= 'C:\\Users\\camri\\OneDrive\\Desktop\\capstone\\CSE486Capstone\\django\\django_project\\examples\\static\\plots\\plot4.png')
forest.robu(con_m, es.lab = "SNP_id", study.lab = "entry_id",
            "Effect Size" = eff_se)
dev.off()

dbDisconnect(con)


