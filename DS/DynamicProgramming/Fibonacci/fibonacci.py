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

