#!/usr/bin/env python3
"""
H4X0R-OMEGA-H1ST0RY Launcher
A holographic touch-based UI for the OMEGA HACKER HISTORICAL MUSEUM
"""

import os
import sys
import time

def print_ascii_art():
    """Print ASCII art logo with Matrix-like animation."""
    art = """
      ██   ██  █████  ██   ██  ██████  ██████  
      ██   ██ ██   ██  ██ ██  ██    ██ ██   ██ 
      ███████ ███████   ███   ██    ██ ██████  
      ██   ██ ██   ██  ██ ██  ██    ██ ██   ██ 
      ██   ██ ██   ██ ██   ██  ██████  ██   ██ 
    ================================================
     ██████  ███    ███ ███████  ██████   █████  
    ██    ██ ████  ████ ██      ██       ██   ██ 
    ██    ██ ██ ████ ██ █████   ██   ███ ███████ 
    ██    ██ ██  ██  ██ ██      ██    ██ ██   ██ 
     ██████  ██      ██ ███████  ██████  ██   ██ 
    ================================================
                H1ST0R1C4L MU53UM
    """
    
    for line in art.split('\n'):
        # Print each character with a delay for Matrix effect
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.001)
        print()
    
    print("\n[+] 1N1T14L1Z1NG H0L0GR4PH1C 1NT3RF4C3...\n")
    time.sleep(0.5)

def check_requirements():
    """Check if all requirements are installed."""
    try:
        import gradio
        import markdown
        import numpy
        import PIL
        import emoji
        return True
    except ImportError as e:
        print(f"[!] Missing dependency: {e}")
        print("[!] Please run: pip install -r requirements.txt")
        return False

def main():
    """Main launcher function."""
    print_ascii_art()
    
    if not check_requirements():
        sys.exit(1)
    
    print("[+] Dependencies loaded successfully")
    time.sleep(0.3)
    print("[+] Initializing holographic interface")
    time.sleep(0.3)
    print("[+] Activating n3o matrix visualization")
    time.sleep(0.3)
    
    try:
        from app import create_ui
        app = create_ui()
        print("\n[+] H0L0GR4PH1C 1NT3RF4C3 R34DY!\n")
        print("[+] Access your local interface at: http://localhost:7860")
        app.launch()
    except Exception as e:
        print(f"[!] Error launching application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 