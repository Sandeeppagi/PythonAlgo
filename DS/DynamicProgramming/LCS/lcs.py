def lcs(str1, str2, str1_len, str2_len):
    # Base condition
    if str1_len == 0 or str2_len == 0:
        return 0
    # Choice Diagram
    if str1[str1_len - 1] == str2[str2_len - 1]:
        return 1 + lcs(str1, str2, str1_len - 1, str2_len - 1)
    else:
        return max(lcs(str1, str2, str1_len - 1, str2_len), lcs(str1, str2, str1_len, str2_len - 1))


def lcs_recursive_v2(str1, str2, str1_idx, str2_idx):
    # Base condition
    if str1_idx == len(str1) or str2_idx == len(str2):
        return 0
    # Choice Diagram
    if str1[str1_idx] == str2[str2_idx]:
        return 1 + lcs_recursive_v2(str1, str2, str1_idx + 1, str2_idx + 1)
    else:
        return max(lcs_recursive_v2(str1, str2, str1_idx + 1, str2_idx),
                   lcs_recursive_v2(str1, str2, str1_idx, str2_idx + 1))

str1 = 'abcdfejgh'
str2 = 'bdekihjl'
str1_len = len(str1)
str2_len = len(str2)

table_top_down = [[-1 for i in range(str2_len + 1)] for j in range(str1_len + 1)]
def lcs_top_down(str1, str2, str1_len, str2_len):
    # Base case
    if str1_len == 0 or str2_len == 0:
        return 0
    # Check if values exists
    if table_top_down[str1_len][str2_len] != -1:
        return table_top_down[str1_len][str2_len]
    # Choice diagram
    if str1[str1_len - 1] == str2[str2_len - 1]:
        table_top_down[str1_len][str2_len] = 1 + lcs_top_down(str1, str2, str1_len - 1, str2_len - 1)
        return table_top_down[str1_len][str2_len]
    else:
        table_top_down[str1_len][str2_len] = max(lcs_top_down(str1, str2, str1_len - 1, str2_len),
                                                 lcs_top_down(str1, str2, str1_len, str2_len - 1))
        return table_top_down[str1_len][str2_len]

print('LCS recursive', lcs(str1, str2, str1_len, str2_len))
print('LCS recursive V2', lcs_recursive_v2(str1, str2, 0, 0))
print('LCS memo', lcs_top_down(str1, str2, str1_len, str2_len))
