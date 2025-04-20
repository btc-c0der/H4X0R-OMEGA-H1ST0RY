"""
H4X0R-OMEGA-H1ST0RY Main Application
A holographic touch-based UI for the OMEGA HACKER HISTORICAL MUSEUM
"""

import os
import sys
from gradio.l33t.ui import create_holographic_interface

# Import necessary modules
try:
    # Add the root directory to the path so imports work correctly
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    
    from brazilian_module import get_br_hacker_data, get_br_template
    from lopht_module import get_lopht_data, get_lopht_template, get_lopht_advisory_template
    from webarchive_nft_module import get_webarchive_nft_data, get_webarchive_nft_template, echo_lopht_members
except ImportError as e:
    print(f"Error importing modules: {e}")
    sys.exit(1)

def load_hacker_groups():
    """
    Load information about hacker groups from all sources
    
    Returns:
        dict: Combined information about all hacker groups
    """
    # Base hacker groups
    HACKER_GROUPS = {
        "MOD": {
            "name": "Masters of Deception",
            "emoji": "📞",
            "description": "Phone phreaking specialists who rivaled Legion of Doom",
            "members": ["Phiber Optik", "Acid Phreak", "Scorpion", "Corrupt"],
            "era": "Early 1990s"
        },
        "CDC": {
            "name": "Cult of the Dead Cow",
            "emoji": "🐄",
            "description": "Coined 'hacktivism' and created Back Orifice",
            "members": ["Mudge", "Dildog", "Deth Veggie", "Omega"],
            "era": "1980s-1990s"
        },
        "LOD": {
            "name": "Legion of Doom",
            "emoji": "⚡",
            "description": "Legendary group known for technical journals",
            "members": ["Erik Bloodaxe", "The Mentor", "Lex Luthor"],
            "era": "1980s-early 1990s"
        }
    }
    
    # Add Brazilian hacker groups
    br_data = get_br_hacker_data()
    for key, group in br_data["groups"].items():
        HACKER_GROUPS[key] = {
            "name": group["name"],
            "emoji": group["emoji"],
            "description": group["description"],
            "members": ["Unknown"],  # Default members if not specified
            "era": group["era"]
        }
    
    # Add L0pht with detailed information
    lopht_data = get_lopht_data()
    HACKER_GROUPS["L0PHT"] = {
        "name": lopht_data["name"],
        "emoji": lopht_data["emoji"],
        "description": "Created L0phtCrack and testified to Congress in 1998",
        "members": [member.split(" (")[0] for member in lopht_data["founders"][:5]],  # First 5 members
        "era": lopht_data["years_active"]
    }
    
    return HACKER_GROUPS

def load_data_sources():
    """
    Load all data sources for the application
    
    Returns:
        dict: Dictionary of data sources
    """
    return {
        'br_data': get_br_hacker_data(),
        'lopht_data': get_lopht_data(),
        'webarchive_data': get_webarchive_nft_data()
    }

def load_template_functions():
    """
    Load all template functions for micro-modules
    
    Returns:
        dict: Dictionary of template functions
    """
    return {
        'phreaking': load_phreaking_template,
        'bbs': load_bbs_template,
        'hacktivism': load_hacktivism_template,
        'brazil': get_br_template,
        'lopht': get_lopht_template,
        'lopht_advisory': get_lopht_advisory_template,
        'webarchive_nft': get_webarchive_nft_template
    }

def load_phreaking_template():
    """Return phone phreaking template"""
    return """# 📞 Phone Phreaking History
            
## The Blue Box Era

Phone phreaking began in the **1960s** when hackers discovered that a 2600 Hz tone could manipulate AT&T's long-distance switching systems. 

- **Blue Box** - Generated tones to make free calls
- **Red Box** - Simulated coin deposits
- **Black Box** - Manipulated voltage to receive calls for free

## Notable Phreakers
- **Cap'n Crunch** (John Draper) - Used a toy whistle from Captain Crunch cereal
- **Steve Wozniak** - Built and sold blue boxes before founding Apple"""

def load_bbs_template():
    """Return BBS template"""
    return """# 💾 Bulletin Board Systems (1980s-90s)
            
BBSes were the digital gathering places before the modern internet.

## Famous Underground BBSes
- **Black Ice Private** - Elite warez distribution
- **The Temple of the Screaming Electron** - San Francisco hub
- **TOTSE** - Text files on subjects ranging from anarchy to technology

## BBS Culture
- **FidoNet** - Worldwide network connecting thousands of BBSes
- **ANSI Art** - Vibrant digital art form born in the BBS scene
- **Warez** - Distribution of cracked software"""

def load_hacktivism_template():
    """Return hacktivism template"""
    return """# ✊ Hacktivism Origins
            
## The Birth of Digital Activism

Hacktivism combines hacking skills with political activism.

## Key Moments
- **1994**: Strano Network initiates first virtual sit-in
- **1996**: Cult of the Dead Cow coins term "hacktivism"
- **1998**: Electronic Disturbance Theater develops FloodNet

## Tactics
- **Virtual Sit-ins** - Overwhelming websites with traffic
- **Website Defacements** - Changing content to spread messages
- **Information Liberation** - Releasing classified documents"""

def create_app():
    """
    Create the main application
    
    Returns:
        gr.Blocks: The complete Gradio interface
    """
    # Load all data and components
    hacker_groups = load_hacker_groups()
    data_sources = load_data_sources()
    template_functions = load_template_functions()
    
    # Create the interface
    return create_holographic_interface(
        hacker_groups=hacker_groups,
        data_sources=data_sources,
        template_functions=template_functions,
        echo_function=echo_lopht_members
    )

# Entry point
def main():
    app = create_app()
    app.launch()

if __name__ == "__main__":
    main() 