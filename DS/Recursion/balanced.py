def balanced(array, current_index=0, open_bracket_no=0):
    if len(array) % 2 == 1:
        return False

    # Base case1 and 2
    if current_index == len(array):
        return open_bracket_no == 0

    # Base case3
    if open_bracket_no < 0:  # A closing bracket did not find its corresponding opening bracket
        return False

    # Recursive case1
    if array[current_index] == "(":
        return balanced(array, current_index + 1, open_bracket_no + 1)

    # Recursive case2
    elif array[current_index] == ")":
        return balanced(array, current_index + 1, open_bracket_no - 1)


# Driver Code
arr = ["(", "(", ")", ")", "(", ")"]
print(f"Is array {arr} balanced : {balanced(arr)}")
