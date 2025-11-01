import shutil
from pathlib import Path
from logger import log_command
from validator import validate_cp_args

def cp(args):
    if len(args) < 2:
        print("Ошибка: укажите источник и назначение")
        log_command("cp", success=False, error_msg="Не хватает аргументов")
        return

    recursive = "-r" in args
    if recursive:
        args = [a for a in args if a != "-r"]

    src = Path(args[0])
    dst = Path(args[1])

    try:
        validate_cp_args(src, dst, recursive)

        if src.is_dir():
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            if dst.is_dir():
                dst = dst / src.name
            shutil.copy2(src, dst)

        log_command(f"cp {'-r ' if recursive else ''}{args[0]} {args[1]}")

    except Exception as e:
        print(f"ERROR: {e}")
        log_command(f"cp {'-r ' if recursive else ''}{args[0]} {args[1]}", success=False, error_msg=str(e))