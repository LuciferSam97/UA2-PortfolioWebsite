import streamlit as st
from sending_emails import send_mail

st.header("Contact Me")

with st.form(key='email_form'):
    user_email = st.text_input("Enter your Email Address")
    message = st.text_area("Enter Your Message")
    button = st.form_submit_button("Send")

    if button:
        send_mail(receiver=user_email, body=message, subject=f"Website enquiry from {user_email}.")
        st.info("Your email has been sent!")