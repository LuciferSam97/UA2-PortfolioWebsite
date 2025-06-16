import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Sam Richards")
    content = """Hi, I'm Sam and I'm a mathematician, theoretical physicist, and programmer.
    """
    st.info(content)

content2 = """Below you can find some of the apps I have built in python. Please feel free to contact me for more information!"""
st.write(content2)

col3, col4 = st.columns(2)

data_frame = pd.read_csv("data.csv", sep=";")
with col3:
    for index, row in data_frame[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in data_frame[10:].iterrows():
        st.header(row["title"])



