from pathlib import Path

def ensure_exists(path):
    if not path.exists():
        raise FileNotFoundError(f"Путь {path} не существует")

def ensure_is_dir(path):
    if not path.is_dir():
        raise NotADirectoryError(f"объект {path} не является каталогом")

def ensure_is_file(path):
    if not path.is_file():
        raise IsADirectoryError(f"объект {path} не является файлом")
    
def validate_cp_args(src, dst, recursive=False):
    """Проверяет аргументы для команды cp."""
    ensure_exists(src)
    if src.is_dir() and not recursive:
        raise ValueError("Для копирования каталога используйте опцию -r")

def validate_rm_args(path, recursive=False):
    """Проверяет аргументы для команды rm."""
    ensure_exists(path)
    if path.is_dir() and not recursive:
        raise ValueError("Для удаления каталога используйте опцию -r")

def validate_rm_safe(path):
    """Проверяет, что путь не критичный для удаления."""
    resolved = path.resolve()
    if resolved == Path("/") or str(resolved).endswith("C:\\"):
        raise PermissionError("Нельзя удалить корневой каталог")