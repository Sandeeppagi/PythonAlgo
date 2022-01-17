wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 8
n = len(wt)
print(n)
# Create matrix to store the values W for columns and n is rows
table = [[-1 for j in range(W + 1)] for i in range(n + 1)]
print(table)


def knapsack(wt, val, W, n):
    if n == 0 or W == 0:
        return 0
    if table[n][W] != -1:
        return table[n][W]

    if wt[n - 1] <= W:
        table[n][W] = max(val[n - 1] + knapsack(wt, val, W - wt[n - 1], n - 1), knapsack(wt, val, W, n - 1))
        return table[n][W]
    else:
        table[n][W] = knapsack(wt, val, W, n - 1)
        return table[n][W]


print(knapsack(wt, val, W, n))
