import pandas as pd
import numpy as np
import seaborn as sns
sns.set_theme() 
import plotly.express as px
import plotly.graph_objects as go
import plotly
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Earth Temperature",
    page_icon="👋",
)
st.title("Earth Temperature: Etude du réchauffement climatique de 1880 à 2100")
