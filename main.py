"""Точка входа проекта measurement_project."""

from utils.statistics import calculate_average, find_min, find_max


def main():
    numbers = [12.5, 7.8, 15.3, 9.1, 20.4, 3.6, 18.9, 11.2, 14.7, 8.3]
    print("Среднее:", calculate_average(numbers))
    print("Минимум:", find_min(numbers))
    print("Максимум:", find_max(numbers))


if __name__ == "__main__":
    main()
    