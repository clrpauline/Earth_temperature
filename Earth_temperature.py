import pandas as pd
import numpy as np
import seaborn as sns
sns.set_theme() 
import plotly.express as px
import plotly.graph_objects as go
import plotly
import streamlit as st

st.set_page_config(
    page_title="Earth Temperature",
    page_icon="🌍",
)

st.sidebar.title("Credits")
st.sidebar.write("**Made with love by:**")
st.sidebar.write("🤖Pauline Cellier")
st.sidebar.write("🐸Mariella Goebl")
st.sidebar.write("🦆Guillaume Chavanne")
     
                           

st.markdown("<h1 style='text-align: center; '>Analyse du dérèglement climatique et projections 🌍</h1>", unsafe_allow_html=True)
st.write("""Dans cette étude, vous sera présenté notre analyse réchauffement climatique, du début de la révolution industrielle, jusqu'à la fin du XXIe siècle. 
Les données analysées sont des anomalies de température qui proviennent de différentes sources de données récupérées et citées ci-dessous.
""")
st.write(""" 
💡 Une **anomalie de température** est l’écart entre la température mesurée par rapport à la température moyenne calculée sur une période d’au moins trente ans. 
Elle peut être positive ou négative et nous informe ainsi du réchauffement ou refroidissement d’une zone, d’un pays, d’une surface maritime ou même de l'entièreté du globe terrestre.
""")

st.markdown("""
Afin de pouvoir évaluer et constater ce dérèglement climatique, nous avons décidé d’étudier les **anomalies de température** issues de différents datasets (NASA, Kaggle, World Bank, CMIP 5) : 
- Analyse du dérèglement climatique à **l’échelle globale** grâce aux données récupérées sur le site de la NASA;
- Réduction du maillage afin de constater si l’analyse reste la même que précédemment lorsque l'on analyse les **données par continents et pays**; 
- Pour finir, nous essayerons de nous projeter dans un futur plus ou moins proche (2100) afin d’observer **quel potentiel avenir est attendu pour le monde actuel**

""")

st.markdown("<h2 style='text-align: center; '>Jeux de données utilisés</h2>", unsafe_allow_html=True)
genre = st.radio('',
     ('Dataset principal : NASA', 'Dataset par pays : Kaggle', 'Dataset des projections par pays : CMIP 5 et World Bank '))

if genre == 'Dataset principal : NASA':
     df_annuel=pd.read_csv('ressources/ZonAnn.Ts+dSST.csv')
     df_per_zones=pd.read_csv('ressources/DataFrame_anomaly_per_zones.csv')
     df_per_zones=df_per_zones.drop('Unnamed: 0',axis=1)
     st.subheader('Source :')
     st.write("Les données sont les anomalies de température calculées par la NASA, plus précisément du GISS (Goddard Institute for Space Studies). Ces données sont des estimations globales issues des stations météorologiques du regroupement de plusieurs sources :")
     st.write("- Le NOAA GHCN v4 pour les mesures des stations météorologiques terrestres;")
     st.write("- Le ERSST v5 pour les mesures océaniques.")

     st.markdown("**Unités de mesures :** Degré Celsius")

     st.subheader('Datasets :')
     col1, col2 = st.columns(2)

     with col1:
        st.write("**Données Globales par zone géographique**")
        st.write("*Données annuelles de 1880 à 2021, période de référence : 1951-1980*")
        st.dataframe(df_annuel ,1000, 250)
    
     with col2:
        st.write("**Données Globales par Hémisphère et par Mois**")
        st.write("*Données annuelles de 1880 à 2021, période de référence : 1951-1980*")
        st.dataframe(df_per_zones ,1000, 250)



elif genre== 'Dataset par pays : Kaggle':
     df_country=pd.read_csv('ressources/df_country.csv')
     df_zones=pd.read_csv('ressources/df_zone.csv')
     st.subheader('Source :')
     st.write("Les données sont les anomalies de température calculées par la Food and Agriculture Organization of the United Nations.")
     
     st.markdown("**Unités de mesures :** Degré Celsius")

     st.subheader('Datasets :')
     col1, col2 = st.columns(2)

     with col1:
        st.write("**Anomalies de température par pays et par an**")
        st.write("*Données annuelles de 1961 à 2019, période de référence : 1951-1980*")
        st.dataframe(df_country ,1000, 250)
    
     with col2:
        st.write("**Anomalies de température par zones et par an**")
        st.write("*Données annuelles de 1961 à 2019, période de référence : 1951-1980*")
        st.dataframe(df_zones ,1000, 250)

