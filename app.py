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

# Hacker group database for reference
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
    "L0PHT": {
        "name": "L0pht Heavy Industries",
        "emoji": "🔨",
        "description": "Created L0phtCrack and testified to Congress",
        "members": ["Mudge", "Space Rogue", "Weld Pond", "Kingpin"],
        "era": "Late 1990s"
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

# Update L0PHT with more detailed information from our module
lopht_data = get_lopht_data()
HACKER_GROUPS["L0PHT"] = {
    "name": lopht_data["name"],
    "emoji": lopht_data["emoji"],
    "description": "Created L0phtCrack and testified to Congress in 1998",
    "members": [member.split(" (")[0] for member in lopht_data["founders"][:5]],  # First 5 members
    "era": lopht_data["years_active"]
}

# Hacker lingo transformation function
def hackerize_text(text):
    replacements = {
        'a': '4', 'e': '3', 'i': '1', 'o': '0', 
        't': '7', 's': '5', 'A': '4', 'E': '3', 
        'I': '1', 'O': '0', 'T': '7', 'S': '5',
        'ck': 'x', 'CK': 'X'
    }
    
    for char, replacement in replacements.items():
        # Randomly replace about 70% of occurrences for more authentic look
        if random.random() < 0.7:
            text = text.replace(char, replacement)
    
    return text

# Matrix effect generation
def generate_matrix_background(width=800, height=400):
    # Create a black background
    image = Image.new('RGBA', (width, height), color=(0, 0, 0, 255))
    draw = ImageDraw.Draw(image)
    
    # Add matrix-like falling characters
    characters = "01ブラックハットネオハッカー"
    green_shades = [(0, min(255, int(40 + i*20)), 0) for i in range(10)]
    
    for x in range(0, width, 20):
        length = random.randint(5, height // 15)
        y_offset = random.randint(0, height)
        
        for y in range(length):
            actual_y = (y_offset + y * 20) % height
            opacity = int(255 * (1 - y / length))
            color = random.choice(green_shades)
            color_with_opacity = (color[0], color[1], color[2], opacity)
            
            char = random.choice(characters)
            draw.text((x, actual_y), char, fill=color_with_opacity)
    
    # Apply a slight blur for the "glow" effect
    image = image.filter(ImageFilter.GaussianBlur(radius=1))
    return image

# Manuscript generation function
def create_hacker_manuscript(markdown_text, group_theme=None):
    # Convert markdown to HTML
    html_content = markdown.markdown(markdown_text)
    
    # Remove HTML tags to get plain text for image creation
    plain_text = re.sub('<.*?>', '', html_content)
    
    # Hackerize the text
    hacker_text = hackerize_text(plain_text)
    
    # Generate background with matrix effect
    width, height = 800, len(hacker_text.split('\n')) * 25 + 200
    height = max(height, 400)  # Minimum height
    
    # Create base image with matrix effect
    background = generate_matrix_background(width, height)
    draw = ImageDraw.Draw(background)
    
    # Add group-specific theming if selected
    group_banner = ""
    if group_theme and group_theme in HACKER_GROUPS:
        group = HACKER_GROUPS[group_theme]
        group_banner = f"{group['emoji']} {group['name']} | {group['era']} | {group['emoji']}"
        
        # Draw group banner
        draw.rectangle([(0, 0), (width, 40)], fill=(0, 30, 0, 230))
        draw.text((10, 10), group_banner, fill=(0, 255, 0))
    
    # Add content with retro hacker styling
    y_position = 60
    lines = hacker_text.split('\n')
    
    for line in lines:
        if line.strip() == "":
            y_position += 20
            continue
            
        # Add hackerspeak symbols as line decorators
        prefix = random.choice(["[+] ", ">>> ", "## ", "/*", "$> ", "h4x: "])
        decorated_line = prefix + line
        
        # Draw text with green terminal-like glow
        draw.text((20, y_position), decorated_line, fill=(0, 255, 0))
        y_position += 25
    
    # Draw footer
    footer_y = height - 30
    draw.rectangle([(0, footer_y), (width, height)], fill=(0, 30, 0, 230))
    draw.text((10, footer_y + 5), "0M3G4 H4X0R H1ST0R1C4L MU53UM // N30-M4TR1X", fill=(0, 255, 0))
    
    # Convert to bytes for Gradio
    img_byte_arr = io.BytesIO()
    background.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    # Return both the styled HTML and the image
    return html_content, img_byte_arr.getvalue()

# Define emoji-based UI components
def create_ui():
    # Load custom CSS
    css = ""
    css_path = os.path.join(os.path.dirname(__file__), "holo_style.css")
    if os.path.exists(css_path):
        with open(css_path, "r") as f:
            css = f.read()
    
    with gr.Blocks(theme=gr.themes.Glass(), css=css) as demo:
        gr.Markdown(
            """<h1 class="holo-title">0M3G4 H4X0R H1ST0R1C4L MU53UM</h1>
            <p class="title">H0L0 T0UCH B453D M4TR1X N30 1NT3RF4C3</p>""", 
            elem_id="title-md"
        )
        
        with gr.Row(elem_classes=["holographic"]):
            with gr.Column(scale=1):
                gr.Markdown("### <span class='emoji-icon'>🔐</span> S3L3CT H4X0R GR0UP")
                group_selector = gr.Dropdown(
                    choices=["None"] + list(HACKER_GROUPS.keys()),
                    value="None",
                    label="Hacker Collective Theme",
                    elem_classes=["holo-input"]
                )
                
                gr.Markdown("### <span class='emoji-icon'>🌐</span> M1CR0-M0DUL3S")
                with gr.Row():
                    btn_phreaking = gr.Button("📞 PHR34K1NG", elem_classes=["holographic-btn"])
                    btn_bbs = gr.Button("💾 BBS", elem_classes=["holographic-btn"])
                    btn_hacktivism = gr.Button("✊ H4CKT1V1SM", elem_classes=["holographic-btn"])
                
                # Add Brazilian module button
                with gr.Row():
                    btn_brazil = gr.Button("🇧🇷 BR4Z1L13N H4X", elem_classes=["holographic-btn"])
                    btn_lopht = gr.Button("🔐 L0PHT", elem_classes=["holographic-btn"])
                
                with gr.Row():
                    btn_webarchive = gr.Button("🏛️ W3B 4RCH1V3 NFT", elem_classes=["holographic-btn"])
                    btn_lopht_advisory = gr.Button("⚠️ L0PHT 4DV150RY", elem_classes=["holographic-btn"])
                
                group_info = gr.Markdown(elem_classes=["matrix-bg"])
                
                # Echo L0pht members button (ceremonial)
                btn_echo_members = gr.Button("📣 3CH0 L0PHT M3MB3R5", elem_classes=["holographic-btn", "echo-btn"])
                echo_output = gr.Markdown(elem_classes=["echo-output"])
            
            with gr.Column(scale=2):
                gr.Markdown("### <span class='emoji-icon'>📝</span> 3NT3R M4RKDOWN T3XT", elem_classes=["matrix-bg"])
                markdown_input = gr.Textbox(
                    lines=10,
                    placeholder="Enter your markdown text here...",
                    label="Input Markdown",
                    elem_classes=["holo-input"]
                )
                convert_btn = gr.Button("🔄 C0NV3RT T0 H4X0R M4NU5CR1PT", variant="primary", elem_classes=["holographic-btn"])
            
        with gr.Row(elem_classes=["holographic"]):
            with gr.Tab("📜 Manuscript", elem_classes=["holo-tab"]):
                html_output = gr.HTML(label="Formatted Output")
            with gr.Tab("🖼️ H0L0 1M4G3", elem_classes=["holo-tab"]):
                image_output = gr.Image(label="Manuscript Image")
            with gr.Tab("🧩 BR H4X D4T4", elem_classes=["holo-tab"]):
                br_incidents = gr.DataFrame(
                    value=[
                        [incident["year"], incident["name"], incident["description"]]
                        for incident in br_data["incidents"]
                    ],
                    headers=["Year", "Operation", "Description"],
                    label="Brazilian Hacker Incidents"
                )
            
            with gr.Tab("🕰️ L0PHT H15T0RY", elem_classes=["holo-tab"]):
                # L0pht key achievements table
                lopht_achievements = gr.DataFrame(
                    value=[
                        [achievement["year"], achievement["name"], achievement["description"]]
                        for achievement in lopht_data["achievements"]
                    ],
                    headers=["Year", "Achievement", "Description"],
                    label="L0pht Heavy Industries Milestones"
                )
                
            with gr.Tab("🏛️ NFT MU53UM", elem_classes=["holo-tab"]):
                webarchive_data = get_webarchive_nft_data()
                nft_collections = gr.DataFrame(
                    value=[
                        [collection["name"], 
                         collection.get("items", "N/A"), 
                         collection.get("nft_contract", "N/A"), 
                         collection.get("preservation_rating", "B")]
                        for collection in webarchive_data["collections"]
                    ],
                    headers=["Collection", "Items", "NFT Contract", "Preservation Rating"],
                    label="Quantum-Preserved NFT Collections (Target Year: 2420)"
                )
        
        # Function to show group info when selected
        def update_group_info(group_key):
            if group_key == "None" or group_key not in HACKER_GROUPS:
                return "Select a hacking collective to see details"
            
            group = HACKER_GROUPS[group_key]
            info = f"""### <span class='emoji-icon'>{group['emoji']}</span> {group['name']} ({group_key})
            
**Era:** {group['era']}
**Focus:** {group['description']}
**Key Members:** {', '.join(group['members'])}
            """
            return info
        
        # Template text functions for micro-modules
        def load_phreaking_template():
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
        
        # Get template from Brazilian module
        def load_brazil_template():
            return get_br_template()
        
        # Get template from L0pht module
        def load_lopht_template():
            return get_lopht_template()
        
        # Get template from L0pht Advisory module
        def load_lopht_advisory_template():
            return get_lopht_advisory_template()
        
        # Get template from Web Archive NFT Museum module
        def load_webarchive_nft_template():
            return get_webarchive_nft_template()
        
        # Echo L0pht members function
        def acknowledge_lopht_members():
            return echo_lopht_members()
        
        # Connect UI components
        group_selector.change(
            update_group_info, 
            inputs=[group_selector], 
            outputs=[group_info]
        )
        
        convert_btn.click(
            create_hacker_manuscript,
            inputs=[markdown_input, group_selector],
            outputs=[html_output, image_output]
        )
        
        btn_phreaking.click(
            lambda: load_phreaking_template(),
            outputs=[markdown_input]
        )
        
        btn_bbs.click(
            lambda: load_bbs_template(),
            outputs=[markdown_input]
        )
        
        btn_hacktivism.click(
            lambda: load_hacktivism_template(),
            outputs=[markdown_input]
        )
        
        # Add Brazilian module button functionality
        btn_brazil.click(
            lambda: load_brazil_template(),
            outputs=[markdown_input]
        )
        
        # Add L0pht module button functionality
        btn_lopht.click(
            lambda: load_lopht_template(),
            outputs=[markdown_input]
        )
        
        # Add L0pht Advisory button functionality
        btn_lopht_advisory.click(
            lambda: load_lopht_advisory_template(),
            outputs=[markdown_input]
        )
        
        # Add Web Archive NFT Museum button functionality
        btn_webarchive.click(
            lambda: load_webarchive_nft_template(),
            outputs=[markdown_input]
        )
        
        # Add Echo L0pht Members button functionality
        btn_echo_members.click(
            lambda: acknowledge_lopht_members(),
            outputs=[echo_output]
        )
    
    return demo

# Create and launch the UI
app = create_ui()

# Only launch when running directly, not when imported by HF Spaces
if __name__ == "__main__":
    app.launch() 