import streamlit as st
import importlib.util
import sys
from pathlib import Path

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>⚡ Physics | 🧪 Chemistry</h1>", unsafe_allow_html=True)

# Language selector - SIRF EK BAAR
lang = st.sidebar.radio(
    "Language / भाषा",
    ["english", "hindi"],
    format_func=lambda x: "English" if x=="english" else "हिंदी",
    key="main_lang"
)

def run_app(file_path, app_name):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Remove st.set_page_config
        import re
        code = re.sub(r'st\.set_page_config\([^)]*\)', '', code)
        
        # Add language at the top
        code = f"selected_language = '{lang}'\n" + code
        
        # Run
        namespace = {'st': st, '__name__': app_name}
        exec(code, namespace)
        return True
    except Exception as e:
        st.error(f"Error: {e}")
        return False

tab1, tab2 = st.tabs(["🧪 CHEMISTRY", "⚡ PHYSICS"])

with tab1:
    if Path("app1.py").exists():
        run_app("app1.py", "chem")
    else:
        st.error("app1.py not found")

with tab2:
    if Path("app2.py").exists():
        run_app("app2.py", "phys")
    else:
        st.error("app2.py not found")
