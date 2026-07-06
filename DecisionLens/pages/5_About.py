
import streamlit as st

st.title("🚀 Version 2.0 Release Notes")
st.caption("Customer Behaviour Simulation Enhancement")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Version", "2.0")

with col2:
    st.metric("Release", "July 2026")

with col3:
    st.metric("Author", "Pranav Dhadwal")

st.markdown("---")

st.header("📖 Overview")

st.info("""
Version 2 introduces a more realistic customer behaviour simulation by replacing
independent random variables with meaningful behavioural relationships.

The objective is to generate synthetic e-commerce data that closely resembles
real customer interactions while preserving the integrity of the A/B testing experiment.
""")

st.header("✨ What's New")

st.success("""
### 👤 Customer Profile

- Added Gender
- Added Country
- Added Traffic Source

These additions improve customer diversity and support richer exploratory analysis.
""")

st.success("""
### 🔗 Behavioural Relationships

The following relationships are now simulated:

• Country → Traffic Source

• Country → Device

• Age → Session Duration

• Gender → Session Duration

• Device → Session Duration

• Session Duration → Pages Viewed

• Gender → Pages Viewed

• Previous Orders → Purchase Probability

• Experiment Group → Purchase Probability
""")

st.success("""
### 📈 Improved Data Quality

• Reduced completely random feature generation.

• Introduced realistic behavioural dependencies.

• Preserved natural variability to avoid overly deterministic patterns.
""")

st.success("""
### 📊 Analytics Improvements

The updated simulation now provides stronger support for:

• Exploratory Data Analysis

• Customer Segmentation

• Interactive Visualizations

• Feature Engineering

• Statistical Hypothesis Testing

• Business Recommendation Generation
""")

st.markdown("---")

st.subheader("🎯 Objective")

st.warning("""
The goal of Version 2 is **not** to generate perfect synthetic data.

Instead, it aims to simulate **plausible customer behaviour** by combining
realistic relationships with natural randomness, producing a dataset that is
more suitable for business analysis and hypothesis testing.
""")

st.markdown("---")

st.caption("Version 2.0 • Developed by Pranav Dhadwal")
