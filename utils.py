class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

def color_text(text: str, color: str) -> str:
    return f"{color}{text}{Colors.RESET}"
