"""Точка входа проекта measurement_project."""

from pathlib import Path

from utils.reader import read_numbers
from utils.statistics import calculate_average, find_min, find_max


def main():
    # Текущий рабочий каталог
    print(f"Текущий рабочий каталог: {Path.cwd()}")

    # Путь к файлу через pathlib
    input_file = Path("data") / "measurements.txt"
    print(f"Путь к файлу: {input_file}")

    # Проверка существования
    if not input_file.exists():
        print(f"Ошибка: файл {input_file} не найден")
        return

    # Создание каталога logs с exist_ok=True
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    numbers = read_numbers(input_file)
    print("Среднее:", calculate_average(numbers))
    print("Минимум:", find_min(numbers))
    print("Максимум:", find_max(numbers))


if __name__ == "__main__":
    main()