def is_palindrome_permutation(my_str):
    my_str = my_str.replace(" ", "")
    my_str = my_str.lower()

    odd_count = 0
    ht = dict()
    for i in my_str:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    print(ht)

    for k, v in ht.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True


palin_perm = "Tact Coa"
not_palin_perm = "This is not a palindrome permutation"
print(is_palindrome_permutation(palin_perm))
print(is_palindrome_permutation(not_palin_perm))
