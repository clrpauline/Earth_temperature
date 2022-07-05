import pandas as pd
import numpy as np
import seaborn as sns
sns.set_theme() 
import plotly.express as px
import plotly.graph_objects as go
import plotly
import streamlit as st
from streamlit_option_menu import option_menu

#création du menu sidebar:
with st.sidebar:
    selected = option_menu(menu_title="Menu", 
               options=["Introduction","Datasets de base","Autres données","Projections", "Bonus"])
    
#affichage option de menu Introduction:    
if selected == "Introduction":
        st.title("Analyse et projections du dérèglement climatique global")

    
    
    
    
#affichage option de menu Dataset de base:    
if selected == "Datasets de base":
        st.title("Datasets de base")
        dfg= dfg.astype("float")
        st.dataframe(dfg)
        
        
      
                    
                    
                    
#affichage option de menu Autres données:   
if selected == "Autres données":
        st.title("Autres données")    
        st.dataframe(dfg)
        
        
      
                    
                    
                    
#affichage option de menu Projections:           
if selected == "Projections":
        st.title("Projections")
                 
                 
                 
      
                    
                    
                    
#affichage option de menu Bonuss:                  
if selected == "Bonus":
        st.title("Bonus")

