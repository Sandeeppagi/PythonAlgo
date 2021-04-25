def catalan_recursion(number):
    if number == 0:
        return 1
    sum = 0
    for i in range(number):
        sum += (catalan_recursion(i) * catalan_recursion(number - 1 - i))
    return sum


def catalan_top_down(number, memo):
    if number == 0:
        return 1
    elif number in memo:
        return memo[number]
    sum = 0
    for i in range(number):
        sum += catalan_top_down(i, memo) * catalan_top_down(number - 1 - i, memo)
    return sum


def catalan_bottom_up(number):
    table = [None] * (number + 1)
    table[0] = 1
    for i in range(1, number + 1):
        table[i] = 0
        for j in range(i):
            table[i] += (table[j] * table[i - j - 1])
    return table[number]


num = 15
# print(f"Catalan for {num} is {catalan_recursion(num)}")
# print(f"Catalan for {num} is {catalan_top_down(num, {})}")
print(f"Catalan for {num} is {catalan_bottom_up(num)}")