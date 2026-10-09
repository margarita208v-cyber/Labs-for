"""Точка входа проекта measurement_project."""

from utils.reader import read_numbers
from utils.statistics import calculate_average, find_min, find_max


def main():
    numbers = read_numbers("data/measurements.txt")
    print("Прочитано:", numbers)
    print("Среднее:", calculate_average(numbers))
    print("Минимум:", find_min(numbers))
    print("Максимум:", find_max(numbers))


if __name__ == "__main__":
    main()
