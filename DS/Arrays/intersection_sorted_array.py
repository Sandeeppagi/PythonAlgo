def intersection_using_build_in_function(A, B):
    """
    Given two sorted arrays, A and B, determine their intersection. What elements are common to A and B?
    :param A:
    :param B:
    """
    print(set(A).intersection(B))


def intersection_sorted_array(A, B):
    i = 0
    j = 0
    my_intersection = []

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                my_intersection.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(my_intersection)


A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

intersection_using_build_in_function(A, B)
intersection_sorted_array(A, B)
