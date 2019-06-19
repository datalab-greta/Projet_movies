#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:07:31 2019

@author: moi
"""

# importing pandas package 
import pandas as pd 
from sqlalchemy import create_engine

# Définition des accès
user='team'
password='DataLab@2019'
machine='172.20.152.200'
mySQLengine = create_engine("mysql://%s:%s@%s/?charset=utf8" % (user, password, machine))

# Ici, on execute directement du SQL: "USE XXX"
mySQLengine.execute("USE `BDD_Alexandre`;")



# making data frame from csv file
URL = "/home/moi/Documents/Git and the movies/movies/data/casts.csv"
casts = pd.read_csv(URL, sep=';', header=None)
#tbl = pd.read_csv(data, encoding = 'utf8', sep=';', header=None)
print(casts.head)


# Ecriture des données dataframe -> mySQL
# Après avoir supprimé (si existante) la table 'people'
Tname="Casts"
mySQLengine.execute('DROP TABLE IF EXISTS %s' % Tname)
casts.to_sql(Tname, mySQLengine, if_exists='replace', index=False)
print("CSV sauvé dans table '%s'" % Tname)
