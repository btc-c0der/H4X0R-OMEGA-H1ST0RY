"""
Fixed manuscript generator function for H4X0R-OMEGA-H1ST0RY
Copy this function to replace the one in app.py
"""

def create_hacker_manuscript(markdown_text, group_theme=None):
    """
    Create a styled hacker manuscript from markdown text.
    Includes fixes for font handling and error robustness.
    
    Args:
        markdown_text (str): Markdown text to convert
        group_theme (str, optional): Hacker group theme to apply
        
    Returns:
        tuple: (html_content, image_bytes) - styled HTML and PNG image
    """
    try:
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
        
        # Try to load a default font, fallback to None if unavailable
        try:
            font = ImageFont.load_default()
        except Exception:
            font = None
        
        # Add group-specific theming if selected
        group_banner = ""
        if group_theme and group_theme in HACKER_GROUPS:
            group = HACKER_GROUPS[group_theme]
            group_banner = f"{group['emoji']} {group['name']} | {group['era']} | {group['emoji']}"
            
            # Draw group banner
            draw.rectangle([(0, 0), (width, 40)], fill=(0, 30, 0, 230))
            if font:
                draw.text((10, 10), group_banner, fill=(0, 255, 0), font=font)
            else:
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
            try:
                if font:
                    draw.text((20, y_position), decorated_line, fill=(0, 255, 0), font=font)
                else:
                    draw.text((20, y_position), decorated_line, fill=(0, 255, 0))
            except Exception:
                # Handle any text drawing errors gracefully
                # Draw a placeholder line if text fails
                draw.rectangle([(20, y_position), (min(width-20, 20 + len(decorated_line)*8), y_position+5)], fill=(0, 255, 0))
            
            y_position += 25
        
        # Draw footer
        footer_y = height - 30
        draw.rectangle([(0, footer_y), (width, height)], fill=(0, 30, 0, 230))
        
        footer_text = "0M3G4 H4X0R H1ST0R1C4L MU53UM // N30-M4TR1X"
        try:
            if font:
                draw.text((10, footer_y + 5), footer_text, fill=(0, 255, 0), font=font)
            else:
                draw.text((10, footer_y + 5), footer_text, fill=(0, 255, 0))
        except Exception:
            # Draw a placeholder footer if text fails
            draw.rectangle([(10, footer_y + 5), (width - 10, footer_y + 15)], fill=(0, 255, 0))
        
        # Convert to bytes for Gradio
        img_byte_arr = io.BytesIO()
        background.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        
        # Return both the styled HTML and the image
        return html_content, img_byte_arr.getvalue()
    
    except Exception as e:
        # If anything goes wrong, return an error message and a basic image
        error_message = f"<h1>Error generating manuscript</h1><p>{str(e)}</p>"
        
        # Create a simple error image
        error_img = Image.new('RGB', (800, 300), color=(0, 0, 0))
        error_draw = ImageDraw.Draw(error_img)
        try:
            error_draw.text((20, 20), "Error generating H4X0R manuscript", fill=(255, 0, 0))
            error_draw.text((20, 50), str(e), fill=(255, 0, 0))
            error_draw.text((20, 80), "Please try again with different content", fill=(0, 255, 0))
        except Exception:
            # Even drawing the error message failed, just leave the black background
            pass
        
        error_bytes = io.BytesIO()
        error_img.save(error_bytes, format='PNG')
        error_bytes.seek(0)
        
        return error_message, error_bytes.getvalue() 