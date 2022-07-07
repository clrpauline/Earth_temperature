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
st.title("Etude du réchauffement climatique de 1880 à 2100")
st.write("Dans cette étude vous sera présenté une vision objective et factuelle du réchauffement climatique, du début de la révolution industrielle, jusqu'à la fin du XXIe siècle. Les données interactives et visuelles proviennent de mesures de la NASA, plus particulièrement du GISS (Goddard Institute for Space Studies).")
st.write("Les projections que nous proposons pour le futurs proviennent elles de modèles de machine learning ou de modèles statistiques basées sur les mesures passées. Un phénomène si complexe de le réchauffement climatique ne saurait se prévoir purement grâce mesures d'hier mais seront fortement impactés par les choix que nous ferons.")



st.header("1. Jeux de données utilisés")
genre = st.radio('',
     ('Dataset principal : NASA', 'Dataset par pays : Kaggle', 'Dataset des projections par pays : CMIP 5 et World Bank '))

if genre == 'Dataset principal : NASA':
     df_annuel=pd.read_csv('ZonAnn.Ts+dSST.csv')
     df_per_zones=pd.read_csv('DataFrame_anomaly_per_zones.csv')
     df_per_zones=df_per_zones.drop('Unnamed: 0',axis=1)
     st.subheader('Source :')
     st.write("Les données sont anomalies de température calculées par la NASA, plus précisément du GISS (Goddard Institute for Space Studies). Ces données sont des estimations globales issues des stations météorologiques du regroupement de plusieurs sources :")
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
     df_country=pd.read_csv('df_country.csv')
     df_zones=pd.read_csv('df_zone.csv')
     st.subheader('Source :')
     st.write("Les données sont anomalies de température calculées par la Food and Agriculture Organization of the United Nations :")
     
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
     df_HI= pd.read_csv('Dataframe_HI_6.csv')
     df_RCP= pd.read_csv('RCP6.csv')
     df_RCP=df_RCP.drop('Unnamed: 0',axis=1)
     df_proj_pays=pd.read_csv('AnomalyScenarios_RCP.csv')

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
     st.markdown('**Projection des radiations via forçage selon le RCP**')
     st.markdown('**Unité de mesure :** W/m^2')
     st.dataframe(df_RCP )

     st.markdown('**Projection des anomalies de température par pays et selon le RCP**')
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

     st.markdown('**Projection du nombre de jour avec un Heat Index > 35°C  par pays et selon le RCP**')
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
    
st.header("2. Exploration des données")
st.markdown("**Langage utilisé :** Python")
st.markdown("**Librairies utilisées :** Pandas, Numpy, Matplotlib, Seaborn, Plotly, Bokeh, Scikit-learn")
st.markdown("**Valeurs manquantes :** Les valeurs manquantes sont identifiées par 3 astérisques, ces valeurs ont été supprimées du dataframe.")


