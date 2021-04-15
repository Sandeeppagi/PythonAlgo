def sum_of_numbers(num):
    if num == 1:
        return 1
    else:
        return num + sum_of_numbers(num - 1)


num = 5
print(f"Summation of {num} is {sum_of_numbers(num)}")
