# Problem Statement#
# Given a stair with ‘n’ steps, implement a method to count how many possible ways are there to reach the top of the staircase,
# given that, at every step you can either take 1 step, 2 steps, or 3 steps.

# Example 1:
# Number of stairs (n) : 3
# Number of ways = 4
# Explanation: Following are the four ways we can climb : {1,1,1}, {1,2}, {2,1}, {3}

# Example 2:
# Number of stairs (n) : 4
# Number of ways = 7
# Explanation: Following are the seven ways we can climb : {1,1,1,1}, {1,1,2}, {1,2,1}, {2,1,1},
# {2,2}, {1,3}, {3,1}

def staircase(number_of_stairs):
    if number_of_stairs == 0:
        return 0
    if number_of_stairs == 1:
        return 1
    if number_of_stairs == 2:
        return 2
    if number_of_stairs == 3:
        return 4
    step1Count = staircase(number_of_stairs - 1)
    step2Count = staircase(number_of_stairs - 2)
    step3Count = staircase(number_of_stairs - 3)
    return step1Count + step2Count + step3Count


print(staircase(0))
print(staircase(1))
print(staircase(2))
print(staircase(3))
print(staircase(4))
print(staircase(5))
print(staircase(6))
print('-' * 5)


def memo_helper(number_of_stairs):
    table = [0 for i in range(number_of_stairs + 1)]
    return staircase_memo(table, number_of_stairs)


def staircase_memo(table, number_of_stairs):
    if number_of_stairs == 0:
        return 0
    if number_of_stairs == 1:
        return 1
    if number_of_stairs == 2:
        return 2
    if number_of_stairs == 3:
        return 4
    if table[number_of_stairs] == 0:
        step1Count = staircase(number_of_stairs - 1)
        step2Count = staircase(number_of_stairs - 2)
        step3Count = staircase(number_of_stairs - 3)
        table[number_of_stairs] = step1Count + step2Count + step3Count
    return table[number_of_stairs]


print(memo_helper(0))
print(memo_helper(1))
print(memo_helper(2))
print(memo_helper(3))
print(memo_helper(4))
print(memo_helper(5))
print(memo_helper(6))
print('-' * 5)


def staircase_bottom_up(number_of_stairs):
    if number_of_stairs == 0:
        return 0
    if number_of_stairs == 1:
        return 1
    if number_of_stairs == 2:
        return 2
    if number_of_stairs == 3:
        return 4
    dp = [0 for i in range(number_of_stairs + 1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, number_of_stairs + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[number_of_stairs]


print(staircase_bottom_up(0))
print(staircase_bottom_up(1))
print(staircase_bottom_up(2))
print(staircase_bottom_up(3))
print(staircase_bottom_up(4))
print(staircase_bottom_up(5))
print(staircase_bottom_up(6))
print('-' * 5)
