def spreadsheet_encode_column(col_str):
    num = 0
    power = len(col_str) - 1
    for s in col_str:
        num += 26**power * (ord(s.upper()) - ord('A') + 1)
        power -= 1
    return num


print('-' * 30)
print(spreadsheet_encode_column('zz'))
