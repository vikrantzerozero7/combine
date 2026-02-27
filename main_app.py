import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Class 12 Science Hub",
    page_icon="🔬",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .stButton > button {
        width: 100%;
        height: 60px;
        font-size: 20px !important;
        font-weight: bold;
        border-radius: 10px;
        margin: 10px 0px;
    }
    .title {
        text-align: center;
        padding: 20px;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        color: white;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
    <div class="title">
        <h1>📚 Class 12 Science Hub</h1>
        <p>Physics & Chemistry Resources</p>
    </div>
""", unsafe_allow_html=True)

# Create two columns for buttons
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔭 Physics")
    if st.button("📖 Open Physics Resources", key="physics_btn"):
        js = "window.open('https://physics12-uziqxcq849ehzfrxye8z6m.streamlit.app')"
        html = f'<script>{js}</script>'
        st.components.v1.html(html, height=0)
        st.success("✅ Physics link opened in new tab!")

with col2:
    st.markdown("### 🧪 Chemistry")
    if st.button("⚗️ Open Chemistry Resources", key="chemistry_btn"):
        js = "window.open('https://chemistry12-z3ghemmaa6fb8nympw8mzo.streamlit.app')"
        html = f'<script>{js}</script>'
        st.components.v1.html(html, height=0)
        st.success("✅ Chemistry link opened in new tab!")

# Footer
st.markdown("---")
st.markdown("### 🎯 Click any button to open resources in new tab")
st.markdown("#### 📝 Note: Links will open in new browser tab")
