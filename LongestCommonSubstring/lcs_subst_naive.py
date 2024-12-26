def substrings(s):
    subst = []
    for i in range(len(s) + 1):
        for j in range(i + 1, len(s) + 1):
            subst.append(s[i:j])
    return subst


def lcsubst_naive(s1, s2):
    maxlen = 0
    for subst1 in substrings(s1):
        for subst2 in substrings(s2):
            if subst1 == subst2:
                maxlen = max(maxlen, len(subst1))
    # print(substrings(s1))
    # print(substrings(s2))
    return maxlen


if __name__ == '__main__':
    # print(lcsubst_naive('xyzabcd', 'abcdxyz'))
    print(lcsubst_naive('tcaakv', 'uczvbl'))

    # print(lcsubst_naive('xyzabcdpqlskdjgfnvmxkshfoeyuthgj', 'hgkjdutiwpojdabcdhfkdsnjek'))
    # print(lcsubst_naive('longmatchingstringabcdefghijklmnop', 'longmatchingstringponmlkjihgfedcba'))
    # print(lcsubst_naive('longmatchingstringabcdefghijklmnop', 'ponmlkjihgfedcbalongmatchingstring'))
    # print(lcsubst_naive('alongmatchingstringabcdefghijklmnop', 'ponmlkjihgfedcbalongmatchingstringz'))
    # print(lcsubst_naive('qhwiwvqir', 'igjw'))
    # print(substrings('abcde'))