import streamlit as st

st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_icon="static/icons/house-user.ico")

st.title(body="Sam Richards", width="stretch")

st.divider()

cols = st.columns((0.2, 2, 0.2, 2, 0.2))

with cols[1].container(horizontal_alignment="center", vertical_alignment="center"):
    st.image("images/photo.png", caption="Me on the day of my graduation from Cambridge", use_container_width=True)

with cols[3].container(horizontal_alignment="center", vertical_alignment="center", border=10):
    st.header("About me")
    with open("static/AboutMe.txt", "r") as f:
        content = f.read()
    st.markdown(content)
