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

st.write("# Analyse macro du dérèglement climatique 🌍")

st.write("Les données étudiées sont ainsi des anomalies de température mesurées par rapport à la moyenne de température globale recensée entre 1951 et 1980 (NASA, s.d). Cette période de référence est une valeur standard dans les études climatique de l’époque et est régie par l’Organisation Météorologique Mondiale. Cependant, cette période n’est pas figée et évolue dans le temps car la période de référence doit ainsi représenter les normales climatiques. Ainsi, les normales de 1951-1980 ne sont pas représentatives du climat actuel (Météo France, 2022).")
df=pd.read_csv('ressources/ZonAnn.Ts+dSST.csv')
st.subheader("Evolution des anomalies de températures mondiales de 1880 à 2021")
fig = px.bar(df, x='Year', y='Glob', color='Glob',color_continuous_scale='RdYlBu_r', labels={"Glob": "Anomaly<br>in °C"})
fig.update_layout(title_text="Temperature Anomaly from 1880 to 2021<br><sup> Period Reference : mean 1951-1980")
st.plotly_chart(fig, use_container_width=False, sharing="streamlit")

st.markdown("""
La courbe représentant les anomalies de température mondiales est croissante avec un plateau, entre 1951 et 1980 expliqué par les moyennes prises sur cette période de référence pour construire les anomalies.

On observe que la pente de la courbe est plus importante entre 1980 et 2020 qu’entre 1900 et 1940, signifiant une accélération du changement climatique
""")
st.markdown("""Afin de détailler un peu plus notre analyse, nous avons voulu observer si :
- Les anomalies sont indépendantes des saisons et des mois
- Les anomalies sont indépendantes des différentes zones de la planète
""")

genre = st.radio("Afficher l'analyse par :",
     ('Zones', 'Saisons'))

if genre == 'Zones':
     st.markdown("Examinons maintenant les anomalies séparées par hémisphères :")
     zones=pd.read_csv("ressources/AnomalyZones.csv")
     zones.drop(columns='Unnamed: 0', inplace=True)
     zones=zones[zones['Year'] != 2022]
     zones=zones[zones['Zone']!='Global']
     zones= zones.sort_values(by = ["Year", "Zone"])
     zones['Anomaly']=(zones['Jan']+zones['Feb']+zones['Mar']+zones['Apr']+zones['May']+zones['Jun']+zones['Jul']+zones['Aug']+zones['Sep']+zones['Oct']+zones['Nov']+zones['Dec'])/12

     fig = px.bar(zones, x='Zone', y='Anomaly', color='Anomaly',color_continuous_scale='RdYlBu_r', labels={"Anomaly": "Anomaly<br>in °C"})
     fig.update_layout(title_text="Temperature Anomaly from 1880 to 2021<br><sup> Period Reference : mean 1951-1980")
     st.plotly_chart(fig, use_container_width=False, sharing="streamlit")

     st.markdown("""On note que les anomalies sont plus importantes sur l’hémisphère Nord tandis que l’hémisphère Sud croît moins rapidement, ce qui va dans le sens des observations scientifiques. En effet, l'hémisphère Nord est connu pour être plus chaud que l'hémisphère sud, notamment dû au ratio surface  terrestre/surface maritime et au courant des océans réchauffant l’hémisphère Nord  (Feulner and all. ,2013 & Kang, Seager, 2014).
     Pour analyser l'évolution des anomalies par zone au fil du temps, regardons le graphique à barres animé ci-dessous : 
     """)

     fig = go.Figure()
     fig = px.bar(zones, x="Zone", y='Anomaly', animation_frame="Year",animation_group="Zone" ,range_y=[-2,2], 
              color='Anomaly',color_continuous_scale='RdYlBu_r' , orientation="v",color_continuous_midpoint=0, 
              range_color=[zones["Anomaly"].min(), zones["Anomaly"].max()],labels={"Anomaly": "Anomalies <br>en °C"}
              )
     fig.update_xaxes(
         tickangle = 45,
         title_text = None)

     fig.update_layout(title_text="Anomalies de température par zone (nord & sud) de 1880 à2021 <br><sup> Période de référence : 1951-1980")
     st.plotly_chart(fig, use_container_width=False, sharing="streamlit")

     st.markdown("""
      On peut alors observer que c'est à partir du 21ème siècle que les anomalies ne semblent pas réparties homogénéiquement entre l’hémisphère Nord et l’hémisphère Sud.
      Pour confirmer cette observation, regardons le test ANOVA sur l'indépendance de l'anomalie et les zones. Le résultat confirme l'observation: il dépend de la période de temps.
      """)
     st.image('ressources/ANOVA_northsouth_full.jpg')
     st.image('ressources/ANOVA_northsouth_recent.jpg')
     st.markdown("""
      Les résultats des tests pour les données de 1880-2021 montrent que la zone n'a pas d'effet statistiquement significatif sur l'anomalie mesurée.
      Les résultats des tests pour les mêmes données, mais de 1980 à 2021 (c'est-à-dire des périodes plus récentes) montrent que la zone a un effet important sur l'anomalie.

      On peut donc conclure que - dans les périodes plus récentes - les zones divergent dans l'évolution de l'anomalie de température : les deux zones se réchauffent, mais l'hémisphère Nord se réchauffe plus rapidement que la moyenne mondiale, tandis que l'hémisphère Sud se réchauffe plus lentement que la moyenne mondiale.
      """)
     st.subheader("Evolution des anomalies de températures de 1880 à 2021 selon la latitude")
     lat8=pd.read_csv('ressources/lat8.csv')

     lat8['Latitudes']=lat8['Latitudes'].replace(to_replace=['64N-90N', '44N-64N', '24N-44N', 'EQU-24N', '24S-EQU', '44S-24S',
        '64S-44S', '90S-64S'], value=['Arctic Circle (90N-64N)','Northern Tropic of Cancer (44N-64N)', 'Southern Tropic of Cancer (24N-44N)', 'Northern Equator (24N-equ)',
        'Southern Equator (equ-24S)','Northern Tropic of Capricorn (24S-44S)', 'Southern Tropic of Capricorn (44S-64S)','Antarctic Circle (64S-90S)'])
     fig=px.line(lat8,x='Year', y='Anomaly', color='Latitudes', color_discrete_sequence=['#00008b', '#4169e1', '#1e90ff','#add8e6', '#fffacd', '#ffdead', '#f4a460', '#ff8c00'], width=1000, height=500)
     fig.add_trace(go.Scatter(x=df['Year'], y=df['Glob'], name='Global Mean',
                          line=dict(color='firebrick', width=4)))

     st.plotly_chart(fig, use_container_width=False, sharing="streamlit")

     st.markdown("""
      Nous pouvons ainsi observer que les différentes zones, lorsqu’elles sont découpées en huit, impactent les anomalies. 
      On peut notamment observer de plus grandes variations lorsque nous sommes aux pôles. 

      Afin de valider ces observations graphiques, nous avons effectué un test ANOVA sur l’indépendance de la zone par rapport à l’anomalie de température (H0). 
      Le résultat obtenu nous permet ainsi de rejeter H0, validant le fait de la dépendance de la variation de l’anomalie avec les différentes zones (Tableau 2). 
      """)
     image = Image.open('ressources/ANOVA8zones.PNG')
     st.image(image, caption="Résultat de l'ANOVA entre l'anomalie de température et la variable latitudes") 

