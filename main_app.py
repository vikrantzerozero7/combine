import streamlit as st
import importlib.util
import sys
import re
from pathlib import Path

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>⚡ Physics | 🧪 Chemistry</h1>", unsafe_allow_html=True)

# ============================================
# MAIN LANGUAGE CONTROLLER
# ============================================
LANGUAGES = {
    "english": "English",
    "hindi": "हिंदी"
}

# Single language selector in sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    main_language = st.radio(
        "Language / भाषा",
        options=["english", "hindi"],
        format_func=lambda x: "English" if x == "english" else "हिंदी",
        key="main_language",
        index=0
    )
    st.markdown("---")
    st.markdown("### 📖 Instructions")
    if main_language == "english":
        st.markdown("""
        • Click on subject to show/hide
        • Double-click to expand/collapse
        • Select language above
        """)
    else:
        st.markdown("""
        • विषय पर क्लिक करें दिखाने/छिपाने के लिए
        • डबल-क्लिक करें विस्तार/संक्षिप्त करने के लिए
        • ऊपर भाषा चुनें
        """)

# ============================================
# FUNCTION TO SAFELY RUN APPS
# ============================================
def run_app_safe(file_path, module_name, language):
    """Run app with language injection"""
    try:
        # Read file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove any st.set_page_config
        content = re.sub(r'st\.set_page_config\([^)]*\)', '# removed', content)
        
        # Remove sidebar language selector and replace with our language
        # Pattern 1: st.sidebar.radio with language
        pattern1 = r'selected_language\s*=\s*st\.sidebar\.radio\s*\([^)]*\)'
        content = re.sub(pattern1, f'selected_language = "{language}"', content)
        
        # Pattern 2: st.radio in sidebar
        pattern2 = r'st\.sidebar\.radio\s*\([^)]*,\s*key\s*=\s*"[^"]*"\s*\)'
        content = re.sub(pattern2, '', content)
        
        # Pattern 3: Any other radio
        pattern3 = r'st\.radio\s*\([^)]*\)'
        content = re.sub(pattern3, '', content)
        
        # Add language variable at top
        modified_content = f"""# Language set by main app
selected_language = "{language}"
LANGUAGES = {LANGUAGES}

""" + content
        
        # Create unique module name
        unique_name = f"{module_name}_{id(file_path)}"
        
        # Create namespace
        namespace = {
            'st': st,
            '__name__': unique_name,
            '__file__': str(file_path)
        }
        
        # Execute
        exec(modified_content, namespace)
        return True
        
    except Exception as e:
        st.error(f"⚠️ Error in {module_name}: {str(e)}")
        # Show fallback content
        if "physics" in module_name:
            show_physics_fallback(language)
        else:
            show_chemistry_fallback(language)
        return False

# ============================================
# FALLBACK CONTENT
# ============================================
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

def show_physics_fallback(language):
    if language == "english":
        st.info("📘 Physics Mind Map")
        st.markdown("""
        ### Chapters:
        • Electric Charges & Fields
        • Electrostatic Potential
        • Current Electricity
        • Moving Charges & Magnetism
        • Magnetism & Matter
        • Electromagnetic Induction
        • Alternating Current
        • Electromagnetic Waves
        • Ray Optics
        • Wave Optics
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
        • चुंबकत्व एवं द्रव्य
        • वैद्युतचुंबकीय प्रेरण
        • प्रत्यावर्ती धारा
        • वैद्युतचुंबकीय तरंगें
        • किरण प्रकाशिकी
        • तरंग प्रकाशिकी
        • विकिरण की द्वैत प्रकृति
        • परमाणु एवं नाभिक
        • अर्धचालक इलेक्ट्रॉनिकी
        """)

# ============================================
# MAIN TABS
# ============================================
tab1, tab2 = st.tabs(["🧪 CHEMISTRY", "⚡ PHYSICS"])

with tab1:
    st.markdown("### 🧪 Chemistry")
    chem_path = Path("app1.py")
    if chem_path.exists():
        run_app_safe(chem_path, "chemistry", main_language)
    else:
        st.error("❌ app1.py not found")
        show_chemistry_fallback(main_language)

with tab2:
    st.markdown("### ⚡ Physics")
    phys_path = Path("app2.py")
    if phys_path.exists():
        run_app_safe(phys_path, "physics", main_language)
    else:
        st.error("❌ app2.py not found")
        show_physics_fallback(main_language)

# ============================================
# FOOTER
# ============================================
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col2:
    current_lang = "English" if main_language == "english" else "हिंदी"
    st.markdown(f"<p style='text-align: center; color: #666;'>🌐 Language: {current_lang}</p>", unsafe_allow_html=True)
