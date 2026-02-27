import streamlit as st
import re
from pathlib import Path

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>⚡ Physics | 🧪 Chemistry</h1>", unsafe_allow_html=True)

# Main language selector
main_lang = st.sidebar.radio(
    "Language / भाषा",
    ["english", "hindi"],
    format_func=lambda x: "English" if x=="english" else "हिंदी",
    key="main_language"
)

# Instructions in selected language
st.sidebar.markdown("---")
if main_lang == "english":
    st.sidebar.markdown("""
    ### Instructions:
    - Click on subject to show/hide
    - Double-click to expand/collapse
    """)
else:
    st.sidebar.markdown("""
    ### निर्देश:
    - विषय पर क्लिक करें दिखाने/छिपाने के लिए
    - डबल-क्लिक करें विस्तार/संक्षिप्त करने के लिए
    """)

def run_app_with_language(file_path, main_language):
    """Run app with main language injected"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Remove st.set_page_config
        code = re.sub(r'st\.set_page_config\([^)]*\)', '# removed', code)
        
        # IMPORTANT: Force set selected_language to main_language
        # यह line सबसे important है - यह app ke language selector ko override karega
        code = re.sub(
            r'selected_language\s*=\s*st\.sidebar\.radio\([^)]*\)',
            f'selected_language = "{main_language}"  # Set by main app',
            code
        )
        
        # Also ensure LANGUAGES is available
        if 'LANGUAGES' not in code:
            LANGUAGES_STR = """LANGUAGES = {
    "english": "English",
    "hindi": "हिंदी"
}"""
            code = LANGUAGES_STR + "\n\n" + code
        
        # Execute
        exec(code)
        return True
    except Exception as e:
        st.error(f"Error loading {file_path}: {e}")
        return False

# Tabs
tab1, tab2 = st.tabs(["🧪 CHEMISTRY", "⚡ PHYSICS"])

with tab1:
    st.markdown("### 🧪 Chemistry")
    if Path("app1.py").exists():
        run_app_with_language("app1.py", main_lang)
    else:
        st.error("app1.py not found")

with tab2:
    st.markdown("### ⚡ Physics")
    if Path("app2.py").exists():
        run_app_with_language("app2.py", main_lang)
    else:
        st.error("app2.py not found")
