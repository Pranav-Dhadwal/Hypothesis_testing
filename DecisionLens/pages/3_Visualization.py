import os
import pandas as pd
import streamlit as st
from src.visualization import *

st.title("📊 Interactive Visualization")

st.markdown("---")
path = os.path.join("./","data","raw","simulated_data.csv")

if "dataset" in st.session_state:
    data = st.session_state["dataset"]
else:
    data = pd.read_csv(path)

numeric_cols = data.select_dtypes(include="number").drop(columns='customer_id').columns.tolist()
categorical_cols = data.select_dtypes(include="object").columns.tolist()

left, right = st.columns([1,2])

with left:
    chart = st.selectbox(
        "Visualization Type",
        ["Bar Chart","Pie Chart","Histogram","Box Plot","Scatter Plot","Line Plot"]
    )
    if chart=="Bar Chart":
        c = st.selectbox("Categorical Feature", categorical_cols)
    elif chart=="Pie Chart":
        c = st.selectbox("Categorical Feature", categorical_cols)
    elif chart=="Histogram":
        c = st.selectbox("Numerical Feature", numeric_cols)
        bins = st.slider("Bins",5,50,20)
    elif chart=="Box Plot":
        x = st.selectbox("Categorical Feature", categorical_cols)
        y = st.selectbox("Numerical Feature", numeric_cols)
    elif chart=="Scatter Plot":
        x = st.selectbox("X-axis", numeric_cols)
        y = st.selectbox("Y-axis", numeric_cols, index=min(1,len(numeric_cols)-1))
        hue = st.selectbox("Color (Optional)", ["None"]+categorical_cols)
    elif chart=="Line Plot":
        x = st.selectbox("X-axis", numeric_cols)
        y = st.selectbox("Y-axis", numeric_cols, index=min(1,len(numeric_cols)-1))

with right:
    if chart=="Bar Chart":
        plot_bar(data,c)
    elif chart=="Pie Chart":
        plot_pie(data,c)
    elif chart=="Histogram":
        plot_histogram(data,c,bins)
    elif chart=="Box Plot":
        plot_boxplot(data,x,y)
    elif chart=="Scatter Plot":
        plot_scatter(data,x,y,None if hue=="None" else hue)
    elif chart=="Line Plot":
        plot_line(data,x,y)

st.info("""
Use the controls on the left to explore the dataset.
Different chart types automatically expose compatible features.
""")
