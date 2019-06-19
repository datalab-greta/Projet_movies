#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:39:24 2019

@author: moi
"""

#Création d'une dataviz acteurs


#Import des librairies

import requests
from pandas.io.json import json_normalize
import pandas as pd
import qgrid
#Ouverture en Dataframe
URL = "/home/moi/Documents/Projet_movies/File-actors-Alex-Cyprien.csv"
acteurs = pd.read_csv(URL, sep=',')
print(acteurs)

# Création du qgrid
edit_acteurs = qgrid.show_grid(acteurs, show_toolbar=True)
edit_acteurs
##QgridWidget(grid_options={'fullWidthRows': True, 'syncColumnCellResize': True, 'forceFitColumns': True, 'defau…

acteurs_large = acteurs.pivot(index='Stage-name', columns='date-of-birth', values='Origin')
acteurs_large.head

#il est nécessaire d'installer 'highchart' si ce n'est pas déjà fait
from highcharts import Highchart # import highchart library
H = Highchart() # setup highchart instance
for i in acteurs_large.columns:
    H.add_data_set(list(acteurs_large[i]), 'spline', i)
H

# Ajout d'informations au graphique, considérées comme des options par highcharts
options = {
    'title': {
        'text': 'Indice ATMO dans les principales villes de la région Centre-Val de Loire'
    },
    'xAxis': { 
        'title': {
            'text': 'Date (#affichage à finaliser)'
        }
    },
    'yAxis': { 
        'title': {
            'text': 'Indice ATMO'
        }
    }
}
H.set_dict_options(options)
H

#il est nécessaire d'installer 'plotly' si ce n'est pas déjà fait
# Connexion à l'API avec un compte existant
import plotly
plotly.tools.set_credentials_file(username='RemiJulien', api_key='P7zRkAFgDxfcFdcGwzTP')

# Chargement des librairies
import plotly.plotly as py
import plotly.graph_objs as go

# Création de la 'heatmap'
heatmap = go.Heatmap(z=acteurs_large.as_matrix(), x=acteurs_large.columns, y=acteurs_large.index, colorscale='Jet')
data = [heatmap]
py.iplot(data, filename='ATMO-heatmap')


# Définition des accès
user='team'
password='DataLab@2019'
machine='172.20.152.200'
mySQLengine = create_engine("mysql://%s:%s@%s/?charset=utf8" % (user, password, machine))

# Ici, on execute directement du SQL: "USE XXX"
mySQLengine.execute("USE `BDD_Alexandre`;")
# Ecriture des données dataframe -> mySQL
# Après avoir supprimé (si existante) la table 'people'
Tname="Actors"
mySQLengine.execute('DROP TABLE IF EXISTS %s' % Tname)
acteurs.to_sql(Tname, mySQLengine, if_exists='replace', index=False)
print("CSV sauvé dans table '%s'" % Tname)
