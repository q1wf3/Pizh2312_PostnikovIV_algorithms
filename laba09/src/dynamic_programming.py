"""
Реализация алгоритмов динамического программирования.
"""

from typing import List, Tuple


def fibonacci_naive(n: int) -> int:
    """
    Наивная рекурсивная реализация чисел Фибоначчи.

    Сложность: O(2^n) - экспоненциальная.
    """
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


def fibonacci_memoization(n: int) -> int:
    """
    Числа Фибоначчи с мемоизацией (нисходящий подход).

    Сложность: O(n) - линейная.
    """
    memo = {}

    def fib(k: int) -> int:
        if k <= 1:
            return k
        if k not in memo:
            memo[k] = fib(k - 1) + fib(k - 2)
        return memo[k]

    return fib(n)


def fibonacci_tabulation(n: int) -> int:
    """
    Числа Фибоначчи с табличным подходом (восходящий).

    Сложность: O(n) - линейная, память O(1).
    """
    if n <= 1:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


def knapsack_01_tabulation(
    weights: List[int],
    values: List[int],
    capacity: int
) -> Tuple[int, List[int]]:
    """
    Задача о рюкзаке 0-1 (восходящий подход).

    Сложность: O(n * W) время, O(n * W) память.
    где n - количество предметов, W - вместимость.
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], selected_items[::-1]


def knapsack_01_memoization(
    weights: List[int],
    values: List[int],
    capacity: int
) -> int:
    """
    Задача о рюкзаке 0-1 с мемоизацией (нисходящий подход).

    Сложность: O(n * W) время, O(n * W) память.
    """
    n = len(weights)
    memo = {}

    def knapsack(i: int, w: int) -> int:
        if i == 0 or w == 0:
            return 0

        if (i, w) in memo:
            return memo[(i, w)]

        if weights[i - 1] > w:
            result = knapsack(i - 1, w)
        else:
            result = max(
                knapsack(i - 1, w),
                values[i - 1] + knapsack(i - 1, w - weights[i - 1])
            )

        memo[(i, w)] = result
        return result

    return knapsack(n, capacity)


def lcs_tabulation(s1: str, s2: str) -> Tuple[int, str]:
    """
    Наибольшая общая подпоследовательность (восходящий подход).

    Сложность: O(m * n) время, O(m * n) память.
    где m, n - длины строк.
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_chars = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_chars.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], ''.join(reversed(lcs_chars))


def coin_change_dp(
    coins: List[int],
    amount: int
) -> Tuple[int, List[int]]:
    """
    Размен монет (минимальное количество монет для суммы).

    Сложность: O(n * amount) время, O(amount) память.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    if dp[amount] == float('inf'):
        return -1, []

    result_coins = []
    remaining = amount
    while remaining > 0:
        coin = coin_used[remaining]
        result_coins.append(coin)
        remaining -= coin

    return dp[amount], result_coins


def longest_increasing_subsequence(nums: List[int]) -> Tuple[int, List[int]]:
    """
    Наибольшая возрастающая подпоследовательность.

    Сложность: O(n^2) время, O(n) память.
    """
    if not nums:
        return 0, []

    n = len(nums)
    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_len = max(dp)
    max_idx = dp.index(max_len)

    lis = []
    idx = max_idx
    while idx >= 0:
        lis.append(nums[idx])
        idx = prev[idx]

    return max_len, lis[::-1]


def main() -> None:
    """Демонстрация работы алгоритмов."""
    print("Демонстрация алгоритмов динамического программирования")
    print()

    print("1. Числа Фибоначчи:")
    n = 10
    print(f"   F({n}) = {fibonacci_tabulation(n)}")
    print()

    print("2. Задача о рюкзаке 0-1:")
    weights = [2, 3, 5, 7, 1]
    values = [40, 50, 100, 140, 20]
    capacity = 10
    max_value, items = knapsack_01_tabulation(weights, values, capacity)
    print(f"   Предметы: вес={weights}, стоимость={values}")
    print(f"   Вместимость: {capacity}")
    print(f"   Макс. стоимость: {max_value}")
    print(f"   Выбранные предметы: {items}")
    print()

    print("3. Наибольшая общая подпоследовательность:")
    s1, s2 = "ABCBDAB", "BDCAB"
    lcs_len, lcs_str = lcs_tabulation(s1, s2)
    print(f"   Строка 1: '{s1}'")
    print(f"   Строка 2: '{s2}'")
    print(f"   Длина LCS: {lcs_len}")
    print(f"   LCS: '{lcs_str}'")
    print()

    print("4. Размен монет:")
    coins = [1, 5, 10, 25]
    amount = 63
    num_coins, coin_list = coin_change_dp(coins, amount)
    print(f"   Монеты: {coins}")
    print(f"   Сумма: {amount}")
    print(f"   Минимальное количество монет: {num_coins}")
    print(f"   Комбинация: {coin_list}")


if __name__ == "__main__":
    main()
