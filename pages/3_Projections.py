import pandas as pd
import numpy as np
import seaborn as sns
sns.set_theme() 
import plotly.express as px
import plotly.graph_objects as go
import plotly
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Projections",
    page_icon="🌍",
)

st.title("Projections pour la fin du siècle")
st.write("Sur cette page sont centralisées les prédictions qui émanent de notre étude préliminaire. L'objectif de ce rapport étant de répondre à la problématique: **Quels pays deviendront invivables d'ici la fin du siècle?**")
st.write("Ci-dessous un graphique représentant l'un des élément essentiel de notre analyse, les **RCP (pour Representative Concentration Pathway)**.")

df26=pd.read_csv("ressources/Dataframe_HI_2_6.csv")
df45=pd.read_csv("ressources/DataFrame_HI_4_5.csv")
df6=pd.read_csv("ressources/DataFrame_HI_6.csv")
df85=pd.read_csv("ressources/Dataframe_HI_8_5.csv")
data=pd.read_csv("ressources/AnomalyScenarios_RCP.csv")
image = Image.open('ressources/RCP représentation.png')

st.image(image)

fig1 = px.choropleth(df26, locations="Country", color="Seuil",range_color=[0,200],
                  color_discrete_sequence=["green","orange","red"],
                   locationmode='country names',color_continuous_midpoint=0,
                    labels={'Annual':'Nb de jour >35°C'})
fig1.update_layout(autosize=False,margin = dict(l=0,r=0,b=0,t=0,pad=4, autoexpand=True), width=730, legend=dict(yanchor="top",y=0.99,xanchor="right",x=0.99))



fig2 = px.choropleth(df45, locations="Country", color="Seuil",range_color=[0,200],
                  color_discrete_sequence=["green","orange","red"],
                   locationmode='country names',color_continuous_midpoint=0)
fig2.update_layout(autosize=False,margin = dict(l=0,r=0,b=0,t=0,pad=4, autoexpand=True), width=730, legend=dict(yanchor="top",y=0.99,xanchor="right",x=0.99))


fig3 = px.choropleth(df6, locations="Country", color="Seuil",range_color=[0,200],
                  color_discrete_sequence=["green","orange","red"],
                   locationmode='country names',color_continuous_midpoint=0)
fig3.update_layout(autosize=False,margin = dict(l=0,r=0,b=0,t=0,pad=4, autoexpand=True), width=730, legend=dict(yanchor="top",y=0.99,xanchor="right",x=0.99))

fig4 = px.choropleth(df85, locations="Country", color="Seuil",range_color=[0,200],
                  color_discrete_sequence=["red","green","orange"],
                   locationmode='country names',color_continuous_midpoint=0)
fig4.update_layout(autosize=False,margin = dict(l=0,r=0,b=0,t=0,pad=4, autoexpand=True), width=730, legend=dict(yanchor="top",y=0.99,xanchor="right",x=0.99))

fig5 = px.choropleth(data, locations="Country", color = "RCP 2.6", range_color=[-8,8],
                    color_continuous_scale='turbo',locationmode='country names', 
                    color_continuous_midpoint=0, labels={"RCP 2.6": "Anomaly<br>in °C"})
fig5.update_layout(autosize=False,margin = dict(l=0,r=0,b=0,t=0,pad=4, autoexpand=True), width=800)

fig6 = px.choropleth(data, locations="Country", color = "RCP 4.5", range_color=[-8,8],
                    color_continuous_scale='turbo', locationmode='country names', 
                    color_continuous_midpoint=0, labels={"RCP 4.5": "Anomaly<br>in °C"})
fig6.update_layout(autosize=False,margin = dict(l=0,r=0,b=0,t=0,pad=4, autoexpand=True), width=800)

fig7 = px.choropleth(data, locations="Country", color = "RCP 6", range_color=[-8,8],
                    color_continuous_scale='turbo', locationmode='country names', 
                    color_continuous_midpoint=0, labels={"RCP 6": "Anomaly<br>in °C"})
