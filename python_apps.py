import streamlit as st
import pandas as pd
from cards import display_app

def slide_session_reset():
    if "slide_count" not in st.session_state:
        st.session_state["slide_count"] = 0
    elif st.session_state["slide_count"] != 0:
        st.session_state["slide_count"] = 0


def view_options_reset():
    if "view_option" not in st.session_state:
        pass
    elif st.session_state["view_option"] == "Slideshow":
        st.session_state["view_option"] = "All"


def udemy_apps(udemy_key : str):
    st.header("Udemy Course Python Apps")

    with open("static/PythonApps.txt", "r") as f:
        content = f.read()
    st.markdown(content)
    st.page_link(page="contact_me.py", label="Please feel free to contact me for more information!")

    cols = st.columns((0.5, 2, 0.5))
    with cols[1].container(horizontal_alignment="center", vertical_alignment="center"):
        view_options = st.pills("", options=["All", "Slideshow"], default="All", key=udemy_key)

    if view_options == "All":
        slide_session_reset()
        col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
        data_frame = pd.read_csv("static/new_data.csv", sep=";")
        with col3.container(horizontal_alignment="center"):
            for index, row in data_frame[:10].iterrows():
                st.header(row["app_title"])
                st.write(row["description"])
                st.image(row["image"])
                st.link_button(label="Source Code", url=f"{row['git_url']}", icon=":material/folder_code:")

        with col4.container(horizontal_alignment="center"):
            for index, row in data_frame[10:].iterrows():
                st.header(row["app_title"])
                st.write(row["description"])
                st.image(row["image"])
                st.link_button(label="Source Code", url=f"{row['git_url']}", icon=":material/folder_code:")

    elif view_options == "Slideshow":
        if "slide_count" not in st.session_state:
            st.session_state["slide_count"]: int = 0

        cols = st.columns(3)
        with st.container():
            with cols[0].container(vertical_alignment="top", horizontal_alignment="center", height="stretch"):
                left_button = st.button(":material/arrow_back_ios:", width=70, key=f"{udemy_key}_lb")
            with cols[2].container(vertical_alignment="top", horizontal_alignment="center", height="stretch"):
                right_button = st.button(":material/arrow_forward_ios:", width=70, key=f"{udemy_key}_rb")
            if left_button:
                st.session_state["slide_count"] -= 1
            if right_button:
                st.session_state["slide_count"] += 1
            with cols[1].container(border=10, vertical_alignment="center", horizontal_alignment="center"):
                display_app(st.session_state["slide_count"])


def personal_apps():
    st.header("Personal Python Projects")

    with open("static/PersonalApps.txt", "r") as file:
        content1 = file.read()
    st.markdown(content1)


st.title("Python Apps")

page_view = [":material/list: All", ":material/school: Udemy Course Apps", ":material/terminal: Personal Projects"]

select_view = st.segmented_control(label="", options=page_view, default=":material/list: All",
                                   selection_mode="single", on_change=view_options_reset)
st.divider()

if select_view == ":material/list: All":
    udemy_apps("view_option")
    st.divider()
    personal_apps()

elif select_view == ":material/school: Udemy Course Apps":
    udemy_apps("view_option")

elif select_view == ":material/terminal: Personal Projects":
    personal_apps()

elif select_view is None:
    st.write("Oops! Please select a view option to see my apps!")
