import streamlit as st

# Set webpage layout
st.set_page_config(layout="wide")

# Add header to the page
st.header("Phylogenetic Analysis of TA & TE")

# Todo: add content & description
st.subheader("Objectives")
objectives = "Build phylogenies based on IMG (project ID 503441) " \
             "genome contigs identified previously as containing TAs & " \
             "TEs and derive biological conclusion on it."
st.write(objectives)

# Add introduction of the team
st.subheader("Our team")

# Columns for team members
col1, col2, col3 = st.columns([1.5, 1.5, 1.5])

with col1:
    st.subheader("Shu Sian (Jessie) Lyu")
    st.write("Undergraduate Research Assistant")
    # Todo: contact detail or image

with col2:
    st.subheader("Luc Tang")
    st.write("Undergraduate Research Assistant")
    # Todo: contact detail or image
