import pandas as pd
import numpy as np
import seaborn as sns
sns.set_theme() 
import plotly.express as px
import plotly.graph_objects as go
import plotly
import streamlit as st

st.set_page_config(
    page_title="Projections",
    page_icon="🌍",
)

st.title("Projections pour la fin du siècle")
st.write("Cartes de projections des anomalies")
st.write("Cartes de projections des pays invivables")



st.subheader("Projection de l'invivabilité des pays d'ici 2100")

df26=pd.read_csv("ressources/Dataframe_HI_2_6.csv")
df45=pd.read_csv("ressources/DataFrame_HI_4_5.csv")
df6=pd.read_csv("ressources/DataFrame_HI_6.csv")
df85=pd.read_csv("ressources/Dataframe_HI_8_5.csv")

fig1 = px.choropleth(df26, locations="Country", color="Seuil",range_color=[0,200],
                  color_discrete_sequence=["green","orange","red"],
                   locationmode='country names',color_continuous_midpoint=0,
                    labels={'Annual':'Nb de jour >35°C'})


fig2 = px.choropleth(df45, locations="Country", color="Seuil",range_color=[0,200],
                  color_discrete_sequence=["green","orange","red"],
                   locationmode='country names',color_continuous_midpoint=0)

fig3 = px.choropleth(df6, locations="Country", color="Seuil",range_color=[0,200],
                  color_discrete_sequence=["green","orange","red"],
                   locationmode='country names',color_continuous_midpoint=0)


fig4 = px.choropleth(df85, locations="Country", color="Seuil",range_color=[0,200],
                  color_discrete_sequence=["red","green","orange"],
                   locationmode='country names',color_continuous_midpoint=0)

Choix_selectbox=["RCP2,6","RCP4,5","RCP6","RCP8,5"]

st.selectbox("Quel scénatio voulez vous afficher sous forme de map?", option=Choix_selectbox)
