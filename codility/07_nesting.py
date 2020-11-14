"""
A string S consisting of N characters is called properly nested if:

        S is empty;
        S has the form "(U)" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.

For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

    def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..1,000,000];
        string S consists only of the characters "(" and/or ")".
"""
import unittest
from collections import deque


def solution(S: str) -> int:
    matching_pairs = {"(": ")"}

    closing_brackets = set(matching_pairs.values())
    brackets = set(bracket
                   for brackets in matching_pairs.items()
                   for bracket in brackets)

    brackets_stack = deque()

    def has_matching_pair(char):
        if not brackets_stack:
            return False

        stack_top = brackets_stack[-1]
        matching_pair = matching_pairs.get(stack_top)
        return matching_pair == char

    for char in S:
        if char not in brackets:
            continue

        is_closing = char in closing_brackets

        if not is_closing:
            brackets_stack.append(char)
            continue

        if not has_matching_pair(char):
            return 0

        brackets_stack.pop()

    return 1 if not brackets_stack else 0


class SolutionTests(unittest.TestCase):
    def test_case_1(self):
        result = solution("")
        self.assertTrue(result)

    def test_case_2(self):
        result = solution("(((())))")
        self.assertTrue(result)

    def test_case_4(self):
        result = solution("((()()))")
        self.assertTrue(result)

    def test_case_5(self):
        result = solution("((()))(()()(()))")
        self.assertTrue(result)

    def test_case_6(self):
        result = solution("(()()]")
        self.assertFalse(result)

    def test_case_7(self):
        result = solution(")(")
        self.assertFalse(result)

    def test_case_8(self):
        result = solution("(()(")
        self.assertFalse(result)

    def test_case_9(self):
        result = solution("((((")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
