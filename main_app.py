import streamlit as st
import importlib.util
import sys
import re
from pathlib import Path

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>⚡ Physics | 🧪 Chemistry</h1>", unsafe_allow_html=True)

# Function to auto-fix radio button IDs
def fix_radio_ids(content, prefix):
    """Add unique keys to all radio buttons"""
    
    # Pattern to find st.radio calls without key
    pattern = r'(st\.sidebar\.radio|st\.radio)\s*\(\s*([^,)]+)(?:,?\s*options\s*=\s*([^,)]+))?'
    
    def add_key(match):
        full_match = match.group(0)
        if 'key=' not in full_match:
            # Add unique key
            if full_match.endswith(')'):
                return full_match[:-1] + f', key="{prefix}_radio_{hash(full_match)%10000}")'
        return full_match
    
    modified = re.sub(pattern, add_key, content, flags=re.DOTALL)
    return modified

# Function to run module
def run_module_safe(module_path, module_name, prefix):
    try:
        with open(module_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove set_page_config
        content = re.sub(r'st\.set_page_config\([^)]*\)', '# removed', content)
        
        # Fix radio button IDs
        content = fix_radio_ids(content, prefix)
        
        # Execute in namespace
        namespace = {'st': st, '__name__': f"{module_name}_{prefix}"}
        exec(content, namespace)
        
        return True
    except Exception as e:
        st.error(f"Error loading {module_name}: {str(e)}")
        return False

# Simple fallback
def show_fallback(subject):
    st.info(f"Loading {subject}...")

# Create tabs
tab1, tab2 = st.tabs(["🧪 CHEMISTRY", "⚡ PHYSICS"])

with tab1:
    chem_path = Path("app1.py")
    if chem_path.exists():
        with st.spinner("Loading Chemistry..."):
            if not run_module_safe(chem_path, "chemistry", "chem"):
                show_fallback("Chemistry")
    else:
        st.error("app1.py not found")

with tab2:
    phys_path = Path("app2.py")
    if phys_path.exists():
        with st.spinner("Loading Physics..."):
            if not run_module_safe(phys_path, "physics", "phys"):
                show_fallback("Physics")
    else:
        st.error("app2.py not found")
