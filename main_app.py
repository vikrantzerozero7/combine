import streamlit as st
from pathlib import Path

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>⚡ Physics | 🧪 Chemistry</h1>", unsafe_allow_html=True)

# Language selector - sirf ek baar
lang = st.sidebar.radio(
    "Language / भाषा",
    ["english", "hindi"],
    key="main_lang"
)

st.sidebar.markdown("---")
if lang == "english":
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

def run_app(file_path):
    """Run app with language injection"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Remove st.set_page_config
        code = code.replace('st.set_page_config(layout="wide")', '# removed')
        
        # CRITICAL: Force set the language variable
        # Find and replace the language selector line
        import re
        pattern = r'selected_language\s*=\s*st\.sidebar\.radio\([^)]*\)'
        code = re.sub(pattern, f'selected_language = "{lang}"', code)
        
        # Execute
        exec(code)
        return True
    except Exception as e:
        st.error(f"Error: {e}")
        return False

# Tabs
tab1, tab2 = st.tabs(["🧪 CHEMISTRY", "⚡ PHYSICS"])

with tab1:
    st.markdown("### 🧪 Chemistry")
    if Path("app1.py").exists():
        run_app("app1.py")
    else:
        st.error("app1.py not found")

with tab2:
    st.markdown("### ⚡ Physics")
    if Path("app2.py").exists():
        run_app("app2.py")
    else:
        st.error("app2.py not found")
