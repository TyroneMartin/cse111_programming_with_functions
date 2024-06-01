# Define ANSI escape codes for colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"  # Reset to default color

# Example usage
print(f"{RED}This is red text{RESET}")
print(f"{GREEN}This is green text{RESET}")
print(f"{YELLOW}This is yellow text{RESET}")
print(f"{BLUE}This is blue text{RESET}")
print(f"{MAGENTA}This is magenta text{RESET}")
print(f"{CYAN}This is cyan text{RESET}")
print("This is default color text")

# Example of changing color for a portion of the text
print(f"This is {RED}red{RESET} and this is {GREEN}green{RESET}.")
print(f"Mixing {YELLOW}yellow{RESET} with {BLUE}blue{RESET} and {MAGENTA}magenta{RESET}.")
print(f"Using {CYAN}cyan{RESET} within the same sentence.")

# Example of embedding colors within a longer string
message = f"Warning: {RED}Disk space is low{RESET}. Please {GREEN}delete unnecessary files{RESET} to free up space."
print(message)
