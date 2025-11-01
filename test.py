import os
import tempfile
import shutil
from pathlib import Path

# Импорты из твоих модулей
from commands.ls import ls
from commands.cd import cd
from commands.cat import cat
from commands.cp import cp
from commands.mv import mv
from commands.rm import rm
from logger import log_command

def run_test(description, test_func):
    print(f"\nТест: {description}")
    try:
        test_func()
        print("Успех")
    except Exception as e:
        print(f"Ошибка: {e}")

def test_ls():
    ls([])

def test_cat():
    # Создаём временный файл
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("Тестовый файл\n")
        fname = f.name
    cat([fname])
    os.unlink(fname)

def test_cd():
    old_cwd = os.getcwd()
    cd([".."])
    assert os.getcwd() != old_cwd
    os.chdir(old_cwd)

def test_cp():
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("Тест копирования\n")
        src = f.name
    dst = src + ".copy"
    cp([src, dst])
    assert os.path.exists(dst)
    os.unlink(src)
    os.unlink(dst)

def test_mv():
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("Тест перемещения\n")
        src = f.name
    dst = src + "_new"
    mv([src, dst])
    assert os.path.exists(dst)
    assert not os.path.exists(src)
    os.unlink(dst)

def test_rm():
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("Тест удаления\n")
        fname = f.name
    rm([fname])
    assert not os.path.exists(fname)

if __name__ == "__main__":
    print("Запуск тестов...")
    run_test("ls", test_ls)
    run_test("cat", test_cat)
    run_test("cd", test_cd)
    run_test("cp", test_cp)
    run_test("mv", test_mv)
    run_test("rm", test_rm)
    print("\nВсе тесты завершены.")