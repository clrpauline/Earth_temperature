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
