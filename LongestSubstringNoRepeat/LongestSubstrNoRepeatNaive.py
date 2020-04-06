def lsnr_naive(s):
    maxlen = 0
    lsnr = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substr = s[i:j]
            if not repeated_char(substr):
                if len(substr) > maxlen:
                    maxlen = len(substr)
                    lsnr = substr
    return maxlen, lsnr


def repeated_char(s):
    seen = set()
    for c in s:
        if c in seen:
            return True
        seen.add(c)
    return False


if __name__ == '__main__':
    print(lsnr_naive('abcdeabc'))
    print(lsnr_naive('aabcdebc'))
    print(lsnr_naive('ababcdec'))
    print(lsnr_naive('abcabcde'))
    print(lsnr_naive('abcdeaxzy'))

    # print(repeated_char('a'))
    # print(repeated_char('b'))
    # print(repeated_char('c'))
    # print(repeated_char('ab'))
    # print(repeated_char('abc'))
    # print(repeated_char('aabc'))
    # print(repeated_char('abac'))
    # print(repeated_char('abca'))
