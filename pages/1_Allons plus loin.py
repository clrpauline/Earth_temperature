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


st.dataframe("df_country_kaggle.csv")
