import os
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📈 Exploratory Data Analysis")

st.markdown("---")

data_path = os.path.join('./', 'data', 'raw', 'simulated_data.csv' )

if "dataset" in st.session_state:
    data = st.session_state["dataset"]
else:
    data = pd.read_csv(data_path)

st.markdown("#### Data Overview")
st.dataframe(data.head(5))

col1, col2 = st.columns(2)

with col1:
    st.metric(label='Rows', value=data.shape[0])

with col2:
    st.metric(label='Columns', value=data.shape[1])

col1, col2 = st.columns(2)

with col1:
    st.metric(label='Missing Values', value=data.isna().sum().sum())

with col2:
    st.metric(label='Duplicated Values', value=data.duplicated().sum())


with st.expander("Check Columns"):
    data_type_summary = {
        'Column Name' : list(),
        'Data Type' : list()
    }

    for col_name, data_type in data.dtypes.items():
        data_type_summary['Column Name'].append(col_name.replace("_", " ").title())
        data_type_summary['Data Type'].append(data_type)

    st.dataframe(data_type_summary)

with st.expander("Statistic Summary"):

    num_cols = data.select_dtypes(include='number').columns.drop(['customer_id', 'purchase_prob'])

    statistic_summary = []
    for col in num_cols:
        statistic_summary.append({
            "Column": col,
            "Average": data[col].mean(),
            "Max": data[col].max(),
            "Min": data[col].min(),
            "Std": data[col].std()
        })

    st.dataframe(statistic_summary)

def cat_summary(df, col):

    value_counts = df[col].value_counts()

    ratio = (df[col].value_counts(normalize=True).mul(100).round(2))

    summary_df = pd.DataFrame({"Count": value_counts,"Ratio (%)": ratio}).reset_index()

    summary_df.columns = [col.replace("_", " ").title(),"Count","Ratio (%)"]

    return {
        "Mode": df[col].mode().iloc[0],"Unique Values": df[col].nunique(),"Summary": summary_df
    }

with st.expander("Categorical Summary"):

    for col in data.select_dtypes(include="object"):

        st.markdown(f"#### {col.replace('_', ' ').title()}")

        summary = cat_summary(data, col)

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Mode", summary["Mode"])

        with col2:
            st.metric("Unique Values", summary["Unique Values"])

        st.dataframe(summary["Summary"])

st.markdown("---")
