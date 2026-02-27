import streamlit as st
import importlib.util
import sys
import re
from pathlib import Path

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>⚡ Physics | 🧪 Chemistry</h1>", unsafe_allow_html=True)

# ============================================
# LANGUAGE CONFIGURATION
# ============================================
LANGUAGES = {
    "english": "English",
    "hindi": "हिंदी"
}

# ============================================
# SIDEBAR LANGUAGE SELECTOR (SINGLE)
# ============================================
with st.sidebar:
    st.title("⚙️ Settings")
    selected_language = st.radio(
        "Language / भाषा",
        options=["english", "hindi"],
        format_func=lambda x: "English" if x == "english" else "हिंदी",
        key="global_language",
        index=0
    )
    st.markdown("---")
    st.markdown("### 📖 Instructions")
    if selected_language == "english":
        st.markdown("""
        • Click on subject to show/hide
        • Double-click to expand/collapse
        """)
    else:
        st.markdown("""
        • विषय पर क्लिक करें दिखाने/छिपाने के लिए
        • डबल-क्लिक करें विस्तार/संक्षिप्त करने के लिए
        """)

# ============================================
# FUNCTION TO RUN APP WITH LANGUAGE INJECTION
# ============================================
def run_app_with_language(file_path, app_name, language):
    """Run app with language injection"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove st.set_page_config
        content = re.sub(r'st\.set_page_config\([^)]*\)', '# removed', content)
        
        # Remove any existing language selector in sidebar
        content = re.sub(
            r'selected_language\s*=\s*st\.sidebar\.radio\([^)]*\)',
            f'selected_language = "{language}"  # Set by main app',
            content
        )
        
        # Also remove any other radio buttons that might cause conflicts
        content = re.sub(
            r'st\.sidebar\.radio\([^)]*\)',
            '# sidebar radio removed',
            content
        )
        
        # Make sure LANGUAGES dict is available
        if 'LANGUAGES' not in content:
            # Add LANGUAGES at the top
            content = f"LANGUAGES = {LANGUAGES}\n\n" + content
        
        # Create unique module name
        module_name = f"{app_name}_{language}"
        
        # Create namespace with all necessary variables
        namespace = {
            'st': st,
            '__name__': module_name,
            'LANGUAGES': LANGUAGES,
            'selected_language': language  # Inject directly
        }
        
        # Execute
        exec(content, namespace)
        return True
        
    except Exception as e:
        st.error(f"Error loading {app_name}: {str(e)}")
        return False

# ============================================
# FALLBACK CONTENT
# ============================================
def show_physics_fallback(language):
    if language == "english":
        st.info("📘 Physics Mind Map")
        st.markdown("""
        ### Chapters:
        • Electric Charges & Fields
        • Electrostatic Potential
        • Current Electricity
        • Moving Charges & Magnetism
        • Electromagnetic Induction
        • Alternating Current
        • Ray Optics & Wave Optics
        • Dual Nature of Radiation
        • Atoms & Nuclei
        • Semiconductor Electronics
        """)
    else:
        st.info("📘 भौतिक विज्ञान माइंड मैप")
        st.markdown("""
        ### अध्याय:
        • वैद्युत आवेश तथा क्षेत्र
        • स्थिरवैद्युत विभव
        • विद्युत धारा
        • गतिमान आवेश और चुंबकत्व
        • वैद्युतचुंबकीय प्रेरण
        • प्रत्यावर्ती धारा
        • किरण प्रकाशिकी एवं तरंग प्रकाशिकी
        • विकिरण की द्वैत प्रकृति
        • परमाणु एवं नाभिक
        • अर्धचालक इलेक्ट्रॉनिकी
        """)

def show_chemistry_fallback(language):
    if language == "english":
        st.info("📘 Chemistry Mind Map")
        st.markdown("""
        ### Chapters:
        • Solutions
        • Electrochemistry
        • Chemical Kinetics
        • d & f Block Elements
        • Coordination Compounds
        • Haloalkanes & Haloarenes
        • Alcohols, Phenols & Ethers
        • Aldehydes, Ketones & Acids
        • Amines
        • Biomolecules
        """)
    else:
        st.info("📘 रसायन विज्ञान माइंड मैप")
        st.markdown("""
        ### अध्याय:
        • विलयन
        • वैद्युत रसायन
        • रासायनिक बलगतिकी
        • d एवं f ब्लॉक तत्व
        • उपसहसंयोजन यौगिक
        • हैलोऐल्केन एवं हैलोऐरीन
        • एल्कोहॉल, फिनॉल एवं ईथर
        • एल्डिहाइड, कीटोन एवं अम्ल
        • एमीन
        • जैव-अणु
        """)

# ============================================
# MAIN TABS
# ============================================
tab1, tab2 = st.tabs(["🧪 CHEMISTRY", "⚡ PHYSICS"])

with tab1:
    st.markdown("### 🧪 Chemistry")
    chem_path = Path("app1.py")
    if chem_path.exists():
        with st.spinner("Loading Chemistry..."):
            if not run_app_with_language(chem_path, "chemistry", selected_language):
                show_chemistry_fallback(selected_language)
    else:
        st.error("app1.py not found")
        show_chemistry_fallback(selected_language)

with tab2:
    st.markdown("### ⚡ Physics")
    phys_path = Path("app2.py")
    if phys_path.exists():
        with st.spinner("Loading Physics..."):
            if not run_app_with_language(phys_path, "physics", selected_language):
                show_physics_fallback(selected_language)
    else:
        st.error("app2.py not found")
        show_physics_fallback(selected_language)

# ============================================
# FOOTER
# ============================================
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col2:
    current_lang = "English" if selected_language == "english" else "हिंदी"
    st.markdown(f"<p style='text-align: center; color: #666;'>🌐 Language: {current_lang}</p>", unsafe_allow_html=True)