fig7.update_layout(autosize=False,margin = dict(l=0,r=0,b=0,t=0,pad=4, autoexpand=True), width=800)

fig8 = px.choropleth(data, locations="Country", color = "RCP 8.5", range_color=[-8,8],
                    color_continuous_scale='turbo', locationmode='country names', 
                    color_continuous_midpoint=0, labels={"RCP 8.5": "Anomaly<br>in °C"})
fig8.update_layout(autosize=False,margin = dict(l=0,r=0,b=0,t=0,pad=4, autoexpand=True), width=800)



Choix_selectbox=[" ","RCP2,6: Scénario optimiste","RCP4,5: Scénario moyen bas","RCP6: Scénario moyen haut","RCP8,5: Scénario pessimiste", "Tous les scénarios"]
st.write("Comme on le remarque, 4 scénarios ont été prévus pour la fin du siècle (RCP2.6 pour le plus optimiste et RCP8.5 pour le plus pessimiste). Les scénarios RCP sont des prédictions complexes sur l'évolution de notre climat jusqu'à la fin du siècle. Elles prennent en compte enormément de paramètres comme les emissions de différents gaz à effet de serre, l'activité volcanique, l'impact des radiations solaires mmais tout est ici représenté en terme de CO2 pour faciliter la compréhension. Nous vous proposons de choisir entre les 4 voies possibles qui ont été évaluées par les scientifiques du GIEC:")

results = st.selectbox("Quel scénario voulez vous afficher sous forme de cartes?", options=Choix_selectbox)

if results == "RCP2,6: Scénario optimiste":
    st.subheader("Projection des anomalies par pays en 2100")
    
    st.write("Avec le scénario RCP2,6")
    st.plotly_chart(fig5)
    st.subheader("Projection de l'invabilité des pays d'ici 2100")
    st.write("Avec le scénario RCP2,6")
    st.plotly_chart(fig1)
    st.sidebar.title("Analyse RCP2,6")
    st.sidebar.write("Salut")
    
elif results == "RCP4,5: Scénario moyen bas":
    st.subheader("Projection des anomalies par pays en 2100")
    st.write("Avec le scénario RCP4,5")
    st.plotly_chart(fig6)
    st.subheader("Projection de l'invivabilité des pays d'ici 2100")
    st.write("Avec le scénario RCP2,6")
    st.plotly_chart(fig2) 
    st.sidebar.title("Analyse RCP4,5")
    st.sidebar.write("Salut")
    
elif results == "RCP6: Scénario moyen haut":
    st.subheader("Projection des anomalies par pays en 2100")
    st.write("Avec le scénario RCP6")
    st.plotly_chart(fig7)
    st.subheader("Projection de l'invivabilité des pays d'ici 2100")
    st.write("Avec le scénario RCP6")
    st.plotly_chart(fig3)
    st.sidebar.title("Analyse RCP6")
    st.sidebar.write("Salut")
    
elif results == "RCP8,5: Scénario pessimiste":
    st.subheader("Projection des anomalies par pays en 2100")
    st.write("Avec le scénario RCP8,5")
    st.plotly_chart(fig8)
    st.subheader("Projection de l'invivabilité des pays d'ici 2100")
    st.write("Avec le scénario RCP8,5")
    st.plotly_chart(fig4)
    st.sidebar.title("Analyse RCP8,5")
    st.sidebar.write("Salut")
    
elif results == "Tous les scénarios":
    st.subheader("Projection de l'invivabilité des pays d'ici 2100")
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
    st.plotly_chart(fig3)
    st.plotly_chart(fig4)
    st.subheader("Projection des anomalies par pays en 2100")
    st.plotly_chart(fig5)
    st.plotly_chart(fig6)
    st.plotly_chart(fig7)
    st.plotly_chart(fig8)
    st.sidebar.title("Analyse Globale")
    st.sidebar.write("Salut")
    
   
