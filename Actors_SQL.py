# importing pandas package 
import pandas as pd 
from sqlalchemy import create_engine
# importing PostgreSQL library

# Définition des accès
user='team'
password='DataLab@2019'
#machine='172.20.152.200'
machine='127.0.0.1'
#base_donnees='BDD_Alexandre'
base_donnees='Datalab'
#mySQLengine = create_engine("mysql://%s:%s@%s/%s?charset=utf8" % (user, password, machine, base_donnees))
pgSQLengine = create_engine("postgresql://%s:%s@%s/%s" % (user, password, machine, base_donnees))

# Ici, on execute directement du SQL: "USE XXX"
#mySQLengine.execute("USE `BDD_Alexandre`;")



# making data frame from csv file
URL = "/home/moi/Documents/Projet_movies/movies/data/actors.csv"
acteurs = pd.read_csv(URL, sep=';', header=None)
#tbl = pd.read_csv(data, encoding = 'utf8', sep=';', header=None)
print(acteurs.head)


# Ecriture des données dataframe -> mySQL
# Après avoir supprimé (si existante) la table 'people'
Tname="Actors2"
#mySQLengine.execute('DROP TABLE IF EXISTS %s' % Tname)
acteurs.to_sql(Tname, pgSQLengine, if_exists='replace', index=False)
result=pgSQLengine.execute("SELECT * FROM \"ListeApprenants\";")
for x in result:
    print(x)

#print("CSV sauvé dans table '%s'" % Tname)

mySQLengine.close()
