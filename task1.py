from pathlib import Path
import shutil
import sys

def parse_arguments():
    source_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    destination_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")
    return source_dir, destination_dir

def copy_and_sort_files(src: Path, dest: Path):
    try:
        for item in src.iterdir():
            if item.is_dir():
                copy_and_sort_files(item, dest)
            elif item.is_file():
                extension = item.suffix[1:].lower()  
                target_dir = dest / extension

                target_dir.mkdir(parents=True, exist_ok=True)

                try:
                    shutil.copy2(item, target_dir)
                    print(f"Копіюємо: {item} -> {target_dir}")
                except Exception as e:
                    print(f"Помилка копіювання {item}: {e}")
    except Exception as e:
        print(f"Помилка доступу до {src}: {e}")

def main():
    source_dir, destination_dir = parse_arguments()

    if not source_dir.exists():
        print(f"Вихідна директорія '{source_dir}' не знайдена.")
        sys.exit(1)

    destination_dir.mkdir(parents=True, exist_ok=True)

    copy_and_sort_files(source_dir, destination_dir)
    print("Копіювання завершено.")

if __name__ == "__main__":
    main()