"""
H4X0R-OMEGA-H1ST0RY Main Application
A holographic touch-based UI for the OMEGA HACKER HISTORICAL MUSEUM
"""

import sys
import os

# Check if modules are in place
try:
    from src.main import create_app
except ImportError:
    # Attempt to recover by checking if we need to add current directory to path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if current_dir not in sys.path:
        sys.path.append(current_dir)
    
    # Try the legacy imports if we can't find the modular structure
    try:
        from src.main import create_app
    except ImportError:
        print("Error: Unable to import from the modular structure.")
        print("Falling back to the legacy monolithic architecture.")
        
        import gradio as gr
        import markdown
        import numpy as np
        import base64
        from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
        import emoji
        import re
        import random
        import io
        import os
        # Import Brazilian module
        from brazilian_module import get_br_hacker_data, get_br_template
        # Import L0pht module
        from lopht_module import get_lopht_data, get_lopht_template, get_lopht_advisory_template
        # Import Web Archive NFT Museum module
        from webarchive_nft_module import get_webarchive_nft_data, get_webarchive_nft_template, echo_lopht_members
        
        # Legacy create_ui function is used
        from legacy import create_ui

# Create the application
app = create_app() if 'create_app' in locals() else create_ui()

# Launch the app when run directly (not when imported by HF Spaces)
if __name__ == "__main__":
    app.launch() 