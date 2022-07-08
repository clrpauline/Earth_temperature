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

st.title("Projections pour la fin du siècle🌍")


df26=pd.read_csv("ressources/Dataframe_HI_2_6.csv")
df45=pd.read_csv("ressources/DataFrame_HI_4_5.csv")
df6=pd.read_csv("ressources/DataFrame_HI_6.csv")
df85=pd.read_csv("ressources/Dataframe_HI_8_5.csv")
data=pd.read_csv("ressources/AnomalyScenarios_RCP.csv")
image = Image.open('ressources/RCPexp.png')


fig1 = px.choropleth(df26, locations="Country", color="Seuil",range_color=[0,200],
                  color_discrete_sequence=["green","orange","red"],
                   locationmode='country names',color_continuous_midpoint=0,
                    labels={'Annual':'Nb de jour >35°C'})
fig1.update_layout(autosize=False,margin = dict(l=0,r=0,b=0,t=0,pad=4, autoexpand=True), width=730, legend=dict(yanchor="bottom",y=0.1,xanchor="right",x=0.99, title="Conditions"))



fig2 = px.choropleth(df45, locations="Country", color="Seuil",range_color=[0,200],
                  color_discrete_sequence=["green","orange","red"],
                   locationmode='country names',color_continuous_midpoint=0)
fig2.update_layout(autosize=False,margin = dict(l=0,r=0,b=0,t=0,pad=4, autoexpand=True), width=730, legend=dict(yanchor="bottom",y=0.1,xanchor="right",x=0.99, title="Conditions"))


fig3 = px.choropleth(df6, locations="Country", color="Seuil",range_color=[0,200],
                  color_discrete_sequence=["green","orange","red"],
                   locationmode='country names',color_continuous_midpoint=0)
fig3.update_layout(autosize=False,margin = dict(l=0,r=0,b=0,t=0,pad=4, autoexpand=True), width=730, legend=dict(yanchor="bottom",y=0.1,xanchor="right",x=0.99, title="Conditions"))

fig4 = px.choropleth(df85, locations="Country", color="Seuil",range_color=[0,200],
                  color_discrete_sequence=["red","green","orange"],
                   locationmode='country names',color_continuous_midpoint=0)
fig4.update_layout(autosize=False,margin = dict(l=0,r=0,b=0,t=0,pad=4, autoexpand=True), width=730, legend=dict(yanchor="bottom",y=0.1,xanchor="right",x=0.99, title="Conditions"))

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



Choix_selectbox=["Introduction","RCP2,6: Scénario optimiste","RCP4,5: Scénario moyen bas","RCP6: Scénario moyen haut","RCP8,5: Scénario pessimiste", "Tous les scénarios"]

results = st.sidebar.selectbox("Quel scénario voulez vous afficher sous forme de cartes?", options=Choix_selectbox)


if results == "Introduction":
    st.write("Sur cette page sont centralisées les prédictions qui émanent de notre étude préliminaire. L'objectif de ce rapport étant de répondre à la problématique: **Quels pays deviendront invivables d'ici la fin du siècle?**")
    st.write("Ci-dessous un graphique représentant l'un des élément essentiel de notre analyse, les **RCP (pour Representative Concentration Pathway)**.")
    st.image(image)
    st.write("Comme on le remarque, 4 scénarios ont été prévus pour la fin du siècle (RCP2.6 pour le plus optimiste et RCP8.5 pour le plus pessimiste). Les scénarios RCP sont des prédictions complexes sur l'évolution de notre climat. Elles prennent en compte beaucoup de paramètres comme les émissions de différents gaz à effet de serre, l'activité volcanique, l'impact des radiations solaires.L'unité de mesure globale est le W/M² qui correspond au chiffres après RCP. Nous vous proposons donc de choisir entre les 4 voies possibles qui ont été évaluées par les scientifiques du GIEC (Voir la slidebar)")
    

elif results == "RCP2,6: Scénario optimiste":
    st.subheader("Projection des anomalies par pays en 2100")
    
    st.write("Avec le scénario RCP2,6")
    st.plotly_chart(fig5)
    st.subheader("Projection de l'invabilité des pays d'ici 2100")
    st.write("Avec le scénario RCP2,6")
    st.plotly_chart(fig1)
    st.sidebar.title("Analyse RCP2,6")
    st.sidebar.write("Dans ce scénario qui voit monter légèrement puis baisser les emissions de CO2, l'impact est minime vis à vis des anomalies. Nous resterons donc à des niveaux d'anomalies que nous connaissons actuellement. Aucun pays n'est déclaré invivable dans sa totalité selon nos critères.")
    st.write("Notre classification de l'invivabilité des pays se base sur l'indice de chaleur qui est un calcul entre la température et l'humidité, voici les seuils retenus:")
    st.write("🟩Vivable: Moins de 100 jours >35°C par an")
    st.write("🟧Conditions difficiles: Entre 100 et 200 jours >35°C par an")
    st.write("🟥Invivable: Plus de 200 jours >35°C par an")
    
