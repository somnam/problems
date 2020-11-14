"""
Given a string s, find the length of the longest substring without repeating characters.
"""

import unittest
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)

        idx = 0
        streak = 0
        longest_streak = 0

        while idx < len(s):
            char = s[idx]

            if char in seen:
                if streak > longest_streak:
                    longest_streak = streak

                # Restart from position after first duplicate char.
                idx = seen[char] + 1
                streak = 0
                seen.clear()
            else:
                # Char seen for first time in current streak.
                seen[char] = idx
                streak += 1
                idx += 1

                if streak > longest_streak:
                    longest_streak = streak

        return longest_streak


class SolutionTests(unittest.TestCase):
    def test_case_1(self):
        result = Solution().lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(3, result)  # abc

    def test_case_2(self):
        result = Solution().lengthOfLongestSubstring("bbbbb")
        self.assertEqual(1, result)  # b

    def test_case_3(self):
        result = Solution().lengthOfLongestSubstring("pwwkew")
        self.assertEqual(3, result)  # wke

    def test_case_4(self):
        result = Solution().lengthOfLongestSubstring(" ")
        self.assertEqual(1, result)  # \s

    def test_case_5(self):
        result = Solution().lengthOfLongestSubstring("aa")
        self.assertEqual(1, result)  # a

    def test_case_6(self):
        result = Solution().lengthOfLongestSubstring("dvdf")
        self.assertEqual(3, result)  # vdf

    def test_case_7(self):
        result = Solution().lengthOfLongestSubstring("abcb")
        self.assertEqual(3, result)  # bcb

    def test_case_8(self):
        result = Solution().lengthOfLongestSubstring("asjrgapaj")
        self.assertEqual(6, result)  # sjrgap


if __name__ == '__main__':
    unittest.main()