elif genre== 'Dataset des projections par pays : CMIP 5 et World Bank ' :
     df_HI= pd.read_csv('ressources/DataFrame_HI_6.csv')
     df_RCP= pd.read_csv('ressources/RCP6.csv')
     df_RCP=df_RCP.drop('Unnamed: 0',axis=1)
     df_proj_pays=pd.read_csv('ressources/AnomalyScenarios_RCP.csv')

     st.subheader('Sources :')
     st.markdown("""
     Le modèle appelé CMIP5 (Coupled Model Intercomparison Project v5 ), est un protocole expérimental qui a été développé et publié en 2013 dans le cadre du programme de recherche sur le climat mondial (World Climate Research Program) (Program for Climate Model Diagnosis & Intercomparison, 2013). Il s’agit de quatres scénarios où un forçage radiatif, dépendant du comportement humain sur les années à venir, est appliqué.  En effet, le dérèglement climatique ne peut pas être prédit avec un unique scénario étant donné la multiplicité des paramètres et la corrélation de ces derniers avec le comportement humain (CoastAdapt, s.d).


     Les scientifiques ont ainsi mis en place quatres différents scénarios, du “meilleur” au “pire” :
     
     - **RCP 2.6**, où les efforts pour réduire les émissions sont importants et ou l’anomalie de température globale à 2100 croît puis diminue à +1°C (comparée à la moyenne de 1986 à 2005);
     - **RCP 4.5**, où les efforts pour réduire les émission sont modérés et ou l’anomalie de température globale à 2100 croît jusqu’à +1,8°C (comparée à la moyenne de 1986 à 2005);
     - **RCP 6**, où les efforts sont faibles pour réduire les différentes émissions et ou l’anomalie de température globale à 2100  croît jusqu’à 2,2°C (comparée à la moyenne de 1986 à 2005);
     - **RCP 8.5**, où il n’y a presque pas d’effort de fait pour réduire les émissions et où l'anomalie de température globale à 2100 croît jusqu’à 3,7°C (comparée à la moyenne de 1986 à 2005).
     """)

     st.subheader('Datasets :')
     st.markdown("<h4 style='text-align: center; '>Projection des radiations via forçage selon le RCP</h4>", unsafe_allow_html=True)
     st.markdown('**Unité de mesure :** W/m^2')
     st.dataframe(df_RCP )

     st.markdown("<h4 style='text-align: center; '>Projection des anomalies de température par pays et selon le RCP</h4>", unsafe_allow_html=True)
     st.markdown("""
     - **Collection :** CMIP5 Projections
     - **Variable :** Mean-Temperature
     - **Période :** 2080-2099
     - **Agrégation :** Annual
     - **Calcul :** Anomaly (from Reference Period, 1986-2005)
     - **Percentile :** Median (50th)
     - **Scénarios :** RCP 2.6; RCP 4.5; RCP 6; RCP 8.5
     - **Modèle :** Multi-Model Ensemble
     - **Unité de mesure :** Degré Celsius
     """)
     st.dataframe(df_proj_pays)    

     st.markdown("<h4 style='text-align: center; '>Projection du nombre de jour avec un Heat Index > 35°C  par pays et selon le RCP</h4>", unsafe_allow_html=True)
     st.markdown("""
     - **Collection :** CMIP5 Projections
     - **Variable :** Heat index
     - **Période :** 2080-2099
     - **Agrégation :** Annual
     - **Calcul :** Anomaly (from Reference Period, 1986-2005)
     - **Percentile :** Median (50th)
     - **Scénarios :** RCP 2.6; RCP 4.5; RCP 6; RCP 8.5
     - **Modèle :** Multi-Model Ensemble

     """)
     st.dataframe(df_HI )    
    
st.header("Exploration des données")
st.markdown("**Langage utilisé :** Python")
st.markdown("**Librairies utilisées :** Pandas, Numpy, Matplotlib, Seaborn, Plotly, Bokeh, Scikit-learn")
st.markdown("**Valeurs manquantes :** Les valeurs manquantes sont identifiées par 3 astérisques, ces valeurs ont été supprimées du dataframe.")

st.header("Bibliographie")
st.markdown("""
**Jeux de données**

Kaggle (2020). Climate Change Dataset. Climate Change | Kaggle

NASA (s.d).GISTEMPS Datasets.  GISS Surface Temperature Analysis (GISTEMP v4)

Potsdam Institute for Climate Impact Research (s.d). RCP Concentration Calculations and Dat, Final Version, background data, acknowledgements and further info. RCP Scenario data group

World Bank Group (s.d).  Download Data : Climatology World Bank | Climate Change Knowledge Portal 

**Autres sources**

CoastAdapt (s.d.). What are the RCPs ?. What are the RCPs? | CoastAdapt

Ecologie.gouv (2018). Changement climatique : causes, effets et enjeux. Changement climatique | Ecologie.gouv

Feulner, Rahmstorf and all. (2013). Why is the Northern Hemisphere warmer than the Southern Hemisphere?. Geophysical Research Abstracts. Geophysical Research Abstracts

Futura-Science (2021). Vers des étés qui dureront six mois avec le réchauffement climatique. Vers des étés qui dureront six mois.

JM.Jancovici (2007). Qu’est-ce qu’un modèle climatique ? Quels sont leurs premières conclusions ? Qu'est-ce qu'un modèle climatique ? Quels sont leurs premières conclusions.

Kang, Seager (2014). Croll revisited: Why is the northern hemisphere warmer than the southern hemisphere ?. Columbia University, New York. Croll Revisited: Why is the Northern Hemisphere Warmer than the Southern Hemisphere? 

Le Point (2019). Étude : les sujets de conversation préférés des Français. Etude | Le Point

Météo France (Juin 2022). De nouvelles normales pour qualifier le climat en France. De nouvelles normales pour qualifier le climat | Meteo France

Program for Climate Model Diagnosis & Intercomparison (2013). CMIP5 Overview. CMIP5 - Coupled Model Intercomparison Project Phase 5 - Overview

Save4Planet (2022). Réchauffement climatique : définition, causes et conséquences. Réchauffement climatique | Save4Planet.com

Weather.gov (s.d). What is the Heat Index? (Index de chaleur). Heat Index | Weather.gov

""")


