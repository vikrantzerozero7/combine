import streamlit as st
import importlib.util
import sys
from pathlib import Path

# Page config
st.set_page_config(
    page_title="Physics & Chemistry",
    page_icon="🔬",
    layout="wide"
)

# Simple custom CSS
st.markdown("""
<style>
    /* Clean tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0px 20px;
        font-weight: 600;
    }
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    /* Simple header */
    .app-header {
        text-align: center;
        padding: 10px;
        margin-bottom: 10px;
        border-bottom: 2px solid #eee;
    }
</style>
""", unsafe_allow_html=True)

# Simple header
st.markdown("<h2 style='text-align: center;'>⚡ Physics | 🧪 Chemistry</h2>", unsafe_allow_html=True)
st.markdown("---")

# Function to safely run modules
def run_module_safe(module_path, module_name):
    """Run a module after removing set_page_config"""
    try:
        with open(module_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove st.set_page_config
        import re
        modified_content = re.sub(
            r'st\.set_page_config\([^)]*\)', 
            '# removed', 
            content
        )
        
        # Create temp file
        temp_path = module_path.parent / f"temp_{module_name}.py"
        with open(temp_path, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        
        # Import
        spec = importlib.util.spec_from_file_location(module_name, temp_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        
        # Clean up
        temp_path.unlink()
        return True
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return False

# Simple fallback
def show_fallback(subject):
    st.info(f"📘 {subject} content will appear here")
    st.write("Please ensure the app file is in the same directory.")

# Create just 2 tabs
tab1, tab2 = st.tabs(["🧪 CHEMISTRY", "⚡ PHYSICS"])

# Chemistry Tab
with tab1:
    chem_path = Path("app1.py")
    if chem_path.exists():
        with st.spinner("Loading Chemistry..."):
            if not run_module_safe(chem_path, "chemistry_app"):
                show_fallback("Chemistry")
    else:
        show_fallback("Chemistry")

# Physics Tab
with tab2:
    phys_path = Path("app2.py")
    if phys_path.exists():
        with st.spinner("Loading Physics..."):
            if not run_module_safe(phys_path, "physics_app"):
                show_fallback("Physics")
    else:
        show_fallback("Physics")

# Simple footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #666; font-size: 12px;'>⚡ Physics | 🧪 Chemistry</p>", unsafe_allow_html=True)
