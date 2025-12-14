"""
Реализация трех жадных алгоритмов для лабораторной работы №8.
"""

from typing import List, Tuple, Dict
import heapq


def interval_scheduling(
    intervals: List[Tuple[int, int]]
) -> List[Tuple[int, int]]:
    """
    Задача о выборе заявок (Interval Scheduling).

    Сложность: O(n log n) - сортировка по времени окончания.

    Args:
        intervals: список интервалов (начало, конец)

    Returns:
        список выбранных интервалов
    """
    # Сортируем по времени окончания O(n log n)
    sorted_intervals = sorted(intervals, key=lambda x: x[1])

    selected = []
    last_end = -float('inf')

    # Жадный выбор: всегда берем интервал с наименьшим временем окончания
    for start, end in sorted_intervals:
        if start >= last_end:  # Если интервал не пересекается
            selected.append((start, end))
            last_end = end

    return selected


def fractional_knapsack(
    capacity: float,
    items: List[Tuple[float, float]]
) -> Tuple[float, List[Tuple[float, float, float]]]:
    """
    Непрерывный рюкзак (Fractional Knapsack).

    Сложность: O(n log n) - сортировка по удельной стоимости.

    Args:
        capacity: вместимость рюкзака
        items: список предметов (вес, стоимость)

    Returns:
        (максимальная стоимость, список взятых предметов с долями)
    """
    # Рассчитываем удельную стоимость O(n)
    items_with_ratio = [(weight, value, value / weight)
                        for weight, value in items]

    # Сортируем по удельной стоимости (убывание) O(n log n)
    items_sorted = sorted(items_with_ratio,
                          key=lambda x: x[2],
                          reverse=True)

    total_value = 0.0
    taken_items = []
    remaining_capacity = capacity

    # Жадный выбор: берем предметы с наибольшей удельной стоимостью
    for weight, value, ratio in items_sorted:
        if remaining_capacity <= 0:
            break

        if weight <= remaining_capacity:
            # Берем целиком
            taken_items.append((weight, value, 1.0))
            total_value += value
            remaining_capacity -= weight
        else:
            # Берем часть
            fraction = remaining_capacity / weight
            taken_items.append((weight, value, fraction))
            total_value += value * fraction
            remaining_capacity = 0

    return total_value, taken_items


class HuffmanNode:
    """Узел дерева Хаффмана."""

    def __init__(self, char: str = None, freq: float = 0.0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        return self.freq < other.freq


def huffman_coding(
    frequencies: Dict[str, float]
) -> Tuple['HuffmanNode', Dict[str, str]]:
    """
    Алгоритм Хаффмана для оптимального префиксного кодирования.

    Сложность: O(n log n) - работа с двоичной кучей.

    Args:
        frequencies: словарь {символ: частота}

    Returns:
        (корень дерева, словарь кодов)
    """
    # Создаем кучу из узлов O(n)
    heap = []
    for char, freq in frequencies.items():
        node = HuffmanNode(char, freq)
        heapq.heappush(heap, (freq, node))

    # Строим дерево Хаффмана O(n log n)
    while len(heap) > 1:
        # Извлекаем два узла с наименьшими частотами
        freq1, node1 = heapq.heappop(heap)
        freq2, node2 = heapq.heappop(heap)

        # Создаем новый узел
        merged = HuffmanNode(None, freq1 + freq2)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, (freq1 + freq2, merged))

    # Получаем корень дерева
    _, root = heapq.heappop(heap)

    # Генерируем коды O(n)
    codes = {}

    def _generate_codes(node: HuffmanNode, code: str = "") -> None:
        """Рекурсивная генерация кодов."""
        if node is None:
            return

        if node.char is not None:  # Лист
            codes[node.char] = code
            return

        _generate_codes(node.left, code + "0")
        _generate_codes(node.right, code + "1")

    _generate_codes(root)
    return root, codes


def main() -> None:
    """Основная функция для демонстрации работы алгоритмов."""
    print("Демонстрация работы жадных алгоритмов")
    print()

    # 1. Демонстрация Interval Scheduling
    print("1. Задача о выборе заявок:")
    intervals = [(1, 4), (3, 5), (0, 6), (5, 7)]
    result = interval_scheduling(intervals)
    print(f"   Интервалы: {intervals}")
    print(f"   Выбраны: {result}")
    print(f"   Всего выбрано: {len(result)} интервалов")
    print()

    # 2. Демонстрация Fractional Knapsack
    print("2. Непрерывный рюкзак:")
    capacity = 50
    items = [(10, 60), (20, 100), (30, 120)]
    value, taken = fractional_knapsack(capacity, items)
    print(f"   Вместимость: {capacity}")
    print(f"   Предметы: {items}")
    print(f"   Максимальная стоимость: {value:.2f}")
    print()

    # 3. Демонстрация Huffman Coding
    print("3. Алгоритм Хаффмана:")
    frequencies = {'a': 0.4, 'b': 0.3, 'c': 0.2, 'd': 0.1}
    root, codes = huffman_coding(frequencies)
    print(f"   Частоты: {frequencies}")
    print(f"   Коды: {codes}")
    print()

    print("Все алгоритмы реализованы и готовы к использованию.")


if __name__ == "__main__":
    main()
