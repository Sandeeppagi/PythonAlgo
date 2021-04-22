def factorial(number):
    table = [0] * (number + 1)
    table[0] = 1
    for i in range(1, number + 1):
        table[i] = table[i - 1] * i
    return table[number]


def factorial_recursion(number):
    if number == 0:
        return 1
    return factorial_recursion(number - 1) * number


num = 5
print(f"Factorial of {num} is {factorial(num)}")
print(f"Factorial of {num} using recursion is {factorial_recursion(num)}")