if genre=='Saisons':
     st.markdown("""
      Nous allons ensuite visualiser l'évolution de ces anomalies en fonction des mois de l'année. 
      """)
     st.subheader("Analyse des anomalies de température par mois depuis 1880")
     df_glob_month=pd.read_csv('ressources/df_glob_month.csv')
     df_glob_month2=df_glob_month.loc[df_glob_month['year']!=2022]
     fig = px.bar_polar(df_glob_month2, r="Anomaly", theta="month", color="Anomaly", animation_frame="year",animation_group="month",
                    color_continuous_scale= 'RdYlBu_r', color_continuous_midpoint=0, 
                     range_color=[df_glob_month["Anomaly"].min(), df_glob_month["Anomaly"].max()],
                    range_r=[df_glob_month["Anomaly"].min(), df_glob_month["Anomaly"].max()],
                    labels={"Anomaly": "Anomalies <br>en °C"}
                    )
     fig.update_layout(title_text="Anomalies de température mondiales de 1880 à2021 <br><sup> Période de référence : 1951-1980")
     fig.update_polars(angularaxis_dtick=1, 
                   angularaxis_exponentformat="power")
     st.plotly_chart(fig, use_container_width=False, sharing="streamlit")
 
     st.markdown("""


      Pour mieux discerner l'évolution au fil des ans, nous examinons les saisons (printemps, été, automne, hiver), plutôt que les mois. 
      """)

     st.subheader("Analyse des anomalies de température par *saison* depuis 1880")
     df_NASA=pd.read_csv('ressources/Anomalies_season.csv')
     df_NASA=df_NASA.loc[df_NASA['Year']!=2022]
     df_NASA= df_NASA.replace(to_replace='***', value=np.nan)
     df_NASA.iloc[:,3]=df_NASA.iloc[:,3].astype('float')
     df_season = df_NASA[['Year', 'Season','Anomaly']]

     fig = px.bar_polar(df_season, r="Anomaly", theta="Season", color="Anomaly", animation_frame="Year",animation_group="Season",
                    color_continuous_scale= 'RdYlBu_r', color_continuous_midpoint=0, 
                     range_color=[df_season["Anomaly"].min(), df_season["Anomaly"].max()],
                    range_r=[df_season["Anomaly"].min(), df_season["Anomaly"].max()],
                    labels={"Anomaly": "Anomalies <br>en °C"}
                    )
     fig.update_layout(title_text="Anomalies de température mondiales par saison de 1880 à2021 <br><sup> Période de référence : 1951-1980")
     fig.update_polars(angularaxis_dtick=1, 
                   angularaxis_exponentformat="power")

     st.plotly_chart(fig, use_container_width=False, sharing="streamlit")

     st.markdown("""
      Les saisons semblent évoluer de manière relativement égale, c'est-à-dire qu'il n'y a pas une seule saison qui connaît des anomalies particulièrement élevées ou faibles. 

      Cependant, ces dernières années, il est devenu plus courant que les hivers soient exceptionnellement chauds.
      Pour confirmer cette hypothèse, examinons deux tests ANOVA : 
      """)
     st.subheader("Test ANOVA sur season et anomalie : 1880-2021 (haut) et 1880-1920 (bas)")
     st.image("ressources/ANOVA_seasons_1880-2021.jpg")
     st.markdown(" ")
     st.image("ressources/ANOVA_seasons_1880-1920.jpg")

     st.markdown("""
      Ce test nous permet de conclure sur l'indépendance des saisons envers l’anomalie de température de nos jours, tandis qu’il semblerait que cela ai pu avoir un impact avant 1920. 
      Cela semble logique au vu des observations climatiques : les saisons commencent à se déplacer, nous ne pouvons plus définir l’hiver et l’été par rapport à des mois de l’année.
      """)
