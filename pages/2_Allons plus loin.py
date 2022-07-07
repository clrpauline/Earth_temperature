import pandas as pd
import numpy as np
import seaborn as sns
sns.set_theme() 
import plotly.express as px
import plotly.graph_objects as go
import plotly
import streamlit as st

st.markdown("<h1 style='text-align: center; '>Analyse des anomalies de température par zones et pays 🌍</h1>", unsafe_allow_html=True)


st.write("Pour aller plus loin, nous avons ainsi récupéré un jeu de données rescensant les anomalies de température par continents et par pays de 1961 à 2019. Ces anomalies sont comparées à la moyenne de température entre 1951 et 1980.")

genre = st.radio('',
     ('Par Continents ', 'Par Pays'))

if genre == 'Par Continents ':
     st.markdown("<h3 style='text-align: center; '>Analyse des anomalies de température par zones de 1961 à 2019 </h3>", unsafe_allow_html=True)   
     df_zone=pd.read_csv('ressources/df_zone.csv')
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
     st.markdown("""
     Une fois de plus la tendance est claire, plus nous avançons dans le temps, plus les anomalies augmentent en températures et ce dans l’ensemble des zones géographiques. 
     Ce graphique met aussi en avant les zones où les anomalies semblent progresser plus rapidement que la moyenne mondiale (Europe et Afrique).
     """)
else :
     st.markdown("<h3 style='text-align: center; '>Analyse des anomalies de température par pays de 1961 à 2019 </h3>", unsafe_allow_html=True)   

     df=pd.read_csv('ressources/Temperature_change_Data.csv')
     df=df.replace({"URSS": "Russia",})
     df=df.rename({'tem_change':'Anomalies'}, axis=1)
     fig = px.choropleth(df, locations="Country Name", color="Anomalies",
                    color_continuous_scale='RdYlBu_r', animation_group="Country Name",
                    locationmode='country names', animation_frame="year", color_continuous_midpoint=0, 
                   range_color=[-2, 3]
             )
     fig.update_layout(title_text="Anomaly from 1961 to 2019 <br><sup> Period Reference : mean 1951-1980")
     st.plotly_chart(fig, use_container_width=False, sharing="streamlit")
     st.markdown("""Il est ainsi évident qu’en 50 ans, nous avons des anomalies de températures qui ont radicalement évoluées avec en 1969 des anomalies autour de 0°C tandis qu’en 2019, ces dernières se situent autour des 1°C à 2°C selon les pays, suivant ainsi la courbe globale de l’évolution des anomalies de température. On peut ainsi également observer que les pays de l’hémisphère Nord ont plus de variation de température que les pays de l’hémisphère Sud.""")

st.markdown('Etant donné la croissance de ces anomalies, engendrant des températures extrêmes, une question importante pour les prochaines années se pose : il y aura-t-il des pays définis comme invivables d’ici quelques années ?')
