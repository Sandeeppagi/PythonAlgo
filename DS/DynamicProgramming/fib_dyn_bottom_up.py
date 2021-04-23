def fib_bottom_up(number):
    table = [None] * (number + 1)
    table[0] = 0
    table[1] = 1
    if number == 0 or number == 1:
        return table[number]
    for i in range(2, number + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[number]


num = 1000
print(f"Fibonacci for number {num} is {fib_bottom_up(num)}")
