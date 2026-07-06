# Imports 
import os
import streamlit as st
from src.simulation import generate_customer_data

# data path 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data', 'raw')
os.makedirs(DATA_DIR, exist_ok=True)

data_path = os.path.join(DATA_DIR, 'simulated_data.csv')

# title for the app featuer 
st.title("Generate Dataset")
st.markdown("---")

# Listing column name to be used to generate dataset 
st.info(
    "The generated dataset includes demographic and behavioural features required for analysis."
)

with st.expander("View Dataset Features"):
    col1, col2 = st.columns(2)
    with col1:
        st.write('General Features : ')

        st.write("- ID")
        st.write("- Age")
        st.write("- Location")
        st.write("- Device")

    with col2 : 
        st.write("Behavioural Features : ")
        
        st.write("- Previous orders")
        st.write("- Sesson Duration")
        st.write("- Pages Viewed")
        st.write("- Purchased")
        st.write("- Experiment Groups")

st.markdown("---")

# user input for the total data rows 
# st.markdown("#### Set the Significance")
# alpha = st.slider(
#     label="Alpha",
#     min_value=0.00,
#     max_value=1.0,
#     value=0.05,
#     step=0.01,
# )

st.markdown(
    "### Dataset Customization"
)
st.markdown("Rows")
st.caption(
    "Total number of rows needed"
)
n_size = st.slider(
    label="Number of Customers",
    min_value=100,
    max_value=10000,
    value=200,
    step=100,
)

st.caption(
    "Controls how much the new recommendation engine changes purchase probability."
)
purchase_lift = st.slider(
    label = 'Purchase Lift (%)',
    min_value=-10.0,
    max_value=10.0,
    value=0.0,
    step=.1,
)
st.write(
    """ 
Generate a synthetic customer behavior dataset
for statistical analysis and hypothesis testing.
"""
)

if st.button("Generate Dataset"):

    df = generate_customer_data(
        n_rows=n_size,
        purchase_lift=purchase_lift
    )

    # Store for other pages
    st.session_state["dataset"] = df

    # Save to CSV
    df.to_csv(
        data_path,
        index=False
    )

    st.success("Dataset Generated Successfully!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Rows",
            len(df)
        )

    with col2:
        st.metric(
            "Purchase Lift",
            f"{purchase_lift}%"
        )

    st.dataframe(df.head())

