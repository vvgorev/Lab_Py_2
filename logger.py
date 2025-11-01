from datetime import datetime
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent

def log_command(command, success=True, error_msg=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if success:
        log_entry = f"[{timestamp}] {command}\n"
    else:
        log_entry = f"[{timestamp}] ERROR: {error_msg}\n"

    log_file = PROJECT_DIR / "shell.log"

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)