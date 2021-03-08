"""
    "rail safety" = "fairy tales"
    "roast beef" = "eat for BSE"
    "William Shakespeare" = "I am a weakish speller"
    "Madam Curie" = "Radium came"
"""



def is_anagram(s1, s2):
    ht = dict()

    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1

    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1

    for i in ht:
        if ht[i] != 0:
            return False

    return True


s1 = "rail safety"
s2 = "fairy tales"
print('-'*30)
print(is_anagram(s1, s2))

s1 = s1.replace(" ","").lower()
s2 = s2.replace(" ", "").lower()
print(sorted(s1) == sorted(s2))
