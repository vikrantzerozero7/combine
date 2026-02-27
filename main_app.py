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
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0px 20px;
        font-weight: 600;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>⚡ Physics | 🧪 Chemistry</h2>", unsafe_allow_html=True)
st.markdown("---")

# Function to run module in isolated namespace
def run_module_isolated(module_path, module_name):
    """Run module in isolated namespace"""
    try:
        # Read file
        with open(module_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove set_page_config
        import re
        content = re.sub(r'st\.set_page_config\([^)]*\)', '# removed', content)
        
        # Create unique module name
        unique_name = f"{module_name}_{id(module_path)}"
        
        # Create namespace
        namespace = {
            'st': st,
            '__name__': unique_name,
            '__file__': str(module_path)
        }
        
        # Execute in namespace
        exec(content, namespace)
        
        return True
    except Exception as e:
        st.error(f"Error loading {module_name}: {str(e)}")
        return False

# Simple fallback
def show_fallback(subject):
    st.info(f"📘 {subject} app loading...")
    if subject == "Physics":
        st.markdown("""
        ### Physics Chapters:
        - Electric Charges and Fields
        - Electrostatic Potential
        - Current Electricity
        - Moving Charges and Magnetism
        - Electromagnetic Induction
        - Alternating Current
        - Ray Optics
        - Wave Optics
        - Dual Nature of Radiation
        - Atoms and Nuclei
        - Semiconductor Electronics
        """)
    else:
        st.markdown("""
        ### Chemistry Chapters:
        - Solutions
        - Electrochemistry
        - Chemical Kinetics
        - p-block Elements
        - d and f-block Elements
        - Coordination Compounds
        - Haloalkanes and Haloarenes
        - Alcohols, Phenols and Ethers
        - Aldehydes, Ketones and Carboxylic Acids
        - Amines
        - Biomolecules
        """)

# Create 2 tabs
tab1, tab2 = st.tabs(["🧪 CHEMISTRY", "⚡ PHYSICS"])

# Chemistry Tab
with tab1:
    chem_path = Path("app1.py")
    if chem_path.exists():
        st.success("✅ Chemistry app found")
        with st.spinner("Loading Chemistry..."):
            if not run_module_isolated(chem_path, "chemistry"):
                show_fallback("Chemistry")
    else:
        st.warning("⚠️ app1.py not found")
        show_fallback("Chemistry")

# Physics Tab
with tab2:
    phys_path = Path("app2.py")
    if phys_path.exists():
        st.success("✅ Physics app found")
        with st.spinner("Loading Physics..."):
            if not run_module_isolated(phys_path, "physics"):
                show_fallback("Physics")
    else:
        st.warning("⚠️ app2.py not found")
        show_fallback("Physics")

st.markdown("---")
