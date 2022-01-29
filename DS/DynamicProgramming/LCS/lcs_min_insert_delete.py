def solve(str1, str2, str1_len, str2_len):
    table = [[0]*(str2_len+1) for i in range(str1_len+1)]
    for i in range(1, str1_len+1):
        for j in range(1, str2_len+1):
            if str1[i-1] == str2[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    lcs = table[str1_len][str2_len]
    insertion = str2_len - lcs
    deletions = str1_len - lcs
    return insertion + deletions

str1 = 'abcdxyz'
str2 = 'amnoyz'
str1_len = len(str1)
str2_len = len(str2)
print(solve(str1, str2, str1_len, str2_len))