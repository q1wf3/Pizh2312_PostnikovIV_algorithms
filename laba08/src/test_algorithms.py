"""
Тестирование трех основных жадных алгоритмов.
"""

from greedy_algorithms import (
    interval_scheduling,
    fractional_knapsack,
    huffman_coding
)


def test_interval_scheduling() -> None:
    """Тест задачи о выборе заявок."""
    print("Тест: Задача о выборе заявок")

    intervals = [(1, 4), (3, 5), (0, 6), (5, 7),
                 (3, 8), (5, 9), (6, 10), (8, 11),
                 (8, 12), (2, 13), (12, 14)]

    result = interval_scheduling(intervals)

    print(f"Всего интервалов: {len(intervals)}")
    print(f"Выбрано интервалов: {len(result)}")
    print(f"Выбранные интервалы: {result}")

    # Проверка, что интервалы не пересекаются
    for i in range(len(result) - 1):
        assert result[i][1] <= result[i + 1][0], "Интервалы пересекаются"

    print("Проверка: интервалы не пересекаются - OK")
    print()


def test_fractional_knapsack() -> None:
    """Тест непрерывного рюкзака."""
    print("Тест: Непрерывный рюкзак")

    capacity = 50
    items = [(10, 60), (20, 100), (30, 120)]

    value, taken = fractional_knapsack(capacity, items)

    print(f"Вместимость: {capacity}")
    print(f"Предметы: {items}")
    print(f"Максимальная стоимость: {value:.2f}")

    # Проверка, что не превышена вместимость
    total_weight = sum(weight * fraction for weight, _, fraction in taken)
    assert total_weight <= capacity, "Превышена вместимость"

    print("Взятые предметы:")
    for weight, val, fraction in taken:
        print(f"  Вес: {weight}, Стоимость: {val}, Доля: {fraction:.2%}")

    print("Проверка: вместимость не превышена - OK")
    print()


def test_huffman_coding() -> None:
    """Тест алгоритма Хаффмана."""
    print("Тест: Алгоритм Хаффмана")

    frequencies = {'a': 0.4, 'b': 0.3, 'c': 0.2, 'd': 0.1}
    _, codes = huffman_coding(frequencies)

    print("Частоты символов:")
    for char, freq in sorted(frequencies.items()):
        print(f"  '{char}': {freq:.3f}")

    print("\nКоды Хаффмана:")
    for char, code in sorted(codes.items()):
        print(f"  '{char}': {code}")

    # Проверка префиксного свойства
    all_codes = list(codes.values())
    for i in range(len(all_codes)):
        for j in range(len(all_codes)):
            if i != j and all_codes[i].startswith(all_codes[j]):
                raise AssertionError("Нарушено префиксное свойство")

    print("\nПроверка: префиксное свойство выполняется - OK")

    # Расчет средней длины кода
    avg_length = sum(len(code) * frequencies[char]
                     for char, code in codes.items())
    print(f"\nСредняя длина кода: {avg_length:.3f} бит/символ")
    print()


def main() -> None:
    """Запуск всех тестов."""
    print("Тестирование жадных алгоритмов")
    print()

    test_interval_scheduling()
    test_fractional_knapsack()
    test_huffman_coding()

    print("Все тесты пройдены успешно!")


if __name__ == "__main__":
    main()
