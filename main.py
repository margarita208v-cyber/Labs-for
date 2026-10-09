# Точка входа проекта measurement_project

import logging
from pathlib import Path

from utils.reader import read_numbers
from utils.statistics import calculate_average, find_min, find_max


def validate_numbers(numbers):
    if not numbers:
        raise ValueError("Список измерений пуст")


def main():
    # Настройка логирования
    Path("logs").mkdir(exist_ok=True)
    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        encoding="utf-8",
        force=True,
    )

    logging.info("Запуск программы")
    print(f"Текущий рабочий каталог: {Path.cwd()}")

    input_file = Path("data") / "measurements.txt"
    print(f"Путь к файлу: {input_file}")

    try:
        numbers = read_numbers(input_file)
        logging.info(f"Файл успешно прочитан: {input_file}")
        logging.info(f"Прочитано значений: {len(numbers)}")

        validate_numbers(numbers)

        count = len(numbers)
        avg = calculate_average(numbers)
        mn = find_min(numbers)
        mx = find_max(numbers)

        print(f"Количество: {count}")
        print(f"Среднее:    {avg:.2f}")
        print(f"Минимум:    {mn}")
        print(f"Максимум:   {mx}")

        logging.info(f"Статистика: count={count}, min={mn}, max={mx}, avg={avg:.2f}")

    except FileNotFoundError as e:
        logging.error(f"FileNotFoundError: {e}")
        print(f"Ошибка: файл не найден — {e}")

    except ValueError as e:
        logging.error(f"ValueError: {e}")
        print(f"Ошибка значения: {e}")

    finally:
        logging.info("Завершение программы")


if __name__ == "__main__":
    main()