import streamlit as st
import pandas as pd
from streamlit import session_state


def display_app(index : int):
    df = pd.read_csv("static/new_data.csv", sep=";")

    i = index % len(df)
    st.header(df.loc[df.index == i]["app_title"].squeeze())
    st.write(df.loc[df.index == i]["description"].squeeze())
    st.image(df.loc[df.index == i]["image"].squeeze())
    st.link_button(label="Source Code", url=f"{df.loc[df.index == i]['git_url'].squeeze()}", icon=":material/folder_code:")
#   st.write(f"[Source Code]({df.loc[df.index == i]['git_url'].squeeze()})")
