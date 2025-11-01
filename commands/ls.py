from pathlib import Path
from logger import log_command
from validator import ensure_is_dir
from datetime import datetime

def ls(arg):
    path = "."
    long_format = False

    if arg and arg[0] == "-l":
        long_format = True
        arg = arg[1:]

    if arg:
        path = arg[0]

    try:
        p = Path(path)
        ensure_is_dir(p)

        items = list(p.iterdir())

        if long_format:
            for item in items:
                stat = item.stat()
                size = stat.st_size
                mtime = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M")
                type_str = "d" if item.is_dir() else "-"
                print(f"{type_str}rw-r--r-- {size:>8} {mtime} {item.name}")
        else:
            for item in items:
                print(item.name)
    
        log_command(f"ls {'-l ' if long_format else ''}{path}")
    
    except Exception as e:
        print(f"ERROR: {e}")
        log_command(f"ls {'-l ' if long_format else ''}{path}", success=False, error_msg=str(e))

