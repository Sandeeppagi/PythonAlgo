def find_product(lst):
    result = []
    left_product = 1
    for i in range(len(lst)):
        current_product = 1
        for item in lst[i + 1:]:
            current_product = current_product * item
        result.append(current_product * left_product)
        left_product = left_product * lst[i]
    return result


def find_product_v2(lst):
    product = []
    left_product = 1
    right_product = 1
    for ele in lst:
        product.append(left_product)
        left_product = left_product * ele
    for i in range(len(lst) -1, -1, -1):
        product[i] = product[i] * right_product
        right_product = right_product * lst[i]
    return product


print(find_product([1, 2, 3, 4]))
print(find_product_v2([1, 2, 3, 4]))
