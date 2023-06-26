import streamlit as st
import pandas as pd

# Set webpage layout
st.set_page_config(layout="wide")
# Add header
st.header("TA and TE files")
# option files
TA_options = ["TA.fas", "TA.nwk", "cog_stats", "pfam_stats"]
TE_options = ["TE.fas", "TE.nwk", "cog_stats", "pfam_stats"]

# Add columns
column1, empty, column2 = st.columns([5, 0.5, 5])

with column1:
    # drop down menu
    TA_file = st.selectbox("Select a TA file", options=TA_options)
    # Add details and graph of each file
    match TA_file:
        case "TA.fas":
            details = "A file that contains TA (Toxin-Antitoxin) name " \
                      "with actual sequences."
            example = """
            \>Ga0393409_004_36_905\n
            MASPELEVLGITTVAGNVSVEKTSRNARQICELAGCPQMAVYAGCPRPLLRPLQTAEEVHGKSG
            IDGANLPEPQMPLGSLHAVQYLIETLMAAQEPVTLALLGPMTNLAVALVQQPRIVERIRRLVFM
            GGSAFEGNTTPAAEFNIFTDPHAAQIVLSAGIPEVVMLGLNVTQQVLSTPERIERIRALGTRVG
            QTVADMLAFYGKFDIRRYGLPGGPLHDPCVVAYLLQPQLFELKPCYVEVETASPLNLGRTVVDR
            WGLSGRPANVQVAFGVDAEEFYRLLTERLGRYR
            """
            st.subheader("Details")
            st.write(details)
            st.write(example)
        case "TA.nwk":
            # Get tree string
            with open("files/column1.nwk") as file:
                tree = file.readline()
            tree = tree[:-1]

            details = "A tree represented file of TA's sequences"
            st.subheader("Details")
            st.write(details)
            """tree_file = f"files/column1.nwk"
            t = Tree(tree_file)
            st.write(t)"""
        case "cog_stats":
            df = pd.read_csv("files/cog_stats_column1_full_name.csv",
                             sep="\t")
            st.dataframe(df)
        case "pfam_stats":
            df = pd.read_csv("files/pfam_stats_column1_full_name.csv",
                     sep="\t")
            st.dataframe(df)

with column2:
    # drop down menu
    TE_file = st.selectbox("Select a TA file", options=TE_options)
    # Add details and graph of each file
    match TE_file:
        case "TE.fas":
            details = "A file that contains TE (Transposable Elements) name " \
                      "with actual sequences."
            example = """
            \>Ga0308414_1000287\n
            ACGGTGTGCACGTGAGGGGAGGTGCGGCGGGATAGCACCATGTGCTCGGCGATGCGCTGCCGCA
            TGATGGACATGGGTTCGCGCAACTCGTCCCCCTCGAAGGGCCGCGACGGTCCCATGGTCGCCCC
            GGTGGCGTAGGTGGGCGGGGTGGAGGCGGCAGGCGCCGCCGGCCGGGAGGGCCGAGGCGCTGGC
            CTGGGAGTGGGGGTCACCGGGGGCGGAGCCGCCGCTGCAGGAGGCGCGGCGGGGGCGGCTTGCG
            CCTCCCTCCTCGCCACGAAGGCGAGG...
            """
            st.subheader("Details")
            st.write(details)
            st.write(example)
        case "TE.nwk":
            details = "A tree represented file of TE's sequences"
            st.subheader("Details")
            st.write(details)
        case "cog_stats":
            pass
        case "pfam_stats":
            pass

"""    st.subheader("Tree comparison")
    st.image("images/tree_comparison.png")"""


