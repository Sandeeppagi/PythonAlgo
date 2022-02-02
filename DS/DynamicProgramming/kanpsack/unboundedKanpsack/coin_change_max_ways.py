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
Sum = 6
n = len(coins)