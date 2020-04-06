from random import randrange, choice
from unittest import TestCase

from ShortestCommonSupersequence import scs_naive, scs_recur


class TestSCS(TestCase):
    def test_scs_recur(self):
        for _ in range(100):
            # s1 = random_string(5)
            # s2 = random_string(5)
            # print(s1, s2)
            # print(scs_recur(s1, s2))
            # self.assertEqual(scs_naive(s1, s2), scs_recur(s1, s2))

            s1 = ''.join([choice('abcde') for _ in range(randrange(1, 5 + 1))])
            s2 = ''.join([choice('abcde') for _ in range(randrange(1, 5 + 1))])
            print(s1, s2)
            print(scs_recur(s1, s2))
            self.assertEqual(scs_naive(s1, s2), scs_recur(s1, s2))
