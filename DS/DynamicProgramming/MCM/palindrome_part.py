def is_palindrome(string):
    return string == string[::-1]


def solve(str, i, j):
    if i >= j or is_palindrome(str[i:j + 1]):
        return 0

    min_val = 2 ** 32
    for k in range(i, j):
        temp = solve(str, i, k) + solve(str, k + 1, j) + 1
        min_val = min(min_val, temp)
    return min_val


string = 'ababbc'
n = len(string)
print(solve(string, 0, n - 1))

table = [[-1] * (n + 1) for i in range(n + 1)]


def solve_memo(str, i, j):
    if i >= j or is_palindrome(str[i:j + 1]):
        return 0
    if table[i][j] != -1:
        return table[i][j]
    min_val = 2 ** 32
    for k in range(i, j):
        temp = solve(str, i, k) + solve(str, k + 1, j) + 1
        min_val = min(min_val, temp)
        table[i][j] = min_val
    return table[i][j]


print(solve_memo(string, 0, n - 1))
