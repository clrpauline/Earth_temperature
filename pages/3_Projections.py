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


df26=pd.read_csv("ressources/Dataframe_HI_2_6.csv")
df45=pd.read_csv("ressources/DataFrame_HI_4_5.csv")
df6=pd.read_csv("ressources/DataFrame_HI_6.csv")
df85=pd.read_csv("ressources/Dataframe_HI_8_5.csv")

fig1 = px.choropleth(df26, locations="Country", color="Seuil",range_color=[0,200],
                  color_discrete_sequence=["green","orange","red"],
                   locationmode='country names',color_continuous_midpoint=0,
                    labels={'Annual':'Nb de jour >35°C'})
fig1.update_layout(autosize=False,margin = dict(l=0,r=0,b=0,t=0,pad=4, autoexpand=True), width=800)


fig2 = px.choropleth(df45, locations="Country", color="Seuil",range_color=[0,200],
                  color_discrete_sequence=["green","orange","red"],
                   locationmode='country names',color_continuous_midpoint=0)
fig2.update_layout(autosize=False,margin = dict(l=0,r=0,b=0,t=0,pad=4, autoexpand=True), width=800)


fig3 = px.choropleth(df6, locations="Country", color="Seuil",range_color=[0,200],
                  color_discrete_sequence=["green","orange","red"],
                   locationmode='country names',color_continuous_midpoint=0)
fig3.update_layout(autosize=False,margin = dict(l=0,r=0,b=0,t=0,pad=4, autoexpand=True), width=800)

fig4 = px.choropleth(df85, locations="Country", color="Seuil",range_color=[0,200],
                  color_discrete_sequence=["red","green","orange"],
                   locationmode='country names',color_continuous_midpoint=0)
fig4.update_layout(autosize=False,margin = dict(l=0,r=0,b=0,t=0,pad=4, autoexpand=True), width=800)

fig5 = px.choropleth(data, locations="Country", color = "RCP 2.6", range_color=[-8,8],
                    color_continuous_scale='turbo',locationmode='country names', 
                    color_continuous_midpoint=0, labels={"RCP 2.6": "Anomaly<br>in °C"})
fig5.update_layout(title_text="Anomaly projection for End of Century (2080-'99) <br><sup>...assuming Scenario RCP 2.6</sup>", font=dict(size=20))

fig6 = px.choropleth(data, locations="Country", color = "RCP 4.5", range_color=[-8,8],
                    color_continuous_scale='turbo', locationmode='country names', 
                    color_continuous_midpoint=0, labels={"RCP 4.5": "Anomaly<br>in °C"})
fig5.update_layout(title_text="<sup>...assuming Scenario RCP 4.5</sup>", font=dict(size=20))

fig7 = px.choropleth(data, locations="Country", color = "RCP 6", range_color=[-8,8],
                    color_continuous_scale='turbo', locationmode='country names', 
                    color_continuous_midpoint=0, labels={"RCP 6": "Anomaly<br>in °C"})
fig7.update_layout(title_text="<sup>...assuming Scenario RCP 6</sup>", font=dict(size=20))

fig8 = px.choropleth(data, locations="Country", color = "RCP 8.5", range_color=[-8,8],
                    color_continuous_scale='turbo', locationmode='country names', 
                    color_continuous_midpoint=0, labels={"RCP 8.5": "Anomaly<br>in °C"})
fig8.update_layout(title_text="<sup>...assuming Scenario RCP 8.5</sup>", font=dict(size=20))



Choix_selectbox=[" ","RCP2,6: Scénario optimiste","RCP4,5: Scénario moyen bas","RCP6: Scénario moyen haut","RCP8,5: Scénario pessimiste"]
st.write("Les scénarios RCP sont des prédictions complexes sur l'évolution de notre climat jusqu'à la fin du siècle. Elles prennent en compte enormément de paramètres comme les emissions de différents gaz à effet de serre, l'activité volcanique, l'impact du solaire... Nous vous proposons de choisir entre les 4 choix possibles qui ont été évalué par les scientifiques:")
results = st.selectbox("Quel scénario voulez vous afficher sous forme de map?", options=Choix_selectbox)

if results == "RCP2,6: Scénario optimiste":
    st.subheader("Projection de l'invivabilité des pays d'ici 2100")
    st.write("Avec le scénario RCP2,6")
    st.plotly_chart(fig1)
    st.plotly_chart(fig5)
elif results == "RCP4,5: Scénario moyen bas":
    st.subheader("Projection de l'invivabilité des pays d'ici 2100")
    st.write("Avec le scénario RCP4,5")
    st.plotly_chart(fig2)
    st.plotly_chart(fig6)               
elif results == "RCP6: Scénario moyen haut":
    st.subheader("Projection de l'invivabilité des pays d'ici 2100")
    st.write("Avec le scénario RCP6")
    st.plotly_chart(fig3)
    st.plotly_chart(fig7)
elif results == "RCP8,5: Scénario pessimiste":
    st.subheader("Projection de l'invivabilité des pays d'ici 2100")
    st.write("Avec le scénario RCP8,5")
    st.plotly_chart(fig4)
    st.plotly_chart(fig8)
    
    
   
