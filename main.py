#Точка входа проекта measurement_project.

from pathlib import Path

from utils.reader import read_numbers
from utils.statistics import calculate_average, find_min, find_max


def main():
    print(f"Текущий рабочий каталог: {Path.cwd()}")

    input_file = Path("data") / "measurements.txt"
    print(f"Путь к файлу: {input_file}")

    Path("logs").mkdir(exist_ok=True)

    try:
        numbers = read_numbers(input_file)
        print(f"Прочитано значений: {len(numbers)}")
        print("Среднее:", calculate_average(numbers))
        print("Минимум:", find_min(numbers))
        print("Максимум:", find_max(numbers))

    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден")

    except ValueError as e:
        print(f"Ошибка значения: {e}")


if __name__ == "__main__":
    main()