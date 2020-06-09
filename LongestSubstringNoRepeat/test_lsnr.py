from unittest import TestCase

from LongestSubstringNoRepeat.LongestSubstrNoRepeat import lsnr
from LongestSubstringNoRepeat.LongestSubstrNoRepeatNaive import lsnr_naive
from RandomData import random_string


class TestLsnr(TestCase):
    def test_lsnr(self):
        self.assertEqual(lsnr(''), lsnr_naive(''))
        self.assertEqual(lsnr('a'), lsnr_naive('a'))
        self.assertEqual(lsnr('abcde'), lsnr_naive('abcde'))
        self.assertEqual(lsnr('abcdeabc'), lsnr_naive('abcdeabc'))
        self.assertEqual(lsnr('aabcdebc'), lsnr_naive('aabcdebc'))
        self.assertEqual(lsnr('ababcdec'), lsnr_naive('ababcdec'))
        self.assertEqual(lsnr('abcabcde'), lsnr_naive('abcabcde'))
        self.assertEqual(lsnr('abcdeaxzy'), lsnr_naive('abcdeaxzy'))

        for _ in range(10000):
            s = random_string(30)
            print(s)
            print(lsnr(s))
            self.assertEqual(lsnr(s), lsnr_naive(s))
