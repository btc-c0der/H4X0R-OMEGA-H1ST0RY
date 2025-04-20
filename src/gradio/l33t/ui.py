"""
H4X0R-OMEGA-H1ST0RY Gradio UI components
Provides the holographic interface elements and interactions
"""

import gradio as gr
import os
from .manuscript import create_hacker_manuscript

def load_holo_styles():
    """
    Load custom CSS for holographic interface
    
    Returns:
        str: CSS code for the holographic interface
    """
    css = ""
    css_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "holo_style.css")
    if os.path.exists(css_path):
        with open(css_path, "r") as f:
            css = f.read()
    return css

def create_tabs(data_sources):
    """
    Create tab components for the UI
    
    Args:
        data_sources (dict): Data for populating tabs
        
    Returns:
        list: List of Gradio tab components
    """
    tabs = []
    
    # Manuscript tab
    with gr.Tab("📜 Manuscript", elem_classes=["holo-tab"]) as tab_manuscript:
        html_output = gr.HTML(label="Formatted Output")
        tabs.append((tab_manuscript, html_output))
    
    # Holographic image tab
    with gr.Tab("🖼️ H0L0 1M4G3", elem_classes=["holo-tab"]) as tab_image:
        image_output = gr.Image(label="Manuscript Image")
        tabs.append((tab_image, image_output))
    
    # Add other tabs if data is available
    if 'br_data' in data_sources and 'incidents' in data_sources['br_data']:
        with gr.Tab("🧩 BR H4X D4T4", elem_classes=["holo-tab"]) as tab_br:
            br_incidents = gr.DataFrame(
                value=[
                    [incident["year"], incident["name"], incident["description"]]
                    for incident in data_sources['br_data']["incidents"]
                ],
                headers=["Year", "Operation", "Description"],
                label="Brazilian Hacker Incidents"
            )
            tabs.append((tab_br, br_incidents))
    
    # L0pht history tab
    if 'lopht_data' in data_sources and 'achievements' in data_sources['lopht_data']:
        with gr.Tab("🕰️ L0PHT H15T0RY", elem_classes=["holo-tab"]) as tab_lopht:
            lopht_achievements = gr.DataFrame(
                value=[
                    [achievement["year"], achievement["name"], achievement["description"]]
                    for achievement in data_sources['lopht_data']["achievements"]
                ],
                headers=["Year", "Achievement", "Description"],
                label="L0pht Heavy Industries Milestones"
            )
            tabs.append((tab_lopht, lopht_achievements))
    
    # NFT Museum tab
    if 'webarchive_data' in data_sources and 'collections' in data_sources['webarchive_data']:
        with gr.Tab("🏛️ NFT MU53UM", elem_classes=["holo-tab"]) as tab_nft:
            nft_collections = gr.DataFrame(
                value=[
                    [collection["name"], 
                     collection.get("items", "N/A"), 
                     collection.get("nft_contract", "N/A"), 
                     collection.get("preservation_rating", "B")]
                    for collection in data_sources['webarchive_data']["collections"]
                ],
                headers=["Collection", "Items", "NFT Contract", "Preservation Rating"],
                label="Quantum-Preserved NFT Collections (Target Year: 2420)"
            )
            tabs.append((tab_nft, nft_collections))
    
    return tabs

def create_micro_module_buttons(template_functions):
    """
    Create buttons for the micro-modules
    
    Args:
        template_functions (dict): Dictionary of button names and their callback functions
        
    Returns:
        dict: Dictionary of button components
    """
    buttons = {}
    
    # First row of buttons
    with gr.Row():
        if 'phreaking' in template_functions:
            btn_phreaking = gr.Button("📞 PHR34K1NG", elem_classes=["holographic-btn"])
            buttons['phreaking'] = btn_phreaking
            
        if 'bbs' in template_functions:
            btn_bbs = gr.Button("💾 BBS", elem_classes=["holographic-btn"])
            buttons['bbs'] = btn_bbs
            
        if 'hacktivism' in template_functions:
            btn_hacktivism = gr.Button("✊ H4CKT1V1SM", elem_classes=["holographic-btn"])
            buttons['hacktivism'] = btn_hacktivism
    
    # Second row of buttons
    with gr.Row():
        if 'brazil' in template_functions:
            btn_brazil = gr.Button("🇧🇷 BR4Z1L13N H4X", elem_classes=["holographic-btn"])
            buttons['brazil'] = btn_brazil
            
        if 'lopht' in template_functions:
            btn_lopht = gr.Button("🔐 L0PHT", elem_classes=["holographic-btn"])
            buttons['lopht'] = btn_lopht
    
    # Third row of buttons
    with gr.Row():
        if 'webarchive_nft' in template_functions:
            btn_webarchive = gr.Button("🏛️ W3B 4RCH1V3 NFT", elem_classes=["holographic-btn"])
            buttons['webarchive_nft'] = btn_webarchive
            
        if 'lopht_advisory' in template_functions:
            btn_lopht_advisory = gr.Button("⚠️ L0PHT 4DV150RY", elem_classes=["holographic-btn"])
            buttons['lopht_advisory'] = btn_lopht_advisory
    
    return buttons

