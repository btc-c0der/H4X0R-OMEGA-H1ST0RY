"""
H4X0R-OMEGA-H1ST0RY Manuscript Generator
Converts markdown to stylized hacker-themed manuscripts
"""

import re
import random
import io
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import markdown

# Text transformation functions
def hackerize_text(text):
    """
    Convert normal text to l33t speak by replacing characters
    
    Args:
        text (str): Input text to transform
        
    Returns:
        str: Text with characters replaced for l33t aesthetics
    """
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

# Visual effects for manuscript generation
def generate_matrix_background(width=800, height=400):
    """
    Create a matrix-style background image
    
    Args:
        width (int): Width of the image
        height (int): Height of the image
        
    Returns:
        PIL.Image: Matrix-effect background image
    """
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
            try:
                draw.text((x, actual_y), char, fill=color_with_opacity)
            except Exception as e:
                # Fix: Use a default font or fallback to a simple shape
                try:
                    font = ImageFont.load_default()
                    draw.text((x, actual_y), char, fill=color_with_opacity, font=font)
                except Exception:
                    # Fallback to simple rectangle if text fails
                    draw.rectangle([(x, actual_y), (x+10, actual_y+10)], fill=color_with_opacity)
    
    # Apply a slight blur for the "glow" effect
    try:
        image = image.filter(ImageFilter.GaussianBlur(radius=1))
    except Exception:
        # Skip blur if it fails
        pass
    
    return image

# Main manuscript generator function
def create_hacker_manuscript(markdown_text, hacker_groups=None, group_theme=None):
    """
    Create a styled hacker manuscript from markdown text
    
    Args:
        markdown_text (str): Markdown text to convert
        hacker_groups (dict): Dictionary of hacker group information
        group_theme (str, optional): Hacker group theme to apply
        
    Returns:
        tuple: (html_content, image_bytes) - styled HTML and PNG image
    """
    if hacker_groups is None:
        hacker_groups = {}
        
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
        if group_theme and group_theme in hacker_groups:
            group = hacker_groups[group_theme]
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