import pandas as pd
import os
import cufflinks as cf
import plotly
import numpy as np

#cf.go_offline()
#cf.set_config_file(offline=True, world_readable=True)


Data = pd.read_csv(r'C:\Users\molly\Documents\__LabNotebook\20200414_Photobleaching tdTomato e coli\20200414_Ecoli_Photobleaching.csv')


Wavelengths = Data.Wavelengths
Spectra = Data.drop(['Wavelengths','Unnamed: 0'], axis = 1)
Spectra.head()


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go # or plotly.express as px
fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
for col in Spectra.columns:
    fig.add_trace(go.Scatter(x=Wavelengths, y=Spectra[col], mode="lines",
                 name=col)
                 )
fig.show()

fig.write_html(r"C:\Users\molly\Documents\__LabNotebook\20200414_Photobleaching tdTomato e coli\Ecoli.html")
    
#fig.update_layout( ... )

#app = dash.Dash()
#app.layout = html.Div([
#    dcc.Graph(figure=fig)
#])

# app.run_server(debug=True, use_reloader=True)  # Turn off reloader if inside Jupyter


