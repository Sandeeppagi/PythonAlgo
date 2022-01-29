def lcs_print(str1, str2, str1_len, str2_len):
    table = [[0 for j in range(str2_len + 1)] for i in range(str2_len + 1)]
    for i in range(str1_len + 1):
        for j in range(str2_len + 1):
            if i == 0 or j == 0:
                table[i][j] = 0

    for i in range(1, str1_len + 1):
        for j in range(1, str2_len + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1]
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    i, j = str1_len, str2_len
    lcs = ''
    while i > 0 or j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs = str1[i - 1] + lcs
            i -= 1
            j -= 1
        else:
            if table[i - 1][j] > table[i][j - 1]:
                i -= 1
            else:
                j -= 1
    return lcs


str1 = 'acbcf'
str2 = 'abcdaf'
str1_len = len(str1)
str2_len = len(str2)
print(lcs_print(str1, str2, str1_len, str2_len))
