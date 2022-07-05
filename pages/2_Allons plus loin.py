import pandas as pd
import numpy as np
import seaborn as sns
sns.set_theme() 
import plotly.express as px
import plotly.graph_objects as go
import plotly
import streamlit as st

st.set_page_config(
    page_title="Allons plus loin",
    page_icon="🌍",
)
st.title("Comparaison avec d'autres données")
st.write("Introduction du dataframe Kaggle")
st.write("Graph additionnels kaggle: Boxplot, Relplot, polarplot...")

#Chargement des dataframes Kaggle:
df_country = pd.read_csv("ressources/df_country_kaggle.csv")
df_zone = pd.read_csv("ressources/df_zone_kaggle.csv")
df_country.rename(columns={'Country Code': 'Code'}, inplace=True)
df_zone.rename(columns={'Country Code': 'Code'}, inplace=True) 

col1, col2 = st.columns(2)

with col1:
    st.subheader("Données par pays")
    st.write("Un dataframe répertoriant l'ensemble des anomalies, dans tous les pays du monde, de 1961 à 2015")
    st.dataframe(df_country ,1000, 250)
            

with col2:
    st.subheader("Données par zones")
    st.write("Un DataFrame répertoriant les anomalies, classées par zones, de 1961 à 2015")
    st.dataframe(df_zone, 1000, 250)


st.subheader("Visualisation des données")    
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

