def solve_knapsack(weight, price, capacity, current_index, memo):
    if capacity <= 0 or current_index >= len(weight):
        return 0

    if (capacity, current_index) in memo:
        return memo[(capacity, current_index)]

    if weight[current_index] > capacity:
        memo[(capacity, current_index)] = solve_knapsack(weight, price, capacity, current_index + 1, memo)
        return memo[(capacity, current_index)]

    price1 = price[current_index] + \
             solve_knapsack(weight, price, capacity - weight[current_index], current_index + 1, memo)
    price2 = solve_knapsack(weight, price, capacity, current_index + 1, memo)
    memo[(capacity, current_index)] = max(price1, price2)
    return memo[(capacity, current_index)]


def knapsack(weight, price, capacity):
    memo = {}
    return solve_knapsack(weight, price, capacity, 0, memo)


print(knapsack([2, 1, 1, 3], [2, 8, 1, 10], 4))
