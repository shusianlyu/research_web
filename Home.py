import streamlit as st

# Set webpage layout
st.set_page_config(layout="wide")

st.header("Phylogenetic Analysis of TA & TE")

st.write("Content goes in here")

st.subheader("Our team")

# Columns for company members
col1, col2, col3 = st.columns([1.5, 1.5, 1.5])

with col1:
    st.subheader("Shu Sian (Jessie) Lyu")
    st.write("Undergraduate Research Assistant")

with col2:
    st.subheader("Luc Tang")
    st.write("Undergraduate Research Assistant")
