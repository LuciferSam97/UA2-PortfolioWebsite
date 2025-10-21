import streamlit as st
import pandas as pd
from cards import display_app

st.title("Python Apps")
st.divider()

st.header("Udemy Python Course Apps")

content = """Below you can find the apps I built in python as part of Ardit Sulce's [Python Mega-Course](https://www.udemy.com/course/the-python-mega-course/). Please feel free to contact me for more information!"""
st.markdown(content)

cols = st.columns((0.5, 2, 0.5))
with cols[1].container(horizontal_alignment="center", vertical_alignment="center"):
    view_options = st.pills("", options=["All", "Slideshow", "Categorised"], default="All")

if view_options == "All":
    col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
    data_frame = pd.read_csv("static/new_data.csv", sep=";")
    with col3:
        for index, row in data_frame[:10].iterrows():
            st.header(row["app_title"])
            st.write(row["description"])
            st.image(row["image"])
            st.link_button(label="Source Code", url=f"{row['git_url']}", icon=":material/folder_code:")

    with col4:
        for index, row in data_frame[10:].iterrows():
            st.header(row["app_title"])
            st.write(row["description"])
            st.image(row["image"])
            st.link_button(label="Source Code", url=f"{row['git_url']}", icon=":material/folder_code:")
elif view_options == "Slideshow":

    if "slide_count" not in st.session_state:
        st.session_state["slide_count"] : int = 0

    cols = st.columns(3)
    with st.container():
        with cols[0].container(vertical_alignment="top", horizontal_alignment="center", height="stretch"):
            left_button = st.button(":material/arrow_back_ios:", width=70)
        with cols[2].container(vertical_alignment="top", horizontal_alignment="center", height="stretch"):
            right_button = st.button(":material/arrow_forward_ios:", width=70)
        if left_button:
            st.session_state["slide_count"] -= 1
        if right_button:
            st.session_state["slide_count"] += 1
        with cols[1].container(border=10, vertical_alignment="center", horizontal_alignment="center"):
            display_app(st.session_state["slide_count"])

elif view_options == "Categorised":
    pass
