#!/usr/bin/env python3
"""
Test script for the H4X0R-OMEGA-H1ST0RY manuscript generator
This helps identify any issues with the manuscript generation functionality
"""

import os
import re
import random
import io
import sys
import markdown
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
import traceback

# Mock data for testing
MOCK_HACKER_GROUPS = {
    "L0PHT": {
        "name": "L0pht Heavy Industries",
        "emoji": "🔐",
        "description": "Created L0phtCrack and testified to Congress",
        "members": ["Mudge", "Space Rogue", "Weld Pond", "Kingpin"],
        "era": "Late 1990s"
    }
}

# Hacker lingo transformation function copied from app.py
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

# Matrix effect generation copied from app.py
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
            # Issue: This line can fail if no font is specified or available
            try:
                draw.text((x, actual_y), char, fill=color_with_opacity)
            except Exception as e:
                print(f"Error drawing text: {e}")
                # Fix: Provide a default font if available
                try:
                    font = ImageFont.load_default()
                    draw.text((x, actual_y), char, fill=color_with_opacity, font=font)
                except Exception as font_e:
                    print(f"Font error: {font_e}")
                    # Fallback to simple rectangle if text fails
                    draw.rectangle([(x, actual_y), (x+10, actual_y+10)], fill=color_with_opacity)
    
    # Apply a slight blur for the "glow" effect
    try:
        image = image.filter(ImageFilter.GaussianBlur(radius=1))
    except Exception as e:
        print(f"Blur error: {e}")
    
    return image

# Manuscript generation function with error handling
def create_hacker_manuscript(markdown_text, group_theme=None):
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
        
        print(f"Creating image with dimensions: {width}x{height}")
        
        # Create base image with matrix effect
        background = generate_matrix_background(width, height)
        draw = ImageDraw.Draw(background)
        
        # Add group-specific theming if selected
        group_banner = ""
        if group_theme and group_theme in MOCK_HACKER_GROUPS:
            group = MOCK_HACKER_GROUPS[group_theme]
            group_banner = f"{group['emoji']} {group['name']} | {group['era']} | {group['emoji']}"
            
            # Draw group banner
            draw.rectangle([(0, 0), (width, 40)], fill=(0, 30, 0, 230))
            
            # Fix: Add font for text drawing
            try:
                font = ImageFont.load_default()
                draw.text((10, 10), group_banner, fill=(0, 255, 0), font=font)
            except Exception as e:
                print(f"Error drawing banner: {e}")
                draw.text((10, 10), group_banner, fill=(0, 255, 0))
        
        # Add content with retro hacker styling
        y_position = 60
        lines = hacker_text.split('\n')
        
        # Fix: Check font availability
        try:
            font = ImageFont.load_default()
            has_font = True
        except Exception:
            has_font = False
            print("Warning: Default font not available")
        
        for line in lines:
            if line.strip() == "":
                y_position += 20
                continue
                
            # Add hackerspeak symbols as line decorators
            prefix = random.choice(["[+] ", ">>> ", "## ", "/*", "$> ", "h4x: "])
            decorated_line = prefix + line
            
            # Draw text with green terminal-like glow
            try:
                if has_font:
                    draw.text((20, y_position), decorated_line, fill=(0, 255, 0), font=font)
                else:
                    draw.text((20, y_position), decorated_line, fill=(0, 255, 0))
            except Exception as e:
                print(f"Error drawing line of text: {e}")
                # Draw a placeholder if text fails
                draw.rectangle([(20, y_position), (100, y_position+10)], fill=(0, 255, 0))
            
            y_position += 25
        
        # Draw footer
        footer_y = height - 30
        draw.rectangle([(0, footer_y), (width, height)], fill=(0, 30, 0, 230))
        
        try:
            if has_font:
                draw.text((10, footer_y + 5), "0M3G4 H4X0R H1ST0R1C4L MU53UM // N30-M4TR1X", fill=(0, 255, 0), font=font)
            else:
                draw.text((10, footer_y + 5), "0M3G4 H4X0R H1ST0R1C4L MU53UM // N30-M4TR1X", fill=(0, 255, 0))
        except Exception as e:
            print(f"Error drawing footer: {e}")
        
        # Convert to bytes for output
        img_byte_arr = io.BytesIO()
        background.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        
        print("Successfully generated manuscript!")
        return html_content, img_byte_arr.getvalue()
    
    except Exception as e:
        print(f"Error in manuscript generation: {e}")
        traceback.print_exc()
        # Return error message and fallback image
        error_img = Image.new('RGB', (400, 200), color=(0, 0, 0))
        draw = ImageDraw.Draw(error_img)
        try:
            draw.text((10, 10), f"Error: {str(e)}", fill=(255, 0, 0))
            draw.text((10, 30), "Check console for details", fill=(255, 0, 0))
        except Exception:
            pass  # Even fallback text failed
        
        error_bytes = io.BytesIO()
        error_img.save(error_bytes, format='PNG')
        error_bytes.seek(0)
        
        return f"<h1>Error in manuscript generation</h1><p>{str(e)}</p>", error_bytes.getvalue()

def run_tests():
    """Run a series of tests on the manuscript generator"""
    print("Running H4X0R-OMEGA-H1ST0RY manuscript generator tests...\n")
    
    test_cases = [
        {
            "name": "Simple text",
            "markdown": "# Test\n\nSimple text for testing",
            "group": None
        },
        {
            "name": "Complex markdown",
            "markdown": """
# Complex Test
## With multiple headings

- And bullet points
- *Italic text*
- **Bold formatting**

```
Code blocks
with multiple lines
```

> And block quotes too
            """,
            "group": None
        },
        {
            "name": "Group theme test",
            "markdown": "# L0pht Test\n\nTesting with L0pht theme",
            "group": "L0PHT"
        },
        {
            "name": "Long text test",
            "markdown": "# " + "Very long heading\n\n" + "Test content\n" * 50,
            "group": None
        },
        {
            "name": "Special characters test",
            "markdown": "# Special Characters\n\n" + 
                       "Unicode: ñáéíóú Émojïs: 🔐🔒🖥️💻\n" +
                       "Symbols: @#$%^&*()",
            "group": None
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest #{i}: {test['name']}")
        print("-" * 40)
        
        try:
            html, image_bytes = create_hacker_manuscript(test["markdown"], test["group"])
            print(f"HTML output length: {len(html)} characters")
            print(f"Image data size: {len(image_bytes)} bytes")
            
            # Optional: Save the images for inspection
            with open(f"test_output_{i}.png", "wb") as f:
                f.write(image_bytes)
                print(f"Saved image to test_output_{i}.png")
            
            print("Test PASSED ✓")
        except Exception as e:
            print(f"Test FAILED ✗ - Error: {e}")
            traceback.print_exc()
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    run_tests() 