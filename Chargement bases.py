#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:40:02 2019

@author: moi
"""

# importing pandas package 
import pandas as pd 
from sqlalchemy import create_engine

# Définition des accès
user='team'
password='DataLab@2019'
machine='172.20.152.200'
base_donnees='Base_films_Alex_Cyprien'
mySQLengine = create_engine("mysql://%s:%s@%s/%s?charset=utf8" % (user, password, machine, base_donnees))



# making data frame from csv file Casts
URLCasts = "/home/moi/Documents/Projet_movies/movies/data/casts.csv"
casts = pd.read_csv(URLCasts, sep=';', header=None)
URLActors = "/home/moi/Documents/Projet_movies/movies/data/actors.csv"
actors = pd.read_csv(URLActors, sep=';', header=None)
URLPeople = "/home/moi/Documents/Projet_movies/movies/data/people.csv"
people = pd.read_csv(URLPeople, sep=';', header=None)
URLRemakes = "/home/moi/Documents/Projet_movies/movies/data/remakes.csv"
remakes = pd.read_csv(URLRemakes, sep=';', header=None)
URLStudios = "/home/moi/Documents/Projet_movies/movies/data/studios.csv"
studios = pd.read_csv(URLActors, sep=';', header=None)

#tbl = pd.read_csv(data, encoding = 'utf8', sep=';', header=None)
#print(casts.head)


# Ecriture des données dataframe -> mySQL
# Après avoir supprimé (si existante) la table 'people'
Tname="Casts"
mySQLengine.execute('DROP TABLE IF EXISTS %s' % Tname)
casts.to_sql(Tname, mySQLengine, if_exists='replace', index=False)
print("CSV sauvé dans table '%s'" % Tname)
