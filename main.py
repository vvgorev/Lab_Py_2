from parser import parse_input
from commands.ls import ls
from commands.cd import cd
from commands.cat import cat
from commands.cp import cp
from commands.mv import mv
from commands.rm import rm
from logger import log_command

def main():
    print("Mini-Shell. Введите 'exit' для выхода.")
    while True:
        try:
            user_input = input(">>> ").strip()
            if user_input.lower() == "exit":
                break

            cmd, args = parse_input(user_input)
            if not cmd:
                continue

            if cmd == "ls":
                ls(args)
            elif cmd == "cd":
                cd(args)
            elif cmd == "cat":
                cat(args)
            elif cmd == "cp":
                cp(args)
            elif cmd == "mv":
                mv(args)
            elif cmd == "rm":
                rm(args)
            else:
                print(f"Неизвестная команда: {cmd}")
                log_command(user_input, success=False, error_msg=f"Неизвестная команда: {cmd}")

        except KeyboardInterrupt:
            print("\nВыход...")
            break

if __name__ == "__main__":
    main()