import streamlit as st

pages = [
    st.Page(
        page="home.py",
        title="Home",
        icon=":material/home:",
    ),
    st.Page(
        page="python_apps.py",
        title="Python Apps",
        icon=":material/apps:",
    ),
    st.Page(
        page="documents.py",
        title="Documents",
        icon=":material/description:",
    ),
    st.Page(
        page="contact_me.py",
        title="Contact Me",
        icon=":material/mail:",
    )
]

page = st.navigation(pages)
page.run()