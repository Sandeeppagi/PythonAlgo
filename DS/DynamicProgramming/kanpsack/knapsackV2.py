def knapsack(wt, val, W, n):
    # Base condition
    if n == 0 or W == 0:
        return 0
    # Choice Diagram
    if wt[n - 1] <= W:
        return max(val[n - 1] + knapsack(wt, val, W - wt[n - 1], n - 1), knapsack(wt, val, W, n - 1))
    else:
        return knapsack(wt, val, W, n - 1)


wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 7
n = len(wt)
print(knapsack(wt, val, W, n))
