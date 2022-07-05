import pandas as pd
import numpy as np
import seaborn as sns
sns.set_theme() 
import plotly.express as px
import plotly.graph_objects as go
import plotly
import streamlit as st
st.set_page_config(
    page_title="Analyse Macro du dérèglement climatique",
    page_icon="🌍",
)



st.write("# Analyse Macro du dérèglement climatique 🌍")

st.write(df)

st.markdown(
    """
   :bulb: Une **anomalie de température** est l’écart entre la température mesurée par rapport à la température moyenne calculée sur une période d’au moins trente ans. Elle peut être positive ou négative et nous informe ainsi du réchauffement ou refroidissement d’une zone, d’un pays, d’une surface maritime ou même de l'entièreté du globe terrestre.

Les données étudiées sont ainsi des anomalies de température mesurées par rapport à la moyenne de température globale recensée entre 1951 et 1980 (NASA, s.d). Cette période de référence est une valeur standard dans les études climatique de l’époque et est régie par l’Organisation Météorologique Mondiale. Cependant, cette période n’est pas figée et évolue dans le temps car la période de référence doit ainsi représenter les normales climatiques. Ainsi, les normales de 1951-1980 ne sont pas représentatives du climat actuel (Météo France, 2022).

"""
)

df=pd.read_csv('ressources/ZonAnn.Ts+dSST.csv')
fig = px.bar(df, x='Year', y='Glob', color='Glob',color_continuous_scale='RdYlBu_r', labels={"Glob": "Anomaly<br>in °C"})
fig.update_layout(title_text="Temperature Anomaly from 1880 to 2021<br><sup> Period Reference : mean 1951-1980")
st.plotly_chart(fig, use_container_width=False, sharing="streamlit")

st.markdown("""
La courbe représentant les anomalies de température mondiales est croissante avec un plateau, entre 1951 et 1980 expliqué par les moyennes prises sur cette période de référence pour construire les anomalies.

On observe que la pente de la courbe est plus importante entre 1980 et 2020 qu’entre 1900 et 1940, signifiant une accélération du changement climatique
""")


df_zone=pd.read_csv('ressources/df_zone.csv')
fig = px.bar_polar(df_zone, r="Anomalies", theta="Country Name", color="Anomalies", animation_frame="year",
                   animation_group="Country Name" , color_continuous_scale= 'RdYlBu_r', color_continuous_midpoint=0, 
                    range_color=[df_zone["Anomalies"].min(), df_zone["Anomalies"].max()],labels={"Anomalies": "Anomaly<br>in °C"}
                   )
fig.update_layout(title_text="Anomaly per zone from 1961 to 2019 <br><sup> Period Reference : mean 1951-1980")


fig.update_polars(angularaxis_dtick=1, 
                  angularaxis_exponentformat="power")

st.plotly_chart(fig, use_container_width=False, sharing="streamlit")

fig = go.Figure()
fig = px.bar(df_zone, x="Country Name", y='Anomalies', animation_frame="year",animation_group="Country Name" ,range_y=[-2,3], 
             color='Anomalies',color_continuous_scale='RdYlBu_r' , orientation="v",color_continuous_midpoint=0, 
             range_color=[df_zone["Anomalies"].min(), df_zone["Anomalies"].max()],labels={"Anomalies": "Anomaly<br>in °C"}
             )
fig.update_xaxes(
        tickangle = 45,
        title_text = None)

fig.update_layout(title_text="Anomaly per zone from 1961 to 2019 <br><sup> Period Reference : mean 1951-1980")
st.plotly_chart(fig, use_container_width=False, sharing="streamlit")
