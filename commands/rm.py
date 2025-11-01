import shutil
from pathlib import Path
from logger import log_command
from validator import validate_rm_args, validate_rm_safe

def rm(args):
    if not args:
        print("Ошибка: укажите файл или каталог")
        log_command("rm", success=False, error_msg="Не указан объект")
        return

    recursive = "-r" in args
    if recursive:
        args = [a for a in args if a != "-r"]

    path = Path(args[0])

    try:
        validate_rm_args(path, recursive)
        validate_rm_safe(path)

        if path.is_dir():
            confirm = input(f"Удалить каталог '{path}' рекурсивно? (y/n): ").strip().lower()
            if confirm != 'y':
                print("Отменено")
                log_command(f"rm {'-r ' if recursive else ''}{args[0]}", success=False, error_msg="Отменено пользователем")
                return
            shutil.rmtree(path)
        else:
            path.unlink()

        log_command(f"rm {'-r ' if recursive else ''}{args[0]}")

    except Exception as e:
        print(f"ERROR: {e}")
        log_command(f"rm {'-r ' if recursive else ''}{args[0]}", success=False, error_msg=str(e))