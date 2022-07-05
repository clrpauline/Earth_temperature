import pandas as pd
import numpy as np
import seaborn as sns
sns.set_theme() 
import plotly.express as px
import plotly.graph_objects as go
import plotly
import streamlit as st

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
    st.subheader("DataFrame par Pays")
    st.write("Le DataFrame des anomalies dans tous les pays du monde de 1961 à 2015")
    st.dataframe(df_country ,1000, 500)
            

with col2:
    st.subheader("DataFrame par Zone")
    st.write("Le DataFrame des anomalies classées par zones de 1961 à 2015")
    st.dataframe(df_zone, 1000, 500)


