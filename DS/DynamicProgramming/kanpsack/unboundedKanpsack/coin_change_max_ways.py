def coinChange(coins, n, Sum):
    if Sum == 0:
        return 1
    if n == 0:
        return 0

    if coins[n - 1] <= Sum:
        return coinChange(coins, n, Sum - coins[n - 1]) + coinChange(coins, n - 1, Sum)
    else:
        return coinChange(coins, n - 1, Sum)


coins = [1, 2, 3]
Sum = 5
n = len(coins)
print(coinChange(coins, n, Sum))
print('-' * 5)

memo = [[-1] * (Sum + 1) for i in range(n + 1)]


def coinChange_memo(coins, n, Sum):
    if Sum == 0:
        return 1
    if n == 0:
        return 0

    if memo[n][Sum] != -1:
        return memo[n][Sum]

    if coins[n - 1] <= Sum:
        memo[n][Sum] = coinChange_memo(coins, n, Sum - coins[n - 1]) + coinChange_memo(coins, n - 1, Sum)
    else:
        memo[n][Sum] = coinChange_memo(coins, n - 1, Sum)
    return memo[n][Sum]


coins = [1, 2, 3]
Sum = 5
n = len(coins)
print(coinChange_memo(coins, n, Sum))
print('-' * 5)


def coinChange_Top_down(coins, n, total):
    if total < 0:
        return 0
    table = [[0] * (total + 1) for i in range(n + 1)]
    for i in range(n + 1):
        table[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, total + 1):
            if coins[i - 1] <= j:
                table[i][j] = table[i][j - coins[i - 1]] + table[i - 1][j]
            else:
                table[i][j] = table[i - 1][j]
    print(table)
    return table[n][total]


coins = [1, 2, 3]
Sum = 5
n = len(coins)
print(coinChange_Top_down(coins, n, Sum))
print('-' * 5)
