import os
import streamlit as st
from src.hypothesis_testing import *

# Data file import 
path = os.path.join("./","data","raw","simulated_data.csv")

if "dataset" in st.session_state:
    data = st.session_state["dataset"]
else:
    data = pd.read_csv(path)

# UI
st.title("🧪 Hypothesis Testing")

# Defining Problem 
st.subheader("Business Problem")
st.info(
    """
    Determine whether the new recommendation strategy
    (Experiment Group B) significantly improves customer
    purchase probability compared to the existing strategy.
    """
)

# Assuming Hypothesis
col1, col2 = st.columns(2)

with col1:
    st.success(
    """
    ### Null Hypothesis (H₀)

    There is no significant difference
    between Group A and Group B.
    """
    )
with col2:
    st.warning(
    """
    ### Alternative Hypothesis (H₁)

    Group B has a significantly higher
    purchase probability than Group A.
    """
    )


# Sumamry of data to display 
summary = get_group_summary(data)

st.subheader("Group Summary")

st.dataframe(summary)

# Performing ttest 
st.subheader("Independent Two Sample T-Test")
t_stat, p_value = perform_ttest(data)

# Displaying result
col1, col2, col3 = st.columns(3)

col1.metric(
    "T Statistic",
    round(t_stat,3)
)

col2.metric(
    "P Value",
    round(p_value,5)
)

col3.metric(
    "Alpha",
    0.05
)

# Business Decision 
decision = hypothesis_result(p_value)
if decision["Result"]:

    st.success(
        f"Decision: {decision['Decision']}"
    )

else:

    st.error(
        f"Decision: {decision['Decision']}"
    )

st.subheader("Business Recommendation")

st.info(
    business_conclusion(
        decision["Result"]
    )
)