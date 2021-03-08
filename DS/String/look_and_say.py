def look_and_say(my_str):
    result = []
    count = 0
    value = None
    for i in range(len(my_str)):
        if value is None:
            value = my_str[i]
            count += 1
        elif value == my_str[i]:
            count += 1
        elif value != my_str[i]:
            result.append(str(count))
            result.append(value)
            value = my_str[i]
            count = 1
    result.append(str(count))
    result.append(value)
    return "".join(result)


def look_and_say_v2(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)


# 1, 11, 21, 1211, 111221, 312211, 13112221
print('-'*30)
s = "1"
print(s)
n = 7
for i in range(n-1):
    s = look_and_say(s)
    print(s)
print('-'*30)
s = "1"
print(s)
n = 7
for i in range(n-1):
    s = look_and_say_v2(s)
    print(s)
