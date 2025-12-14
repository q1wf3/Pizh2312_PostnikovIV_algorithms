"""
Тестирование алгоритмов динамического программирования.
"""

from dynamic_programming import (
    fibonacci_memoization,
    fibonacci_tabulation,
    knapsack_01_tabulation,
    lcs_tabulation,
    coin_change_dp,
    longest_increasing_subsequence
)


def test_fibonacci() -> None:
    """Тест чисел Фибоначчи."""
    print("Тест: Числа Фибоначчи")

    test_cases = [
        (0, 0),
        (1, 1),
        (5, 5),
        (10, 55)
    ]

    for n, expected in test_cases:
        result_memo = fibonacci_memoization(n)
        result_tab = fibonacci_tabulation(n)

        assert result_memo == expected, f"Мемоизация: F({n}) = {result_memo}"
        assert result_tab == expected, f"Табличный: F({n}) = {result_tab}"

        print(f"  F({n}) = {result_tab} - OK")

    print("Все тесты пройдены")
    print()


def test_knapsack() -> None:
    """Тест задачи о рюкзаке 0-1."""
    print("Тест: Задача о рюкзаке 0-1")

    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5

    max_value, items = knapsack_01_tabulation(weights, values, capacity)

    print(f"  Предметы: вес={weights}, стоимость={values}")
    print(f"  Вместимость: {capacity}")
    print(f"  Макс. стоимость: {max_value}")
    print(f"  Выбранные предметы: {items}")

    # Проверка, что вес не превышает вместимость
    total_weight = sum(weights[i] for i in items)
    assert total_weight <= capacity, f"Вес {total_weight} > {capacity}"

    print("  Проверка веса: OK")
    print()


def test_lcs() -> None:
    """Тест наибольшей общей подпоследовательности."""
    print("Тест: Наибольшая общая подпоследовательность")

    test_cases = [
        ("ABC", "ABC", 3, "ABC"),
        ("ABCDGH", "AEDFHR", 3, "ADH"),
        ("AGGTAB", "GXTXAYB", 4, "GTAB")
    ]

    for s1, s2, expected_len, expected_lcs in test_cases:
        length, lcs_str = lcs_tabulation(s1, s2)

        assert length == expected_len, (
            f"Длина: {length} != {expected_len}"
        )
        assert lcs_str == expected_lcs, (
            f"LCS: '{lcs_str}' != '{expected_lcs}'"
        )

        print(f"  '{s1}' & '{s2}' -> '{lcs_str}' (длина {length}) - OK")

    print()


def test_coin_change() -> None:
    """Тест размена монет."""
    print("Тест: Размен монет")

    coins = [1, 5, 10, 25]
    amount = 63

    num_coins, coin_list = coin_change_dp(coins, amount)

    print(f"  Монеты: {coins}")
    print(f"  Сумма: {amount}")
    print(f"  Количество монет: {num_coins}")
    print(f"  Комбинация: {coin_list}")

    # Проверка суммы
    total = sum(coin_list)
    assert total == amount, f"Сумма {total} != {amount}"
    assert len(coin_list) == num_coins, "Количество не совпадает"

    print("  Проверка суммы: OK")
    print()


def test_lis() -> None:
    """Тест наибольшей возрастающей подпоследовательности."""
    print("Тест: Наибольшая возрастающая подпоследовательность")

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    length, subsequence = longest_increasing_subsequence(nums)

    print(f"  Последовательность: {nums}")
    print(f"  Длина LIS: {length}")
    print(f"  LIS: {subsequence}")

    # Проверка, что подпоследовательность возрастающая
    for i in range(len(subsequence) - 1):
        assert subsequence[i] < subsequence[i + 1], "Не возрастает"

    print("  Проверка возрастания: OK")
    print()


def main() -> None:
    """Запуск всех тестов."""
    print("Тестирование алгоритмов ДП")
    print()

    test_fibonacci()
    test_knapsack()
    test_lcs()
    test_coin_change()
    test_lis()

    print("Все тесты успешно пройдены!")


if __name__ == "__main__":
    main()
