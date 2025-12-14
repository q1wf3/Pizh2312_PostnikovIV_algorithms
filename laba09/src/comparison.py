"""
Сравнительный анализ подходов динамического программирования.
"""

import time
from dynamic_programming import (
    fibonacci_naive,
    fibonacci_memoization,
    fibonacci_tabulation,
    knapsack_01_tabulation,
    knapsack_01_memoization
)


def compare_fibonacci_approaches() -> None:
    """
    Сравнение времени работы разных подходов для чисел Фибоначчи.
    """
    print("Сравнение подходов для чисел Фибоначчи")
    print()

    test_values = [10, 20, 30, 40]

    for n in test_values:
        print(f"n = {n}:")

        if n <= 30:
            start = time.time()
            result = fibonacci_naive(n)
            naive_time = time.time() - start
            print(f"  Наивная рекурсия: {result} ({naive_time:.6f} сек)")
        else:
            print("  Наивная рекурсия: слишком долго")

        start = time.time()
        result = fibonacci_memoization(n)
        memo_time = time.time() - start
        print(f"  Мемоизация: {result} ({memo_time:.6f} сек)")

        start = time.time()
        result = fibonacci_tabulation(n)
        tab_time = time.time() - start
        print(f"  Табличный: {result} ({tab_time:.6f} сек)")
        print()


def compare_knapsack_approaches() -> None:
    """
    Сравнение нисходящего и восходящего подходов для рюкзака.
    """
    print("Сравнение подходов для задачи о рюкзаке 0-1")
    print()

    weights = [2, 3, 5, 7, 1, 4, 6, 8, 9, 2]
    values = [40, 50, 100, 140, 20, 60, 120, 160, 180, 30]
    capacity = 15

    print(f"Предметов: {len(weights)}")
    print(f"Вместимость: {capacity}")
    print()

    start = time.time()
    result_tab, items_tab = knapsack_01_tabulation(
        weights, values, capacity
    )
    tab_time = time.time() - start
    print("Восходящий подход (табличный):")
    print(f"  Время: {tab_time:.6f} сек")
    print(f"  Макс. стоимость: {result_tab}")
    print(f"  Выбрано предметов: {len(items_tab)}")
    print()

    start = time.time()
    result_memo = knapsack_01_memoization(weights, values, capacity)
    memo_time = time.time() - start
    print("Нисходящий подход (мемоизация):")
    print(f"  Время: {memo_time:.6f} сек")
    print(f"  Макс. стоимость: {result_memo}")
    print()

    print("Сравнение времени:")
    print(f"  Восходящий: {tab_time:.6f} сек")
    print(f"  Нисходящий: {memo_time:.6f} сек")
    if tab_time < memo_time:
        print("  Вывод: Восходящий подход быстрее")
    else:
        print("  Вывод: Нисходящий подход быстрее")


def analyze_scalability() -> None:
    """
    Анализ масштабируемости алгоритмов ДП.
    """
    print("Анализ масштабируемости алгоритмов ДП")
    print()

    sizes = [5, 10, 15, 20]
    capacity = 30

    print("Зависимость времени от количества предметов (рюкзак):")
    print(f"Вместимость фиксирована: {capacity}")
    print()

    for size in sizes:
        weights = list(range(1, size + 1))
        values = [w * 10 for w in weights]

        start = time.time()
        knapsack_01_tabulation(weights, values, capacity)
        elapsed = time.time() - start

        print(f"  {size} предметов: {elapsed:.6f} сек")


def main() -> None:
    """Основная функция для запуска сравнений."""
    compare_fibonacci_approaches()
    compare_knapsack_approaches()
    analyze_scalability()


if __name__ == "__main__":
    main()
