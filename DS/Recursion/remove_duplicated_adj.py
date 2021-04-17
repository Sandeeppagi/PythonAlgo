def remove_adj_duplicate(string):
    if not string:
        return ''

    if len(string) == 1:
        return string

    if string[0] == string[1]:
        return remove_adj_duplicate(string[1:])

    return string[0] + remove_adj_duplicate(string[1:])


print(remove_adj_duplicate('Hellloo'))  # returns Helo