elif results == "RCP4,5: Scénario moyen bas":
    st.subheader("Projection des anomalies par pays en 2100")
    st.write("Avec le scénario RCP4,5")
    st.plotly_chart(fig6)
    st.subheader("Projection de l'invivabilité des pays d'ici 2100")
    st.write("Avec le scénario RCP2,6")
    st.plotly_chart(fig2) 
    st.sidebar.title("Analyse RCP4,5")
    st.sidebar.write("Ce scénario peut-être plus réaliste prévoit que les anomlies vont progressivement doubler durant le siècle. On atteindra des valeurs de +2,5°C dans la majorité des pays. On voit clairement les pays proches des zones polaires se réchauffer plus vite que la moyenne. La Colombie, l'Afrique de l'Ouest et l'Asie du sud-est deviennent des zones ou les conditions seront difficiles pour vivre")
    st.write("Notre classification de l'invivabilité des pays se base sur l'indice de chaleur qui est un calcul entre la température et l'humidité, voici les seuils retenus:")
    st.write("🟩Vivable: Moins de 100 jours >35°C par an")
    st.write("🟧Conditions difficiles: Entre 100 et 200 jours >35°C par an")
    st.write("🟥Invivable: Plus de 200 jours >35°C par an")
    
elif results == "RCP6: Scénario moyen haut":
    st.subheader("Projection des anomalies par pays en 2100")
    st.write("Avec le scénario RCP6")
    st.plotly_chart(fig7)
    st.subheader("Projection de l'invivabilité des pays d'ici 2100")
    st.write("Avec le scénario RCP6")
    st.plotly_chart(fig3)
    st.sidebar.title("Analyse RCP6")
    st.sidebar.write("Dans ce scénario la tendance des deux premiers se confirme. La moyenne des anomalies tend à tripler par rapport à la période actuelle. Mêmes les zones de l'équateur et tropicales sud ont des anomalies qui dévient beaucoup des températures locales très chaudes. Les zones de conditions difficiles s'étendent dans les zones déjà affectées en RCP4,5. Des dizaines de pays sont maintenant touchés.")
    st.write("Notre classification de l'invivabilité des pays se base sur l'indice de chaleur qui est un calcul entre la température et l'humidité, voici les seuils retenus:")
    st.write("🟩Vivable: Moins de 100 jours >35°C par an")
    st.write("🟧Conditions difficiles: Entre 100 et 200 jours >35°C par an")
    st.write("🟥Invivable: Plus de 200 jours >35°C par an")
    
elif results == "RCP8,5: Scénario pessimiste":
    st.subheader("Projection des anomalies par pays en 2100")
    st.write("Avec le scénario RCP8,5")
    st.plotly_chart(fig8)
    st.subheader("Projection de l'invivabilité des pays d'ici 2100")
    st.write("Avec le scénario RCP8,5")
    st.plotly_chart(fig4)
    st.sidebar.title("Analyse RCP8,5")
    st.sidebar.write("Le pire scénario selon le GIEC, la tendance d'émission de CO2 s'intensifie avec le développement humain. Les anomalies s'emballent et modifient l'ensemble du climat pour de bon. Notre planète avance à grand pas vers un avenir inhospitalier. Les zones qui jusquà maintenant avaient des conditions difficiles deviennent invivables.")
    st.write("Notre classification de l'invivabilité des pays se base sur l'indice de chaleur qui est un calcul entre la température et l'humidité, voici les seuils retenus:")
    st.write("🟩Vivable: Moins de 100 jours >35°C par an")
    st.write("🟧Conditions difficiles: Entre 100 et 200 jours >35°C par an")
    st.write("🟥Invivable: Plus de 200 jours >35°C par an")
    
elif results == "Tous les scénarios":
    st.subheader("Projection des anomalies par pays en 2100")
    st.write("Avec le scénario RCP2,6")
    st.plotly_chart(fig5)
    st.write("Avec le scénario RCP4,5")
    st.plotly_chart(fig6)
    st.write("Avec le scénario RCP6")
    st.plotly_chart(fig7)
    st.write("Avec le scénario RCP8,5")
    st.plotly_chart(fig8)
    st.subheader("Projection de l'invivabilité des pays d'ici 2100")
    st.write("Avec le scénario RCP2,6")
    st.plotly_chart(fig1)
    st.write("Avec le scénario RCP4,5")
    st.plotly_chart(fig2)
    st.write("Avec le scénario RCP6")
    st.plotly_chart(fig3)
    st.write("Avec le scénario RCP8,5")
    st.plotly_chart(fig4)
    st.sidebar.title("Analyse Globale")
    st.sidebar.write("Une page qui vous permet d'explorer l'ensemble des scénarios. Selon vous, lequel est le plus probable?")
    st.write("Notre classification de l'invivabilité des pays se base sur l'indice de chaleur qui est un calcul entre la température et l'humidité, voici les seuils retenus:")
    st.write("🟩Vivable: Moins de 100 jours >35°C par an")
    st.write("🟧Conditions difficiles: Entre 100 et 200 jours >35°C par an")
    st.write("🟥Invivable: Plus de 200 jours >35°C par an")
    
   
