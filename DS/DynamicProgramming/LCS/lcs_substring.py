def lc_substring(str1, str2, str1_len, str2_len):
    table = [[0 for j in range(str2_len+1)] for i in range(str1_len+1)]
    res = 0
    for i in range(str1_len+1):
        for j in range(str2_len+1):
            if i == 0 or j == 0:
                table[i][j] = 0
    for i in range(1, str1_len+1):
        for j in range(1, str2_len+1):
            if str1[i-1] == str2[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
                res = max(res, table[i][j])
            else:
                table[i][j] = 0
    return res

str1 = 'abcdxyz'
str2 = 'xyzabcd'
str1_len = len(str1)
str2_len = len(str2)

print('lc Substring', lc_substring(str1, str2, str1_len, str2_len))