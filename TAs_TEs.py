import streamlit as st


# Add header
st.header("TA and TE files")
# option files
options = ["TA.fas", "TA.nwk", "TE.fas", "TE.nwk"]

# drop down menu
file = st.selectbox("Select a file", options=options)

match file:
    case "TA.fas":
        details = ""
    case "TA.nwk":
        details = ""
    case "TE.fas":
        details = ""
    case "TE.fas":
        details = ""

st.write(details)
