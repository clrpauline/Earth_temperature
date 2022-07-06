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

C1, C2 = st. columns(2)


fig = px.choropleth(df26, locations="Country", color=" ",range_color=[0,200],
                  color_discrete_sequence=["green","orange","red"],
                    title="Invivabilité des pays avec le scénario RCP 2.6",
                    locationmode='country names',color_continuous_midpoint=0)
st.plotly_chart(fig)
