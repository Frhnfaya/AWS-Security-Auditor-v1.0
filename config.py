 # AWS Security Auditor - Configuration File

# AWS Settings
AWS_REGION = 'us-east-1'  

# Severity Levels
SEVERITY = {
    'HIGH': '🔴 HIGH',
    'MEDIUM': '🟡 MEDIUM',
    'LOW': '🟢 LOW',
    'INFO': 'ℹ️  INFO'
}

# Colors for terminal output (using colorama)
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

COLORS = {
    'HIGH': Fore.RED,
    'MEDIUM': Fore.YELLOW,
    'LOW': Fore.GREEN,
    'INFO': Fore.CYAN,
    'RESET': Style.RESET_ALL
}

# Scanner settings
SCAN_TIMEOUT = 30  # seconds
MAX_RETRIES = 3
