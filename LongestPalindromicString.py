def lps_dyna(s):
    if len(s) < 2:
        return s
    dp_arr = [[False] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        dp_arr[i][i] = True  # string with len = 1 are palindromes
    for i in range(len(s) - 1):
        dp_arr[i + 1][i] = True
    # for item in dp_arr:
    #     print(item)
    lps = ''
    for i in range(2, len(s) + 1):
        for j in range(len(s) + 1 - i):
            # print(f'i={i}  j={j}  s[{j}:{j + i}] {s[j:j + i]} ')
            substr = s[j:j + i]
            if substr[0] == substr[-1]:
                dp_arr[j][i-1] = dp_arr[j + 1][i - 2]
                if len(substr) > len(lps):
                    lps = substr
    for item in dp_arr:
        print(item)
    return lps


# s = 'banana'
# 1 = b  a  n  a  n  a
# 2 = ba  an  na  an  na
# 3 = ban  ana  nan  ana
# 4 = bana  anan  nana
# 5 = banan  anana
# 6 = banana


print(lps_dyna('banana'))
# print(lps_dyna('anana'))

# print(lps_dyna(''))
# print(lps_dyna('a'))
# print(lps_dyna('ab'))
# print(lps_dyna('aba'))
# print(lps_dyna('abac'))
# print(lps_dyna('caba'))
