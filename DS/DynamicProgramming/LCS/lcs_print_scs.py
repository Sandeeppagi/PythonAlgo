def solve(str1, str2, str1_len, str2_len):
    table = [[0]*(str2_len+1) for i in range(str1_len+1)]
    for i in range(1, str1_len+1):
        for j in range(1, str2_len+1):
            if str1[i-1] == str2[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    i, j = str1_len, str2_len
    scs = ''
    while i > 0 or j > 0:
        if str1[i-1] == str2[j-1]:
            scs = str1[i-1] + scs
            i -= 1
            j -= 1
        else:
            if table[i-1][j] > table[i][j-1]:
                scs = str1[i-1] + scs
                i -= 1
            else:
                scs = str2[j-1] + scs
    while i > 0:
        scs = str1[i-1] + scs
        i -= 1
    while j > 0:
        scs = str2[j-1] + scs
        j -= 1

    return scs


str1 = 'abac'
str2 = 'cab'
str1_len = len(str1)
str2_len = len(str2)
print(solve(str1, str2, str1_len, str2_len))