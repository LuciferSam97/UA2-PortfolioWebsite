import streamlit as st
from sending_emails import send_mail

st.title("Contact Me")
st.divider()

st.header("Send me an email using the form below!")

with st.form(key='email_form', clear_on_submit=True):
    user_email = st.text_input(label="Enter your Email Address", key='user_email')
    subject = st.text_input(label="Enter a Subject (optional)", max_chars=50, key='subject')
    message = st.text_area(label="Enter Your Message", key='message')
    button = st.form_submit_button("Send")

    if button:
        if user_email is None:
            st.error("Please enter an email address I can use to respond to you!")
        elif message is None:
            st.error("Please enter your message.")
        else:
            if send_mail(sender=user_email, body=message, subject=f"Website enquiry: {subject}."):
                st.info("Your email has been sent!")
                st.markdown(f"""Your message:  \n
                {user_email}  \n
                Subject: {subject}  \n
                Message: {message}
                """)
            else:
                st.error("Sorry, something went wrong. Please try emailing me directly at spm.richards97@gmail.com.")

st.write("You can also email me directly at spm.richards97@gmail.com or "
         "contact me on [LinkedIn](https://www.linkedin.com/in/sam-richards-mathphys/).")