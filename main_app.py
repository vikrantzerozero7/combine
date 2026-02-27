import streamlit as st
from pathlib import Path

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>⚡ Physics | 🧪 Chemistry</h1>", unsafe_allow_html=True)

lang = st.sidebar.radio("Language", ["english", "hindi"])

tab1, tab2 = st.tabs(["CHEMISTRY", "PHYSICS"])

with tab1:
    if Path("app1.py").exists():
        with open("app1.py", "r", encoding='utf-8') as f:
            code = f.read()
            # Remove set_page_config
            code = code.replace('st.set_page_config(layout="wide")', '')
            # Force language
            code = f"selected_language = '{lang}'\n" + code
            exec(code)
    else:
        st.error("app1.py not found")

with tab2:
    if Path("app2.py").exists():
        with open("app2.py", "r", encoding='utf-8') as f:
            code = f.read()
            code = code.replace('st.set_page_config(layout="wide")', '')
            code = f"selected_language = '{lang}'\n" + code
            exec(code)
    else:
        st.error("app2.py not found")
