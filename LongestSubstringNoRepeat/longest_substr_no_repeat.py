def lsnr(s):
    maxlen = 0
    longest_str = ''
    start = 0
    seen = set()
    for i, ch in enumerate(s):
        if ch in seen:
            while ch != s[start]:
                seen.remove(s[start])
                start += 1
            start += 1
        else:
            seen.add(ch)
        if i - start + 1 > maxlen:
            maxlen = i - start + 1
            longest_str = s[start:i + 1]
    return maxlen, longest_str


if __name__ == '__main__':
    print(lsnr('abcdeabc'))
    print(lsnr('aabcdebc'))
    print(lsnr('ababcdec'))
    print(lsnr('abcabcde'))
    print(lsnr('abcdecab'))
    print(lsnr('abcdeaxzy'))
