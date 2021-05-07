def lcs_(str1, str2, i, j, count):
    # base case of when either of string has been exhausted
    if i >= len(str1) or j >= len(str2):
        return count
    # if i and j character matches, increment the count and compare the rest of the strings
    if str1[i] == str2[j]:
        count = lcs_(str1, str2, i + 1, j + 1, count + 1)
    # compare str1[1:] with str2, str1 with str2[1:], and take max of current count and these two results
    return max(count, lcs_(str1, str2, i + 1, j, 0), lcs_(str1, str2, i, j + 1, 0))


def lcs(str1, str2):
    return lcs_(str1, str2, 0, 0, 0)


print(lcs("hello", "elf"))


def lcs_v2(str1, str2, i, j, count, memo):
    # base case of when either of string has been exhausted
    if i >= len(str1) or j >= len(str2):
        return count
    # check if result available in memo
    if (i, j, count) in memo:
        return memo[(i, j, count)]
    c = count
    # if i and j character matches, increment the count and compare the rest of the strings
    if str1[i] == str2[j]:
        c = lcs_v2(str1, str2, i + 1, j + 1, count + 1, memo)
    # compare str1[1:] with str2, str1 with str2[1:], and take max of current count and these two results
    # memoize the result
    memo[(i, j, count)] = max(c, lcs_v2(str1, str2, i + 1, j, 0, memo), lcs_v2(str1, str2, i, j + 1, 0, memo))
    return memo[(i, j, count)]


def lcs(str1, str2):
    memo = {}
    return lcs_v2(str1, str2, 0, 0, 0, memo)


print(lcs("hel", "elf"))

# testing with longer strings
import random
import string

st1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(40))
st2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(60))
print(lcs(st1, st2 + st1))


def lcs_v3(str1, str2):
    n = len(str1)  # length of str1
    m = len(str2)  # length of str1

    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]  # table for tabulation of size m x n
    maxLength = 0  # to keep track of longest substring seen

    for i in range(1, n + 1):  # iterating to fill table
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:  # if characters at this position match,
                dp[i][j] = dp[i - 1][j - 1] + 1  # add 1 to the previous diagonal and store it in this diagonal
                maxLength = max(maxLength, dp[i][j])  # if this substring is longer, replace it in maxlength
            else:
                dp[i][j] = 0  # if character don't match, common substring size is 0
    return maxLength


stressTesting = True  # to only check if your recursive solution is correct, set it to false
testForBottomUp = True  # to test a top down implementation set it to false

print(lcs_v3("hel", "elf"))

# testing with longer strings
import random
import string

st1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(400))
st2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(600))
print(lcs_v3(st1, st2 + st1))
