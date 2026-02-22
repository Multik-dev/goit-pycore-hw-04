import sys
from pathlib import Path
from colorama import Fore, Style, init

# щоб кольори працювали на Windows теж
init(autoreset=True)


def print_tree(path: Path, level: int = 0) -> None:
    """
    Рекурсивно виводить структуру директорії.
    level - рівень вкладеності (для відступів).
    """
    indent = "  " * level

    # Сортуємо: спочатку папки, потім файли, і все за алфавітом
    items = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))

    for item in items:
        if item.is_dir():
            # Папки - іншим кольором
            print(f"{indent}{Fore.CYAN}📂 {item.name}{Style.RESET_ALL}")
            print_tree(item, level + 1)
        else:
            # Файли - іншим кольором
            print(f"{indent}{Fore.YELLOW}📜 {item.name}{Style.RESET_ALL}")


def main() -> None:
    # Перевіряємо, чи передали аргумент
    if len(sys.argv) < 2:
        print("Використання: python hw03.py /шлях/до/директорії")
        return

    dir_path = Path(sys.argv[1])

    # Перевірки на помилки
    if not dir_path.exists():
        print(f"{Fore.RED}Помилка: шлях не існує -> {dir_path}{Style.RESET_ALL}")
        return

    if not dir_path.is_dir():
        print(f"{Fore.RED}Помилка: це не директорія -> {dir_path}{Style.RESET_ALL}")
        return

    # Друкуємо корінь
    print(f"{Fore.GREEN}📦 {dir_path.name}{Style.RESET_ALL}")
    print_tree(dir_path)


if __name__ == "__main__":
    main()
