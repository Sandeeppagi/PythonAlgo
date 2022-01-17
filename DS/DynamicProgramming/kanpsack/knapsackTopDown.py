wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 8
n = len(wt)
print(n)


# Create matrix to store the values W for columns and n is rows
# table = [[-1 for j in range(W + 1)] for i in range(n + 1)]
# print(table)

def knapsack(wt, val, W, n):
    table = [[0 for j in range(W + 1)] for i in range(n + 1)]
    print(table)

    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif wt[i-1] <= j:
                table[i][j] = max(val[i-1] + table[i-1][j-wt[i-1]], table[i-1][j])
            else:
                table[i][j] = table[i-1][j]
    return table[n][W]

print(knapsack(wt, val, W, n))