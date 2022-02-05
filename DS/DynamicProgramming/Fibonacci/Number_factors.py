# Given a number ‘n’, implement a method to count how many
# possible ways there are to express ‘n’ as the sum of 1, 3, or 4.
#
# Example 1:
#
# n : 4
# Number of ways = 4
# Explanation: Following are the four ways we can express 'n' : {1,1,1,1}, {1,3}, {3,1}, {4}
# Example 2:
#
# n : 5
# Number of ways = 6
# Explanation: Following are the six ways we can express 'n' : {1,1,1,1,1}, {1,1,3}, {1,3,1}, {3,1,1},
# {1,4}, {4,1}
# Let’s first start with a recursive brute-force solution.

def count_ways(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    ways1 = count_ways(n - 1)
    ways3 = count_ways(n - 3)
    ways4 = count_ways(n - 4)

    return ways1 + ways3 + ways4


print(count_ways(4))
print(count_ways(5))
print(count_ways(6))
print('-' * 25)


def count_ways_helper(n):
    table = [0 for i in range(n + 1)]
    return count_ways_memo(n, table)


def count_ways_memo(n, table):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    if table[n] == 0:
        count1n = count_ways_memo(n - 1, table)
        count3n = count_ways_memo(n - 3, table)
        count4n = count_ways_memo(n - 4, table)
        table[n] = count1n + count3n + count4n
    return table[n]


print(count_ways_helper(4))
print(count_ways_helper(5))
print(count_ways_helper(6))
print('-' * 25)


def count_ways_bottom_up(n):
    if n <= 2:
        return 1
    if n == 3:
        return 2
    dp = [0 for i in range(n + 1)]
    dp[0], dp[1], dp[2], dp[3] = 1, 1, 1, 2
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 4]
    return dp[n]


print(count_ways_bottom_up(4))
print(count_ways_bottom_up(5))
print(count_ways_bottom_up(6))
print('-' * 25)
