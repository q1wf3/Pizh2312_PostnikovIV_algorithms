"""
Сравнительный анализ жадных алгоритмов для лабораторной работы №8.
"""

import time
import itertools
from typing import List, Tuple
from greedy_algorithms import fractional_knapsack, huffman_coding


def compare_knapsack_algorithms() -> None:
    """
    Сравнение жадного алгоритма для непрерывного рюкзака
    с точным решением для дискретного рюкзака 0-1.
    """
    print("Сравнение алгоритмов для задачи о рюкзаке")
    print()

    # Тестовые данные
    items = [(2, 40), (3, 50), (5, 100), (7, 140), (1, 20)]
    capacity = 10

    print(f"Предметы (вес, стоимость): {items}")
    print(f"Вместимость рюкзака: {capacity}")
    print()

    # 1. Жадный алгоритм для непрерывного рюкзака
    start_time = time.time()
    greedy_value, greedy_items = fractional_knapsack(capacity, items)
    greedy_time = time.time() - start_time

    print("1. Жадный алгоритм (непрерывный рюкзак):")
    print(f"   Максимальная стоимость: {greedy_value:.2f}")
    print(f"   Время выполнения: {greedy_time:.6f} сек")

    # 2. Точное решение для дискретного рюкзака 0-1 (полный перебор)
    def exact_01_knapsack(
        capacity: int,
        items: List[Tuple[int, int]]
    ) -> Tuple[int, tuple]:
        """Точное решение 0-1 рюкзака полным перебором O(2^n)."""
        n = len(items)
        best_value = 0
        best_combination = None

        for r in range(1, n + 1):
            for combination in itertools.combinations(range(n), r):
                total_weight = sum(items[i][0] for i in combination)
                total_value = sum(items[i][1] for i in combination)

                if total_weight <= capacity and total_value > best_value:
                    best_value = total_value
                    best_combination = combination

        return best_value, best_combination

    start_time = time.time()
    exact_value, exact_combination = exact_01_knapsack(capacity, items)
    exact_time = time.time() - start_time

    print("\n2. Точный алгоритм (0-1 рюкзак, полный перебор):")
    print(f"   Максимальная стоимость: {exact_value}")
    print(f"   Время выполнения: {exact_time:.6f} сек")

    if exact_combination:
        print(f"   Оптимальная комбинация: {exact_combination}")

    # 3. Демонстрация случая, когда жадный алгоритм не оптимален для 0-1
    print("\nДемонстрация: когда жадный алгоритм не оптимален для 0-1")
    print()

    tricky_items = [(10, 60), (20, 100), (30, 120)]
    tricky_capacity = 50

    print(f"Предметы: {tricky_items}")
    print(f"Вместимость: {tricky_capacity}")

    # Жадный выбор (по удельной стоимости)
    print("\nЖадный выбор для 0-1 (по удельной стоимости):")
    print("   Берет предмет 1: стоимость 60, вес 10")
    print("   Остается места: 40")
    print("   Итоговая стоимость: 60")

    # Оптимальный выбор
    print("\nОптимальный выбор для 0-1:")
    print("   Берет предметы 2 и 3: стоимость 100 + 120 = 220")
    print("   Вес: 20 + 30 = 50")
    print("   Итоговая стоимость: 220")

    print("\nВывод: Жадный алгоритм не оптимален для 0-1 рюкзака.")


def measure_huffman_performance() -> None:
    """
    Базовые замеры производительности алгоритма Хаффмана.
    """
    print("\nИзмерение производительности алгоритма Хаффмана")
    print()

    # Тестовые данные
    frequencies = {'a': 0.4, 'b': 0.3, 'c': 0.2, 'd': 0.1}

    print(f"Частоты символов: {frequencies}")

    # Замер времени
    start_time = time.time()
    root, codes = huffman_coding(frequencies)
    execution_time = time.time() - start_time

    print(f"Время выполнения: {execution_time:.6f} сек")
    print("\nКоды Хаффмана:")
    for char, code in sorted(codes.items()):
        print(f"  '{char}': {code}")

    # Расчет средней длины кода
    avg_length = sum(len(code) * frequencies[char]
                     for char, code in codes.items())
    print(f"\nСредняя длина кода: {avg_length:.3f} бит/символ")


def main() -> None:
    """Основная функция для запуска анализа."""
    compare_knapsack_algorithms()
    measure_huffman_performance()


if __name__ == "__main__":
    main()
