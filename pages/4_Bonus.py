import pandas as pd
import numpy as np
import seaborn as sns
sns.set_theme() 
import plotly.express as px
import plotly.graph_objects as go
import plotly
import streamlit as st

st.set_page_config(
    page_title="Bonus",
    page_icon="🌍",
)

st.title("Une visualisation graphique qui fait chaud dans le dos😰")

df_country=pd.read_csv('ressources/df_country.csv')
df_country.head()
y=[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460]
y=np.sort(y)[::-1]
x=[5,15,25,35,45,55,65,75,85,95,105,115,125,135,145,155,165,175]

df_country['Country Name'].unique()
df_country['x']=0
df_country['y']=0

uniques=df_country['Country Name'].unique()

f=0
j=0
for i in uniques:
  if f< 19:
       df_country.loc[df_country['Country Name']==i, 'x']=x[j]
       df_country.loc[df_country['Country Name']==i, 'y']=y[f]
       f+=1
  else :
       df_country.loc[df_country['Country Name']==i, 'x']=x[j]
       df_country.loc[df_country['Country Name']==i, 'y']=y[f]
       f=0
       j+=1
df_country.head()




df_country['abs Anomalies']=df_country['Anomalies'].apply('abs')
df_country.head()
df_country2=df_country.drop('Country Code',axis=1)
df_country2=df_country2.fillna(0)

fig = px.scatter(df_country2,x="x", y="y", size="abs Anomalies", color="Anomalies",color_continuous_scale='RdYlBu_r',
                hover_name="Country Name",animation_frame="year", animation_group='Country Name', size_max=60, text='Country Name',
                range_color=[df_country2["Anomalies"].min(), df_country2["Anomalies"].max()], color_continuous_midpoint=0, width=800, height=1200)

fig.update_xaxes(visible=False)
fig.update_yaxes(visible=False)

st.plotly_chart(fig, use_container_width=False, sharing="streamlit")

