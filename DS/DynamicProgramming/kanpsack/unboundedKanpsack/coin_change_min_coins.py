def solve(coins_arr, number_of_coins, total):
    INT_MAX = 2 ** 32
    table = [[0 for j in range(total + 1)] for i in range(number_of_coins + 1)]
    for j in range(total + 1):
        table[0][j] = INT_MAX - 1
        if j % coins_arr[0] == 0:
            table[1][j] = j // coins_arr[0]
        else:
            table[1][j] = INT_MAX - 1
    for i in range(2, number_of_coins + 1):
        for j in range(1, total + 1):
            if coins_arr[i - 1] <= j:
                table[i][j] = min(1 + table[i][j - coins_arr[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]
    return -1 if table[number_of_coins][total] == INT_MAX - 1 else table[number_of_coins][total]


coins_arr = [3, 10, 2]
number_of_coins = len(coins_arr)
total = 7
print(solve(coins_arr, number_of_coins, total))
