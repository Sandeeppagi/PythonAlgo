def fib_bottom_up(number):
    table = [None] * (number + 1)
    table[0] = 0
    table[1] = 1
    if number == 0 or number == 1:
        return table[number]
    for i in range(2, number + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[number]


def fib_bottom_up_space(n):
    if n == 0:  # base cases
        return 0
    if n == 1:  # base cases
        return 1
    secondLast = 0  # base case 1, fib(0) = 0
    last = 1  # base case 2, fib(1) = 1
    current = None  # initially set to None
    for i in range(1, n):  # iterate n times to evaluate n-th fibonacci
        # storing ith fibonacci in current by summing up i-1th and i-2th fibonacci
        current = secondLast + last
        secondLast = last  # updating for next iteration
        last = current
    return current  # return the value of n in tabulation table


num = 6
print(f"Fibonacci for number {num} is {fib_bottom_up(num)}")
print(f"Fibonacci for number {num} is {fib_bottom_up_space(num)}")
