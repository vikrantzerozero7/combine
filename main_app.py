import streamlit as st
import importlib.util
import sys
from pathlib import Path

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>⚡ Physics | 🧪 Chemistry</h1>", unsafe_allow_html=True)

# Function to run app
def run_app(file_path, module_name):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Remove st.set_page_config (sirf yeh remove karo)
        import re
        code = re.sub(r'st\.set_page_config\([^)]*\)', '# removed', code)
        
        # Execute
        namespace = {'st': st, '__name__': module_name}
        exec(code, namespace)
        return True
    except Exception as e:
        st.error(f"Error loading {file_path}: {e}")
        return False

# Simple tabs
tab1, tab2 = st.tabs(["🧪 CHEMISTRY", "⚡ PHYSICS"])

with tab1:
    if Path("app1.py").exists():
        run_app("app1.py", "chemistry_app")
    else:
        st.error("❌ app1.py not found")
        st.info("Please make sure app1.py is in the same folder")

with tab2:
    if Path("app2.py").exists():
        run_app("app2.py", "physics_app")
    else:
        st.error("❌ app2.py not found")
        st.info("Please make sure app2.py is in the same folder")
