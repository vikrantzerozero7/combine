import streamlit as st
from pathlib import Path

st.set_page_config(layout="wide")

lang = st.sidebar.radio("Language", ["english", "hindi"])

tab1, tab2 = st.tabs(["CHEMISTRY", "PHYSICS"])

with tab1:
    with open("app1.py", "r") as f:
        code = f.read()
        code = code.replace('st.set_page_config(layout="wide")', '')
        code = f"selected_language = '{lang}'\n" + code
        exec(code)

with tab2:
    with open("app2.py", "r") as f:
        code = f.read()
        code = code.replace('st.set_page_config(layout="wide")', '')
        code = f"selected_language = '{lang}'\n" + code
        exec(code)
