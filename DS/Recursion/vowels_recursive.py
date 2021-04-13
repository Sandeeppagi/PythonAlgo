def vowels_iterative(string):
    count = 0
    for i in range(len(string)):
        count += is_vowels(string[i])
    return count


def vowels_recursive(string, length):
    if length == 0:
        return is_vowels(string)
    # count = is_vowels(string[length - 1])
    # return vowels_recursive(string, length - 1) + count
    return vowels_recursive(string, length - 1) + is_vowels(string[length - 1])


def is_vowels(character):
    character = character.lower()
    vowels = 'aeiou'
    if character in vowels:
        return 1
    else:
        return 0


my_str = 'what a evening'
print(f"Number of vowels in string using iterative {vowels_iterative(my_str)}")
print(f"Number of vowels in string using recursive {vowels_recursive(my_str, len(my_str))}")