def create_holographic_interface(hacker_groups, data_sources, template_functions, echo_function=None):
    """
    Create the complete holographic interface
    
    Args:
        hacker_groups (dict): Information about hacker groups
        data_sources (dict): Data for tabs and displays
        template_functions (dict): Functions to generate template text
        echo_function (function, optional): Function for the echo L0pht members feature
        
    Returns:
        gr.Blocks: The complete Gradio interface
    """
    # Load custom CSS
    css = load_holo_styles()
    
    # Create the interface
    with gr.Blocks(theme=gr.themes.Glass(), css=css) as demo:
        # Header
        gr.Markdown(
            """<h1 class="holo-title">0M3G4 H4X0R H1ST0R1C4L MU53UM</h1>
            <p class="title">H0L0 T0UCH B453D M4TR1X N30 1NT3RF4C3</p>""", 
            elem_id="title-md"
        )
        
        # Main content area
        with gr.Row(elem_classes=["holographic"]):
            # Left sidebar with controls
            with gr.Column(scale=1):
                # Group selector
                gr.Markdown("### <span class='emoji-icon'>🔐</span> S3L3CT H4X0R GR0UP")
                group_selector = gr.Dropdown(
                    choices=["None"] + list(hacker_groups.keys()),
                    value="None",
                    label="Hacker Collective Theme",
                    elem_classes=["holo-input"]
                )
                
                # Micro-modules section
                gr.Markdown("### <span class='emoji-icon'>🌐</span> M1CR0-M0DUL3S")
                buttons = create_micro_module_buttons(template_functions)
                
                # Group info display
                group_info = gr.Markdown(elem_classes=["matrix-bg"])
                
                # Echo L0pht members button (if function available)
                if echo_function:
                    btn_echo_members = gr.Button("📣 3CH0 L0PHT M3MB3R5", 
                                                elem_classes=["holographic-btn", "echo-btn"])
                    echo_output = gr.Markdown(elem_classes=["echo-output"])
            
            # Main content area with markdown input
            with gr.Column(scale=2):
                gr.Markdown("### <span class='emoji-icon'>📝</span> 3NT3R M4RKDOWN T3XT", 
                           elem_classes=["matrix-bg"])
                markdown_input = gr.Textbox(
                    lines=10,
                    placeholder="Enter your markdown text here...",
                    label="Input Markdown",
                    elem_classes=["holo-input"]
                )
                convert_btn = gr.Button("🔄 C0NV3RT T0 H4X0R M4NU5CR1PT", 
                                       variant="primary", 
                                       elem_classes=["holographic-btn"])
        
        # Tabs for output and data displays
        with gr.Row(elem_classes=["holographic"]):
            tabs = create_tabs(data_sources)
        
        # Connect callbacks
        
        # Group selector callback
        def update_group_info(group_key):
            if group_key == "None" or group_key not in hacker_groups:
                return "Select a hacking collective to see details"
            
            group = hacker_groups[group_key]
            info = f"""### <span class='emoji-icon'>{group['emoji']}</span> {group['name']} ({group_key})
            
**Era:** {group['era']}
**Focus:** {group['description']}
**Key Members:** {', '.join(group['members'])}
            """
            return info
        
        group_selector.change(
            update_group_info, 
            inputs=[group_selector], 
            outputs=[group_info]
        )
        
        # Convert button callback
        convert_btn.click(
            lambda text, group: create_hacker_manuscript(text, hacker_groups, group),
            inputs=[markdown_input, group_selector],
            outputs=[tabs[0][1], tabs[1][1]]  # HTML output and Image output
        )
        
        # Template button callbacks
        for key, button in buttons.items():
            if key in template_functions:
                button.click(
                    lambda func=template_functions[key]: func(),
                    outputs=[markdown_input]
                )
        
        # Echo L0pht members callback
        if echo_function and 'btn_echo_members' in locals():
            btn_echo_members.click(
                lambda: echo_function(),
                outputs=[echo_output]
            )
    
    return demo 