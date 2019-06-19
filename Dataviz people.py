#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 15:01:27 2019

@author: moi
"""

#Import des librairies

import requests
from pandas.io.json import json_normalize
import pandas as pd
import qgrid
#Ouverture en Dataframe
URL = "/home/moi/Documents/Projet_movies/people-Alex-Cyprien.csv"
df = pd.read_csv(URL, sep=',')
print(df)

# Création du qgrid
edit_df = qgrid.show_grid(df, show_toolbar=True)
edit_df