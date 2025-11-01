import os
from pathlib import Path
from logger import log_command
from validator import ensure_is_dir

def cd(args):
    if not args:
        target = Path.home()
    elif args[0] == "..":
        target = Path.cwd().parent
    else:
        target = Path(args[0])

    try:
        ensure_is_dir(target)
        os.chdir(target)
        log_command(f"cd {args[0] if args else ''}")

    except Exception as e:
        print(f"ERROR: {e}")
        log_command(f"cd {args[0] if args else ''}", success=False, error_msg=str(e))