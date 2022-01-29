def solve(str1, str2, str1_len, str2_len):
    table = [[0]*(str2_len+1) for i in range(str1_len+1)]
    for i in range(1, str1_len+1):
        for j in range(1, str2_len+1):
            if str1[i-1] == str2[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    return str1_len + str2_len - table[str1_len][str2_len]


str1 = 'AGGTAB'
str2 = 'GXTXAYB'
str1_len = len(str1)
str2_len = len(str2)
print(solve(str1, str2, str1_len, str2_len))