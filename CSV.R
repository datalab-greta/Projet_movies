library(RMySQL)

BDD<- dbConnect(MySQL(), user="team", host="172.20.152.200", password="DataLab@2019", dbname="BDD_Alexandre")
DF<-read.csv2("home/moi/Documents/movies/data/casts.csv", header = FALSE)
View(DF)
RMySQL::dbWriteTable(BDD, "Casts",DF)