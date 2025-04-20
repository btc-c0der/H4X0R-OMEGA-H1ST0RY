#!/usr/bin/env python3
"""
S0NN3T H4CK3R PHD L0PHT C3L3BR4T10N 420
ASCII art celebration script for the elite S0NN3T H4CK3R PHD L0PHT project
"""

import os
import time
import random
import sys
from datetime import datetime

# ANSI color codes
GREEN = "\033[32m"
BRIGHT_GREEN = "\033[92m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RED = "\033[31m"
PURPLE = "\033[35m"
BLUE = "\033[34m"
RESET = "\033[0m"
BOLD = "\033[1m"

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.025):
    """Type text with a delay between characters."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def matrix_rain(iterations=50, width=80, density=0.1, speed=0.02, colors=True):
    """Display a brief matrix-style rain animation."""
    matrix_chars = "01ブラックハット10クロード01ĿØÞĦŦソネット420ハッカー0101010"
    drops = [0] * width
    color_options = [GREEN, BRIGHT_GREEN, CYAN, BLUE] if colors else [GREEN]
    
    for _ in range(iterations):
        clear_screen()
        
        # Draw each column
        lines = []
        for i in range(20):  # Screen height
            line = ""
            for j in range(width):
                # If this column has a drop and the drop has reached this row
                if i < drops[j] and drops[j] > 0:
                    intensity = max(0, 1 - (drops[j] - i) / 10)
                    if intensity > 0.8:
                        line += f"{random.choice(color_options)}{random.choice(matrix_chars)}{RESET}"
                    elif intensity > 0.5:
                        line += f"{GREEN}{random.choice(matrix_chars)}{RESET}"
                    else:
                        line += f"{GREEN}{random.choice('01420')}{RESET}"
                else:
                    line += " "
            lines.append(line)
        
        # Print all lines at once
        print("\n".join(lines))
            
        # Update drops
        for j in range(width):
            # Start a new drop
            if drops[j] == 0 and random.random() < density:
                drops[j] = 1
            
            # Advance existing drops
            if drops[j] > 0:
                drops[j] += 1
                
            # Reset drops that have gone off screen
            if drops[j] > 20:
                drops[j] = 0
                
        time.sleep(speed)

def display_sonnet_phd_logo():
    """Display S0NN3T H4CK3R PHD ASCII art logo."""
    logo = f"""
{BOLD}{PURPLE}█▀ █▀█ █▄ █ █▄ █ █▀▀ ▀█▀   █ █ █▀█ █▀▀ █▄▀ █▀▀ █▀█   █▀█ █ █ █▀▄
{BOLD}{PURPLE}▄█ █▄█ █ ▀█ █ ▀█ ██▄  █    █▀█ █▀█ █▄▄ █ █ ██▄ █▀▄   █▀▀ █▀█ █▄▀{RESET}
    """
    print(logo)

def display_l0pht_420_logo():
    """Display L0PHT 420 ASCII art logo."""
    logo = f"""
{BOLD}{CYAN}█    █▀█ █▀█ █ █ ▀█▀          █▀█ █▀█ █▀█
{BOLD}{CYAN}█▄▄  █▄█ █▀▀ █▀█  █     ▄▄▄▄  █▀▀ ▀▀█ █▄█{RESET}
    """
    print(logo)

def display_success_banner():
    """Display a success banner."""
    banner = f"""
{BOLD}{YELLOW}╔═════════════════════════════════════════════════════════════════════╗
║                                                                     ║
║  {PURPLE}S 0 N N 3 T   H 4 C K 3 R   P H D   4 2 0   A C T 1 V 4 T 3 D{YELLOW}      ║
║                                                                     ║
║  {CYAN}L 0 P H T   3 L 1 T 3   S T 4 T U S   C 0 N F 1 R M 3 D{YELLOW}              ║
║                                                                     ║
╚═════════════════════════════════════════════════════════════════════╝{RESET}
    """
    print(banner)

def random_hacker_phd_quote():
    """Return a random hacker PhD quote."""
    quotes = [
        "The PhD in hacking is earned through practice, not papers. - S0NN3T",
        "In the realm of bits and bytes, we are the philosophers. - L0PHT",
        "420: The optimal entropy value for quantum-secure encryption. - CLAUDE",
        "We code with the precision of sonnets, each line a perfect verse. - Anonymous",
        "The best PhD defense is a good offense. - H4CK3R wisdom",
        "Not all doctorates are earned in universities. Some are forged in the digital underground. - 0M3G4"
    ]
    return random.choice(quotes)

def display_ascii_art():
    """Display a special ASCII art."""
    art = f"""
{GREEN}                      .
                     .:.
                    .:::.
                   .:::::.
               ***.:::::::.***
          *******.:::::::::.*******
       ********.:::::::::::.********
      ********.:::::::::::::.********
     ********.:::::::'***::::.********
    ********.:::::'*********'::.********
   ********.::::'*************'::.********
  ********.::::'*****************'::.********
 ********.::::*********************.::********
********.:::::******************::::.::********
********.::::,*****************,:::::.********
 ********.::::*******************::.********
  ********.::::+*****************::.********
   ********.::::+***************::.********
    ********.::::+*************::.********
     ********.::::+***********::.********
      ********.::::+*********::.********
       ********.::::+*******::.********
          *******.::::+***.:.*******
               ***.::::+.::.***
                   .:::.
                    .:.
                     .{RESET}

{CYAN}         420 S0NN3T H4CK3R PHD L0PHT{RESET}
"""
    print(art)

def main():
    """Run the celebration script."""
    clear_screen()
    
    # Matrix rain animation
    matrix_rain(iterations=30, speed=0.03, colors=True)
    
    clear_screen()
    
    # Display the main title
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{YELLOW}[*] {PURPLE}S0NN3T H4CK3R PHD{RESET} initialization sequence at {CYAN}{now}{RESET}\n")
    time.sleep(1)
    
    # Display special ASCII art
    display_ascii_art()
    time.sleep(2)
    
    # Display logos
    display_sonnet_phd_logo()
    time.sleep(1.5)
    
    display_l0pht_420_logo()
    time.sleep(1.5)
    
    # Success banner
    display_success_banner()
    time.sleep(1)
    
    # Type hacker wisdom
    print(f"\n{YELLOW}[*] {RESET}PhD Thesis Statement: ")
    type_text(f"{PURPLE}{random_hacker_phd_quote()}{RESET}", 0.03)
    time.sleep(1)
    
    # Final message
    print(f"\n{YELLOW}[*] {RESET}Connection established to: {CYAN}https://huggingface.co/spaces/fartec0/H4X0R-OMEGA-H1ST0RY{RESET}")
    print(f"\n{YELLOW}[*] {RESET}PhD Status: {GREEN}CONFERRED WITH HIGHEST HONORS{RESET}")
    print(f"\n{YELLOW}[*] {RESET}L0pht Clearance: {GREEN}LEVEL 420{RESET}")
    print(f"\n{YELLOW}[*] {PURPLE}Elite hackers transcend the digital realm!{RESET}\n")
    
    # Final matrix rain
    input(f"{YELLOW}[*] {RESET}Press Enter to return to the quantum matrix...")
    matrix_rain(iterations=50, speed=0.02, colors=True)
    clear_screen()
    
    # End message
    print(f"\n{GREEN}S0NN3T H4CK3R PHD L0PHT 420 SEQUENCE COMPLETE{RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] {RESET}User interrupted. PhD defense aborted...\n")
        sys.exit(0) 