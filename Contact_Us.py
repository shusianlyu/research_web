import streamlit as st
from send_email import send_email

st.header("Contact form")

with st.form(key="contact_form"):
    user_email = st.text_input("Your Email Address")
    row_message = st.text_area("Text")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{row_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        if not user_email or not row_message:
            st.info("Please complete the form!")
        else:
            send_email(message)
            st.info("Your email is sent successfully!")
