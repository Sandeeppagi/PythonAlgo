def print_pascal_v1(testVariable):
    if testVariable == 0:
        return [1]
    elif testVariable == 1:
        return [1, 1]
    else:
        array = print_pascal_v1(testVariable - 1)
        print(array)
        max_index = testVariable - 1
        while max_index >= 1:
            value = array[max_index - 1] + array[max_index]
            array[max_index] = value
            max_index -= 1
        array.append(1)
    return array


def print_pascal_v2(testVariable):
    # Base Case
    if testVariable == 0:
        return [1]
    else:
        line = [1]
        # Recursive Case
        previousLine = print_pascal_v2(testVariable - 1)
        for i in range(len(previousLine) - 1):
            line.append(previousLine[i] + previousLine[i + 1])
        line += [1]
    return line


n = 5
print(f"Pascal triangle for number {n} is {print_pascal_v1(n)}")
print(f"Pascal triangle for number {n} is {print_pascal_v2(n)}")
