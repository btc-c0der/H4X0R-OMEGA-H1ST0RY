#!/usr/bin/env python3
"""
H4X0R-OMEGA-H1ST0RY L0PHT C3L3BR4T10N
ASCII art celebration script for the successful deployment of the H4X0R-OMEGA-H1ST0RY space
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

def matrix_rain(iterations=50, width=80, density=0.1, speed=0.02):
    """Display a brief matrix-style rain animation."""
    matrix_chars = "01ブラックハット10ネオハッカー01ĿØÞĦŦとウエアシ0101010"
    drops = [0] * width
    
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
                        line += f"{BRIGHT_GREEN}{random.choice(matrix_chars)}{RESET}"
                    elif intensity > 0.5:
                        line += f"{GREEN}{random.choice(matrix_chars)}{RESET}"
                    else:
                        line += f"{GREEN}{random.choice('01')}{RESET}"
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

def display_lopht_logo():
    """Display L0pht Heavy Industries ASCII art logo."""
    logo = f"""
{BOLD}{CYAN}█    █▀█ █▀█ █ █ ▀█▀    █ █ █▀▀ ▄▀█ █ █ █▄█    █ █▄ █ █▀▄ █ █ █▀ ▀█▀ █▀█ █ █▀▀ █▀
{BOLD}{CYAN}█▄▄  █▄█ █▀▀ █▀█  █     █▀█ ██▄ █▀█ ▀▄▀  █     █ █ ▀█ █▄▀ █▄█ ▄█  █  █▀▄ █ ██▄ ▄█{RESET}
    """
    print(logo)

def display_h4x0r_logo():
    """Display H4X0R-OMEGA-H1ST0RY ASCII art logo."""
    logo = f"""
{BOLD}{GREEN} █ █ █▀█ ▀▄▀ █▀█ █▀█   █▀█ █▀▄▀█ █▀▀ █▀▀ ▄▀█   █ █ █ █▀ ▀█▀ █▀█ █▀█ █▄█
{BOLD}{GREEN} █▀█ █▀█  █  █▄█ █▀▄   █▄█ █ ▀ █ ██▄ █▄█ █▀█   █▀█ █ ▄█  █  █▄█ █▀▄  █ {RESET}
    """
    print(logo)

def display_success_banner():
    """Display a success banner."""
    banner = f"""
{BOLD}{YELLOW}╔═════════════════════════════════════════════════════════════════════╗
║                                                                     ║
║  {GREEN}S P 4 C 3   D 3 P L 0 Y 3 D   S U C C 3 S S F U L L Y{YELLOW}              ║
║                                                                     ║
║  {CYAN}H4X0R-OMEGA-H1ST0RY is n0w 0NL1N3{YELLOW}                                 ║
║                                                                     ║
╚═════════════════════════════════════════════════════════════════════╝{RESET}
    """
    print(banner)

def random_hacker_quote():
    """Return a random hacker quote."""
    quotes = [
        "We could shut down the entire Internet in 30 minutes. - L0pht to Congress, 1998",
        "Information wants to be free. - Hackers Manifesto",
        "Hack the planet! - Hackers, 1995",
        "Never trust the system. Always verify. - Hacker wisdom",
        "This is our world now... the world of the electron and the switch. - The Mentor",
        "A hacker on steroids. - Media description of L0pht"
    ]
    return random.choice(quotes)

def main():
    """Run the celebration script."""
    clear_screen()
    
    # Matrix rain animation
    matrix_rain(iterations=30, speed=0.03)
    
    clear_screen()
    
    # Display the main title
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{YELLOW}[*] {GREEN}H4X0R-OMEGA-H1ST0RY{RESET} activation sequence initiated at {CYAN}{now}{RESET}\n")
    time.sleep(1)
    
    # L0pht logo
    display_lopht_logo()
    time.sleep(1.5)
    
    # H4X0R logo
    display_h4x0r_logo()
    time.sleep(1.5)
    
    # Success banner
    display_success_banner()
    time.sleep(1)
    
    # Type hacker wisdom
    print(f"\n{YELLOW}[*] {RESET}Hacker wisdom: ")
    type_text(f"{GREEN}{random_hacker_quote()}{RESET}", 0.03)
    time.sleep(1)
    
    # Final message
    print(f"\n{YELLOW}[*] {RESET}Connection established to: {CYAN}https://huggingface.co/spaces/fartec0/H4X0R-OMEGA-H1ST0RY{RESET}")
    print(f"\n{YELLOW}[*] {RESET}Status: {GREEN}PRIVATE{RESET}")
    print(f"\n{YELLOW}[*] {GREEN}Hackers of the world, unite!{RESET}\n")
    
    # Final matrix rain
    input(f"{YELLOW}[*] {RESET}Press Enter to return to the matrix...")
    matrix_rain(iterations=50, speed=0.02)
    clear_screen()
    
    # End message
    print(f"\n{GREEN}CONNECTION TERMINATED{RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] {RESET}User interrupted. Exiting the matrix...\n")
        sys.exit(0) 