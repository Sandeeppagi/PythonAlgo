def two_sum_brute_force(A, target):
    """
    Given an array of integers, return True or False if the array has two numbers that add up to a specific target.
    You may assume that each input would have exactly one solution.
    :param A:
    :param target:
    """
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            if A[i] + A[j] == target:
                print(f'Found the numbers {A[i]}, {A[j]} whose sum is {target}')
                break


def two_sum_hash_table(A, target):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(f'Found the numbers {ht[A[i]]}, {A[i]} whose sum is {target}')
            return
        else:
            ht[target - A[i]] = A[i]
    print('Number of not found')

def sorted_array_two_sum(A, target):
    i = 0
    j = len(A)-1
    while i < j:
        if A[i] + A[j] == target:
            print(f'Found the numbers {A[i]}, {A[j]} whose sum is {target}')
            break
        elif A[i] + A[j] > target:
            j -= 1
        else:
            i += 1


A = [-1, 0, 1, 2, 4, 7, 11]
print('-' * 30)
print('Brute Force')
two_sum_brute_force(A, 13)
two_sum_brute_force(A, 7)
sorted_array_two_sum(A, 17)
print('-' * 30)
print('Hash Table')
two_sum_hash_table(A, 13)
two_sum_hash_table(A, 7)
two_sum_hash_table(A, 17)
print('-' * 30)
print('Sorted Array sum')
sorted_array_two_sum(A, 13)
sorted_array_two_sum(A, 7)
sorted_array_two_sum(A, 17)
