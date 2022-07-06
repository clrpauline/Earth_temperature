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

st.title("Bonus")
st.write("Bubble heatmap Guillaume")
st.write("Autres visualisations que vous souhaitez proposer?")


df = pd.read_csv("ressource/DFCO2_Anomaliez.csv")

from bokeh.plotting import figure, output_file, show, save
from bokeh.models.tools import HoverTool
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import LinearAxis, Range1d
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.models import Span

hover = HoverTool(
        tooltips=[
            ("CO2 émis", "@y{0.00 a}"),
            ("Année", "$x{0000}")])

line_plot = figure(plot_width=1300, plot_height=700, title="Emission de CO2 / Anomalies de température (1880-2020)",
                   x_axis_label="Year", y_axis_label="CO2")
line_plot.line(df["Année"], df["Emission_CO2"], line_width=4, legend_label="Emission de CO2",line_color="blue")
line_plot.line(df["Année"], df["Moyenne_Anomalie"], line_width=3, line_color="red", legend_label="Anomalies de température")

line_plot.extra_y_ranges = {"foo": Range1d(start=-0.3, end=1)}
line_plot.add_layout(LinearAxis(y_range_name="foo"), 'right')
line_plot.add_tools(hover)
line_plot.legend.location = "top_left"
line_plot.yaxis.axis_line_width = 3
line_plot.yaxis.axis_line_color = "blue"
hover_color = 'green'

upper = Span(dimension = 'width',   # orientation de l'asymptote
             location = 0,  # position sur l'axe des ordonnées
             line_color = 'black')   # couleur du tracé

line_plot.add_layout(upper)
line_plot.legend.click_policy = 'hide'

st.write(line_plot)
