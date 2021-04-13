def find_square(targetNumber):
    if targetNumber == 0:
        return 0
    else:
        # sum = (2 * targetNumber) - 1
        # print(sum)
        # return findSquare(targetNumber - 1) + sum
        return find_square(targetNumber - 1) + (2 * targetNumber) - 1


num = 5
print(f'Square of a number {num} is {find_square(num)}')
