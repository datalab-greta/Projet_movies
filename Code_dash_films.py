#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 15:27:48 2019

@author: moi
"""

import dash
import dash_table
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import requests
from pandas.io.json import json_normalize
import pandas as pd
from datetime import datetime as dt


df = pd.read_csv('/home/moi/Documents/Projet_movies/File-actors-Alex.csv')

app = dash.Dash(__name__)

# CREATION DE LA DISPOSITION DE L'APPLICATION
app.layout = html.Div([
    
    # Titre de l'application
    html.H1(
        children="Films",
        style={'textAlign': 'center'}
    ),
     
    # Un slider permettant de selectionner la date voulue
    html.Br(),
    html.Hr(),
    html.Label('Dates des films', style={'fontSize': 25, 'marginTop': 35}),
    dcc.RangeSlider(
        id='Périodes',
        min=1950,
        max=2000,
        step=5,
        marks={i: format(i) for i in range(1950, 2001)},
        value=[1990, 2000],
    ),
            
            
            
    # Affichage de la table complete
    html.Br(),
    html.Hr(),
    html.Label('Table de recherche', style={'fontSize': 20, 'marginTop': 40}),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        editable=True,
        filtering=True,
        sorting=True,
        sorting_type="multi",
        row_selectable="multi",
        row_deletable=True,
        pagination_mode="fe",
        pagination_settings={
                "current_page": 0,
                "page_size": 50,
        },
    )
])
    
