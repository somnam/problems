"""
This is a demo task.

Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

import unittest
import itertools
from typing import List


def solution(A: List[int]) -> int:
    A_set = set(A)
    for i in itertools.count(start=1, step=1):
        if i not in A_set:
            return i


class SolutionTests(unittest.TestCase):
    def test_case_1(self):
        A = [1, 3, 6, 4, 1, 2]

        result = solution(A)

        self.assertEqual(result, 5)

    def test_case_2(self):
        A = [1, 2, 3]

        result = solution(A)

        self.assertEqual(result, 4)

    def test_case_3(self):
        A = [-1, -3]

        result = solution(A)

        self.assertEqual(result, 1)

    def test_case_4(self):
        A = [0]

        result = solution(A)

        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
