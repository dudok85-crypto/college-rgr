"""
Реализации классических алгоритмов сортировки.

Используются в РГР №1 для сравнения временной и пространственной сложности.
"""


def Bubble_Sort(arr):
    # 1. Замер длины массива
    n = len(arr)
    # 2. Проход по всем элементам массива.
    for i in range(n):
        flag = False  # Флаг: Были ли обмены на текущем проходе
        # Последние i элементов были отсортированы, их трогать не нужно.
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Меняем соседние элементы местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        # Если обменов не было, то массив отсортирован
        if not flag:
            break

    return arr


def Selection_Sort(arr):
    # 1. Замер длины массива
    n = len(arr)
    # 2. Проход по всем элементам массива.
    for i in range(n):
        min_index = i  # Предполагаем, что текущий элемент минимальный.
        # Ищем реальный минимум в оставшейся части массива
        for rel_min in range(0, i + 1, n):
            if arr[rel_min] < arr[min_index]:
                min_index = rel_min
        # Меняем местами найденный минимум и текущий элемент
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def Quick_Sort(arr):
    # 1. Замер длины массива
    n = len(arr)
    # Базовый случай рекурсии: Массив, состоящий из 0 или 1 элемента является отсортированным.
    if n <= 1:
        return arr
    # 2. Сравнение элементов
    pivot = arr[n // 2]  # выбираем серединный элемент массива как опорник.
    left = [x for x in arr if x < pivot]     # Элементы меньше опорного
    right = [x for x in arr if x > pivot]    # Элементы больше опорного
    middle = [x for x in arr if x == pivot]  # Элементы равные опорному

    # Рекурсивно сортируем левую и правую части и объединяем
    return Quick_Sort(left) + middle + Quick_Sort(right)


def Merge_Sort(arr):
    # 1. Определяем длину массива
    n = len(arr)
    if n <= 1:
        return arr
    # 2. Определить середину массива для последующего его разделения.
    mid = n // 2
    # 3. Рекурсивно делим массив на две половины и сортируем.
    left_half = Merge_Sort(arr[:mid])
    right_half = Merge_Sort(arr[mid:])
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0
    # Слияние двух отсортированных половин
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Добавляем оставшиеся элементы
    result.extend(left[i:])
    result.extend(right[j:])
    return result
