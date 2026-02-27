import streamlit as st
import importlib.util
import sys
from pathlib import Path

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>⚡ Physics | 🧪 Chemistry</h1>", unsafe_allow_html=True)

# ============== MAIN LANGUAGE SETTING ==============
LANGUAGES = {
    "english": "English",
    "hindi": "हिंदी"
}

# Sidebar mein language selector (sirf ek baar)
with st.sidebar:
    st.title("Language Settings / भाषा सेटिंग्स")
    selected_language = st.radio(
        "Select Language / भाषा चुनें",
        options=list(LANGUAGES.keys()),
        format_func=lambda x: LANGUAGES[x],
        key="main_language_selector"
    )
    
    st.markdown("---")
    st.markdown("### Instructions / निर्देश")
    if selected_language == "english":
        st.markdown("""
        - **Click** on subject to show/hide
        - **Double-click** to expand/collapse
        """)
    else:
        st.markdown("""
        - **क्लिक करें** विषय पर दिखाने/छिपाने के लिए
        - **डबल-क्लिक करें** विस्तार/संक्षिप्त करने के लिए
        """)

# Function to modify app code with selected language
def modify_app_code(content, language):
    """Replace language selection in app code with main language"""
    import re
    
    # Find and replace language selector code
    # Pattern to find st.radio for language
    pattern = r'selected_language\s*=\s*st\.sidebar\.radio\s*\([^)]*\)'
    
    # Replace with fixed language variable
    replacement = f'selected_language = "{language}"'
    
    modified = re.sub(pattern, replacement, content)
    
    # Also remove any LANGUAGES dict if it causes issues
    modified = re.sub(r'LANGUAGES\s*=\s*\{[^}]+\}', '# LANGUAGES removed', modified)
    
    return modified

# Function to run module
def run_module_with_language(module_path, module_name, language):
    try:
        with open(module_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove any st.set_page_config
        import re
        content = re.sub(r'st\.set_page_config\([^)]*\)', '# removed', content)
        
        # Modify code to use main language
        content = modify_app_code(content, language)
        
        # Execute in namespace
        namespace = {
            'st': st,
            '__name__': module_name,
            'LANGUAGES': LANGUAGES  # Pass LANGUAGES to app
        }
        exec(content, namespace)
        
        return True
    except Exception as e:
        st.error(f"Error loading {module_name}: {str(e)}")
        return False

# Create tabs
tab1, tab2 = st.tabs(["🧪 CHEMISTRY", "⚡ PHYSICS"])

# Chemistry Tab
with tab1:
    chem_path = Path("app1.py")
    if chem_path.exists():
        with st.spinner("Loading Chemistry..."):
            if not run_module_with_language(chem_path, "chemistry_app", selected_language):
                st.info("Chemistry content loaded with fallback mode")
    else:
        st.error("app1.py not found")

# Physics Tab
with tab2:
    phys_path = Path("app2.py")
    if phys_path.exists():
        with st.spinner("Loading Physics..."):
            if not run_module_with_language(phys_path, "physics_app", selected_language):
                st.info("Physics content loaded with fallback mode")
    else:
        st.error("app2.py not found")

# Footer
st.markdown("---")
st.markdown(f"<p style='text-align: center; color: #666;'>Current Language: {LANGUAGES[selected_language]}</p>", unsafe_allow_html=True)
