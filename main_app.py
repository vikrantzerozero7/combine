import streamlit as st
import importlib.util
import sys
import re
from pathlib import Path

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>⚡ Physics | 🧪 Chemistry</h1>", unsafe_allow_html=True)

# Language selector - सिर्फ एक बार
lang = st.sidebar.radio(
    "Language / भाषा",
    ["english", "hindi"],
    format_func=lambda x: "English" if x=="english" else "हिंदी",
    key="main_lang"
)

# Function to inject language into app
def run_app_with_language(file_path, app_name, language):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Remove st.set_page_config
        code = re.sub(r'st\.set_page_config\([^)]*\)', '# removed', code)
        
        # Force set the language variable - यह सबसे important है
        # हर जगह selected_language = value को replace करो
        code = re.sub(
            r'selected_language\s*=\s*st\.sidebar\.radio\([^)]*\)',
            f'selected_language = "{language}"  # Set by main app',
            code
        )
        
        # Execute
        namespace = {'st': st, '__name__': app_name}
        exec(code, namespace)
        return True
    except Exception as e:
        st.error(f"Error in {app_name}: {e}")
        return False

# Tabs
tab1, tab2 = st.tabs(["🧪 CHEMISTRY", "⚡ PHYSICS"])

with tab1:
    if Path("app1.py").exists():
        run_app_with_language("app1.py", "chemistry", lang)
    else:
        st.error("app1.py not found")

with tab2:
    if Path("app2.py").exists():
        run_app_with_language("app2.py", "physics", lang)
    else:
        st.error("app2.py not found")
