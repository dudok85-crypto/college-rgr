import random

from algorithms import Bubble_Sort, Selection_Sort, Quick_Sort, Merge_Sort
from benchmark import measure_time


if __name__ == "__main__":
    # Генерация случайного списка
    test = [random.randint(1, 1000) for _ in range(100000)]

    # Замеряем время для каждого алгоритма
    time_bubble = measure_time(test, Bubble_Sort, 10)
    time_selection = measure_time(test, Selection_Sort, 10)
    time_quick = measure_time(test, Quick_Sort, 10)
    time_merge = measure_time(test, Merge_Sort, 10)

    print(
        f'Сортировка пузырьком: {time_bubble}\n'
        f'Сортировка выбором: {time_selection}\n'
        f'Быстрая сортировка: {time_quick}\n'
        f'Сортировка слиянием: {time_merge}'
    )
