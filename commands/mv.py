from pathlib import Path
from logger import log_command

def mv(args):
    if len(args) < 2:
        print("Ошибка: укажите источник и назначение")
        log_command("mv", success=False, error_msg="Не хватает аргументов")
        return

    src = Path(args[0])
    dst = Path(args[1])

    try:
        if not src.exists():
            raise FileNotFoundError(f"Источник {src} не найден")

        if dst.exists() and dst.is_dir():
            dst = dst / src.name

        src.rename(dst)

        log_command(f"mv {args[0]} {args[1]}")

    except Exception as e:
        print(f"ERROR: {e}")
        log_command(f"mv {args[0]} {args[1]}", success=False, error_msg=str(e))