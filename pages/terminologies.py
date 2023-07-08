import streamlit as st

st.header("Useful terminologies")

options = ["Toxin-Antitoxin (TA)", "Transposable Elements (TE)",
           "Mobile elements", "Contig"]
term = st.selectbox("Select term to get its definition", options=options)

match term:
    case "Toxin-Antitoxin (TA)":
        st.subheader("Definition")
        st.write("TA systems present in bacteria and archaea are known to "
                 "regulate cell growth in response to environmental stresses.")
    case "Transposable Elements (TE)":
        st.subheader("Definition")
        st.write("DNA sequences that have the ability to change "
                 "their position within a genome.")
    case "Mobile elements":
        st.subheader("Definition")
        st.write("DNA sequences that can move around the genome, changing "
                 "their number of copies or simply changing their location, "
                 "often affecting the activity of nearby genes. They include"
                 " DNA transposable elements, plasmids and "
                 "bacteriophage elements.")
    case "Contig":
        st.subheader("Definition")
        st.write("A set of DNA segments or sequences that overlap in a way "
                 "that provides a contiguous representation of a "
                 "genomic region")

