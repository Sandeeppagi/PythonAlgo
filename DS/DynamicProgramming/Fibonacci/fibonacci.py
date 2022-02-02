def fibonacci(num):
    if num == 0 or num == 1:
        return num
    temp = fibonacci(num-1) + fibonacci(num-2)
    return temp

print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(6))
print(fibonacci(7))

def help_memo(num):
    arr = [-1 for i in range(num+1)]
    return fibonacci_memo(num, arr)

def fibonacci_memo(num, arr):
    if num == 0 or num == 1:
        return num
    if arr[num] != -1:
        return arr[num]
    arr[num] = fibonacci_memo(num-1, arr) + fibonacci_memo(num-2, arr)
    return arr[num]

print(help_memo(3))
print(help_memo(4))
print(help_memo(6))
print(help_memo(7))


def fibonacci_bottom_up(num):
    if num == 0 or num == 1:
        return num
    dp = [0, 1]
    for i in range(2, num + 1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[num]

print(fibonacci_bottom_up(3))
print(fibonacci_bottom_up(4))
print(fibonacci_bottom_up(6))
print(fibonacci_bottom_up(7))

def fibonacci_bottom_up_v2(num):
    if num == 0 or num == 1:
        return num
    n1, n2, temp = 0, 1, 0
    for i in range(2, num+1):
        temp = n1 + n2
        n1 = n2
        n2 = temp
    return n2

print(fibonacci_bottom_up_v2(3))
print(fibonacci_bottom_up_v2(4))
print(fibonacci_bottom_up_v2(6))
print(fibonacci_bottom_up_v2(7))

