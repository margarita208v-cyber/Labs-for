"""Модуль чтения числовых данных из файла."""


def read_numbers(file_path):
    """Читает файл и возвращает список чисел (float)."""
    numbers = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                numbers.append(float(line))
    return numbers
