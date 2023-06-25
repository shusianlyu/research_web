import streamlit as st
from send_email import send_email


# Set webpage layout
st.set_page_config(layout="wide")
st.header("Contact form")

with st.form(key="contact_form"):
    # Get the user email
    user_email = st.text_input("Your Email Address")
    # Get the message
    row_message = st.text_area("Text")
    # Reformat the message
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{row_message}
"""
    # Add button
    button = st.form_submit_button("Submit")
    # Add response
    if button:
        # Make sure user completes the form
        if not user_email or not row_message:
            st.info("Please complete the form!")
        else:
            send_email(message)
            st.info("Your email is sent successfully!")
