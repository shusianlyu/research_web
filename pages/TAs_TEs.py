import streamlit as st
import pandas as pd

# Set webpage layout
st.set_page_config(layout="wide")
# Add header
st.header("TA and TE files")
# option files
TA_options = ["TA.fas", "TA.nwk", "TA_renamed.fas", "TA_renamed.nwk",
              "cog_stats", "pfam_stats"]
TE_options = ["TE.fas", "TE.nwk", "TE_renamed.fas", "TE_renamed.nwk",
              "cog_stats", "pfam_stats"]

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

            details = "A tree represented file of TA's sequences produced " \
                      "from MEGA-X"
            st.subheader("Details")
            st.write(details)
            """tree_file = f"files/column1.nwk"
            t = Tree(tree_file)
            st.write(t)"""
        case "TA_renamed.fas":
            details = "It was produced by converting TA sequence " \
                      "names with matching names from TA to " \
                      "TE based on TASmania_tncentral_blast_output.tsv file"
            example = """
            \>Ga0308418_1000051\n
            MASPELEVLGITTVAGNVSVEKTSRNARQICELAGCPQMAVYAGCPRPLLRPLQTAEEVHGKSG
            IDGANLPEPQMPLGSLHAVQYLIETLMAAQEPVTLALLGPMTNLAVALVQQPRIVERIRRLVFM
            GGSAFEGNTTPAAEFNIFTDPHAAQIVLSAGIPEVVMLGLNVTQQVLSTPERIERIRALGTRVG
            QTVADMLAFYGKFDIRRYGLPGGPLHDPCVVAYLLQPQLFELKPCYVEVETASPLNLGRTVVDR
            WGLSGRPANVQVAFGVDAEEFYRLLTERLGRYR
            """
            st.subheader("Details")
            st.write(details)
            st.write(example)
        case "TA_renamed.nwk":
            details = "A tree represented file of renamed TA sequences " \
                      "produced from MEGA-X"
            st.subheader("Details")
            st.write(details)
        case "cog_stats":
            details = "Count each distinct COG per cluster v.s. overall " \
                      "clusters (Cut tree at level 3 to get one cluster)."
            st.subheader("Details")
            st.write(details)
            df = pd.read_csv("files/cog_stats_column1_full_name.csv",
                             sep="\t")
            st.dataframe(df)
        case "pfam_stats":
            details = "Count each distinct pfam per cluster v.s. overall " \
                      "clusters (Cut tree at level 3 to get one cluster)."
            st.subheader("Details")
            st.write(details)
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
            details = "A tree represented file of TE's sequences produced " \
                      "from MEGA-X"
            st.subheader("Details")
            st.write(details)
        case "cog_stats":
            details = "Count each distinct COG per cluster v.s. overall " \
                      "clusters (Cut tree at level 3 to get one cluster)."
            st.subheader("Details")
            st.write(details)
            df = pd.read_csv("files/pruned_column2_COG_stats.csv",
                             sep="\t")
            st.dataframe(df)
        case "pfam_stats":
            details = "Count each distinct pfam per cluster v.s. overall " \
                      "clusters (Cut tree at level 3 to get one cluster)."
            st.subheader("Details")
            st.write(details)
            df = pd.read_csv("files/pruned_column2_pfam_stats.csv",
                             sep="\t")
            st.dataframe(df)
        case "TE_renamed.fas":
            details = "It was produced by converting TE sequence " \
                      "names with matching names from TE to " \
                      "TA based on TASmania_tncentral_blast_output.tsv file"
            example = """
                    \>Ga0308414_10302791\n
                    ACGGTGTGCACGTGAGGGGAGGTGCGGCGGGATAGCACCATGTGCTCGGCGATGCG
                    CTGCCGCATGATGGACATGGGTTCGCGCAACTCGTCCCCCTCGAAGGGCCGCGACG
                    GTCCCATGGTCGCCCCGGTGGCGTAGGTGGGCGGGGTGGAGGCGGCAGGCGCCGCC
                    GGCCGGGAGGGCCGAGGCGCTGGCCTGGGAGTGGGGGTCACCGGGGGCGGAGCCGC
                    CGCTGCAGGAGGCGCGGCGGGGGCGGCTTGCGCC...
                    """
            st.subheader("Details")
            st.write(details)
            st.write(example)
        case "TE_renamed.nwk":
            details = "A tree represented file of renamed TE sequences " \
                      "produced from MEGA-X"
            st.subheader("Details")
            st.write(details)



