from pathlib import Path
from logger import log_command
from validator import ensure_exists, ensure_is_file

def cat(args):
    if not args:
        print("Ошибка: укажите файл")
        log_command("cat", success=False, error_msg="Файл не указан")
        return

    filepath = Path(args[0])

    try:
        ensure_exists(filepath)
        ensure_is_file(filepath)

        with open(filepath, 'r', encoding='utf-8') as f:
            print(f.read())

        log_command(f"cat {args[0]}")

    except Exception as e:
        print(f"ERROR: {e}")
        log_command(f"cat {args[0]}", success=False, error_msg=str(e))