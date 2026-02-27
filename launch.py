#!/usr/bin/env python3
"""
Launcher for Physics & Chemistry Mind Maps
Combines app1.py (Chemistry) and app2.py (Physics) in tabs
"""

import subprocess
import sys
import os
import webbrowser
from time import sleep

def check_files():
    """Check if required files exist"""
    files = {
        'app1.py': 'Chemistry App',
        'app2.py': 'Physics App',
        'main_app.py': 'Main App'
    }
    
    print("\n🔍 Checking required files...")
    print("-" * 40)
    
    all_good = True
    for file, desc in files.items():
        if os.path.exists(file):
            print(f"✅ {desc:15} found: {file}")
        else:
            print(f"❌ {desc:15} missing: {file}")
            all_good = False
    
    return all_good

def main():
    print("=" * 60)
    print("🚀 Physics & Chemistry Mind Maps Launcher")
    print("=" * 60)
    
    # Check files
    if not check_files():
        print("\n⚠️  Some files are missing!")
        print("Make sure app1.py and app2.py are in the same folder.")
        input("\nPress Enter to exit...")
        return
    
    print("\n✅ All required files found!")
    print("\n📱 Opening app in browser...")
    
    # Open browser
    sleep(2)
    webbrowser.open("http://localhost:8501")
    
    # Run streamlit
    print("\n🚀 Starting Streamlit server...")
    print("Press Ctrl+C to stop\n")
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "main_app.py"])
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down...")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
