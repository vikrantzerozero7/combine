import streamlit as st
import importlib.util
import sys
from pathlib import Path

# Page config - यह सबसे पहले होना चाहिए
st.set_page_config(
    page_title="Physics & Chemistry Mind Maps",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better UI
st.markdown("""
<style>
    /* Main title styling */
    .main-title {
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .main-title h1 {
        margin: 0;
        font-size: 2.5em;
    }
    .main-title p {
        margin: 5px 0 0;
        font-size: 1.2em;
        opacity: 0.9;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        padding: 10px 30px;
        font-size: 18px;
        font-weight: 600;
        border-radius: 8px;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
    }
    
    /* Subject badges */
    .subject-badge {
        display: inline-block;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
        margin: 5px;
    }
    .physics-badge {
        background: #FF9933;
        color: white;
    }
    .chemistry-badge {
        background: #0066CC;
        color: white;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Sidebar styling */
    .sidebar-info {
        background: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<div class="main-title">
    <h1>🔬 Science Mind Maps 📚</h1>
    <p>
        <span class="subject-badge physics-badge">⚡ Physics</span>
        <span class="subject-badge chemistry-badge">🧪 Chemistry</span>
    </p>
    <p>Complete Class 12 NCERT - Bilingual (English/Hindi)</p>
</div>
""", unsafe_allow_html=True)

# Function to dynamically import and run a module without set_page_config
def run_module_safe(module_path, module_name):
    """Safely run a module by capturing its output"""
    try:
        # Read the module file
        with open(module_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove any st.set_page_config calls
        import re
        modified_content = re.sub(
            r'st\.set_page_config\([^)]*\)', 
            '# st.set_page_config removed for multi-app compatibility', 
            content
        )
        
        # Create a temporary file
        temp_path = module_path.parent / f"temp_{module_name}.py"
        with open(temp_path, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        
        # Import the modified module
        spec = importlib.util.spec_from_file_location(module_name, temp_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        
        # Clean up temp file
        temp_path.unlink()
        
        return True
    except Exception as e:
        st.error(f"⚠️ Error loading {module_name}: {str(e)}")
        return False

# Create tabs
tab1, tab2, tab3 = st.tabs(["🧪 Chemistry (app1.py)", "⚡ Physics (app2.py)", "📊 Combined View"])

# Chemistry Tab
with tab1:
    st.markdown("""
    <div style='text-align: center; padding: 10px; background: #e3f2fd; border-radius: 10px; margin-bottom: 20px;'>
        <h2>🧪 Chemistry Mind Map</h2>
        <p style='color: #666;'>Physical • Inorganic • Organic Chemistry</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Check if chemistry app exists
    chem_path = Path("app1.py")
    if chem_path.exists():
        st.success("✅ Chemistry app loaded successfully!")
        with st.spinner("Loading Chemistry content..."):
            success = run_module_safe(chem_path, "chemistry_app")
            if not success:
                st.error("Failed to load Chemistry app. Showing fallback content.")
                show_chemistry_fallback()
    else:
        st.error("❌ app1.py not found in current directory!")
        show_chemistry_fallback()

# Physics Tab
with tab2:
    st.markdown("""
    <div style='text-align: center; padding: 10px; background: #fff3e0; border-radius: 10px; margin-bottom: 20px;'>
        <h2>⚡ Physics Mind Map</h2>
        <p style='color: #666;'>Electrostatics • Optics • Modern Physics</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Check if physics app exists
    phys_path = Path("app2.py")
    if phys_path.exists():
        st.success("✅ Physics app loaded successfully!")
        with st.spinner("Loading Physics content..."):
            success = run_module_safe(phys_path, "physics_app")
            if not success:
                st.error("Failed to load Physics app. Showing fallback content.")
                show_physics_fallback()
    else:
        st.error("❌ app2.py not found in current directory!")
        show_physics_fallback()

# Combined Tab
with tab3:
    st.markdown("## 📊 Complete Science Package")
    
    # Create metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Chapters", "30", "14+16")
    with col2:
        st.metric("Total Topics", "95+", "50+45")
    with col3:
        st.metric("Total Concepts", "220+", "100+120")
    with col4:
        st.metric("Languages", "2", "English/Hindi")
    
    # Subject comparison
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown("""
        <div style='background: #e3f2fd; padding: 20px; border-radius: 10px;'>
            <h3 style='color: #0066CC;'>🧪 Chemistry (app1.py)</h3>
            <ul>
                <li><b>Physical Chemistry</b>: Solutions, Electrochemistry, Kinetics</li>
                <li><b>Inorganic Chemistry</b>: p-block, d-block, f-block, Coordination</li>
                <li><b>Organic Chemistry</b>: Haloalkanes, Alcohols, Aldehydes, Carboxylic Acids</li>
                <li><b>Biomolecules</b>: Carbohydrates, Proteins, Nucleic Acids</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col_right:
        st.markdown("""
        <div style='background: #fff3e0; padding: 20px; border-radius: 10px;'>
            <h3 style='color: #FF9933;'>⚡ Physics (app2.py)</h3>
            <ul>
                <li><b>Electrostatics</b>: Charges, Fields, Potential, Capacitance</li>
                <li><b>Current Electricity</b>: Ohm's law, Circuits, Kirchhoff's laws</li>
                <li><b>Magnetism</b>: Moving charges, Matter, EMI, AC</li>
                <li><b>Optics</b>: Ray optics, Wave optics, Instruments</li>
                <li><b>Modern Physics</b>: Dual nature, Atoms, Nuclei, Semiconductors</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Features comparison
    st.markdown("---")
    st.markdown("### 🌟 Common Features")
    
    feat_cols = st.columns(3)
    features = [
        ("🌐 Bilingual", "English & Hindi support in both apps"),
        ("🖱️ Interactive", "Double-click to expand/collapse nodes"),
        ("🎨 Visual", "Color-coded mind maps for easy learning"),
        ("📱 Responsive", "Works on desktop and mobile"),
        ("📚 NCERT Based", "Complete Class 12 curriculum"),
        ("🎯 Exam Focus", "Important formulas and concepts highlighted")
    ]
    
    for i, (title, desc) in enumerate(features):
        with feat_cols[i % 3]:
            st.markdown(f"""
            <div style='background: #f8f9fa; padding: 10px; border-radius: 5px; margin: 5px;'>
                <h4>{title}</h4>
                <p style='color: #666;'>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

# Fallback functions
def show_chemistry_fallback():
    """Show chemistry content if app1.py is not available"""
    st.info("📘 Chemistry Mind Map Preview (app1.py not found)")
    
    chapters = {
        "Physical Chemistry": ["Solutions", "Electrochemistry", "Chemical Kinetics"],
        "Inorganic Chemistry": ["p-block Elements", "d and f-block Elements", "Coordination Compounds"],
        "Organic Chemistry": ["Haloalkanes", "Alcohols", "Aldehydes", "Carboxylic Acids"]
    }
    
    for category, topics in chapters.items():
        with st.expander(f"📚 {category}"):
            for topic in topics:
                st.markdown(f"• {topic}")

def show_physics_fallback():
    """Show physics content if app2.py is not available"""
    st.info("📕 Physics Mind Map Preview (app2.py not found)")
    
    chapters = {
        "Electrostatics": ["Electric Charges", "Potential", "Capacitance"],
        "Current Electricity": ["Ohm's Law", "Kirchhoff's Laws", "Circuits"],
        "Magnetism": ["Moving Charges", "Magnetism & Matter", "EMI", "AC"],
        "Optics": ["Ray Optics", "Wave Optics", "Instruments"],
        "Modern Physics": ["Dual Nature", "Atoms", "Nuclei", "Semiconductors"]
    }
    
    for category, topics in chapters.items():
        with st.expander(f"⚡ {category}"):
            for topic in topics:
                st.markdown(f"• {topic}")

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/physics.png", width=60)
    st.image("https://img.icons8.com/color/96/000000/chemistry.png", width=60)
    st.markdown("## 📋 App Info")
    
    st.markdown("""
    <div class='sidebar-info'>
        <h4>📁 Loaded Files:</h4>
    """, unsafe_allow_html=True)
    
    # Show which files are loaded
    if Path("app1.py").exists():
        st.success("✅ app1.py (Chemistry)")
    else:
        st.error("❌ app1.py not found")
    
    if Path("app2.py").exists():
        st.success("✅ app2.py (Physics)")
    else:
        st.error("❌ app2.py not found")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🎯 Quick Tips")
    st.info("""
    **How to use:**
    1. Click on tabs to switch subjects
    2. In mind maps, double-click to expand
    3. Click subject title to show/hide all
    4. Use Combined View for overview
    """)
    
    st.markdown("---")
    st.markdown("### 🔗 Quick Links")
    if st.button("🔄 Reload Chemistry"):
        st.rerun()
    if st.button("🔄 Reload Physics"):
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 📱 About")
    st.markdown("""
    **Version:** 2.0.0  
    **Subjects:** Physics + Chemistry  
    **Classes:** 11th & 12th  
    **Language:** Bilingual (EN/HI)
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>Made with ❤️ for Science Students | Complete NCERT Coverage | Bilingual Learning</p>
    <p>⚡ Physics (app2.py) + 🧪 Chemistry (app1.py) = Complete Science Package</p>
</div>
""", unsafe_allow_html=True)
