"""
Setup script for Physics & Chemistry Mind Maps
"""

import os
import sys

def create_requirements():
    """Create requirements.txt file"""
    with open('requirements.txt', 'w') as f:
        f.write("""streamlit>=1.28.0
""")
    print("✅ Created requirements.txt")

def create_readme():
    """Create README.md file"""
    with open('README.md', 'w') as f:
        f.write("""# Physics & Chemistry Mind Maps 🔬

## 📋 Overview
This application combines two separate apps:
- **app1.py** - Chemistry Mind Map 🧪
- **app2.py** - Physics Mind Map ⚡

## 🚀 Quick Start

1. **Install dependencies:**
```bash
pip install -r requirements.txt
