import streamlit as st
from sending_emails import send_mail

st.title("Contact Me")
st.header("Send me an email using the form below!")

with st.form(key='email_form'):
    user_email = st.text_input("Enter your Email Address")
    subject = st.text_input("Enter your Subject (optional)", max_chars=50)
    message = st.text_area("Enter Your Message")
    button = st.form_submit_button("Send")

    if button:
        if user_email is None:
            st.error("Please enter your email address")
        elif message is None:
            st.error("Please enter your message")
        else:
            send_mail(sender=user_email, body=message, subject=f"Website enquiry: {subject}.")
            st.info("Your email has been sent!")

st.write("Or simply email me at spm.richards97@gmail.com")