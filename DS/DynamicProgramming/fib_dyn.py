memo = {}


def fib_dyn(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    elif number in memo:
        return memo[number]
    else:
        memo[number] = fib_dyn(number - 1) + fib_dyn(number - 2)
        return memo[number]


num = 8
print(f"Print the fibonacci for number {num} : {fib_dyn(num)}")
