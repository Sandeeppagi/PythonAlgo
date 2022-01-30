def solve(str1):
    str1_len = len(str1)
    table = [[0] * (str1_len + 1) for i in range(str1_len + 1)]
    for i in range(str1_len + 1):
        for j in range(str1_len + 1):
            if str1[i - 1] == str1[j - 1] and i != j:
                table[i][j] = 1 + table[i - 1][j - 1]
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    len_LRS = table[str1_len][str1_len]
    print(len_LRS)
    lrs_str = ''
    i, j = str1_len, str1_len
    while i > 0 or j > 0:
        if str1[i - 1] == str1[j - 1] and i != j:
            lrs_str = str1[i - 1] + lrs_str
            i -= 1
            j -= 1
        else:
            # if table[i-1][j] > table[i][j-1]:
            #     i -= 1
            # else:
            #     j -= 1

            if table[i][j-1] > table[i-1][j]:
                j -= 1
            else:
                i -= 1
    return lrs_str


str1 = 'aabebcdd'
print(solve(str1))
