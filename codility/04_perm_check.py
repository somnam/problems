"""
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

is a permutation, but array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

    def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

the function should return 1.

Given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

the function should return 0.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [1..1,000,000,000].
"""

import unittest


def solution(A):
    len_A = len(A)
    set_A = set(A)
    len_set_A = len(set_A)
    max_A = max(set_A)
    return 1 if len_A == len_set_A and len_A == max_A else 0


class SolutionTest(unittest.TestCase):
    def test_case_1(self):
        A = [4, 1, 3, 2]
        self.assertEqual(1, solution(A))

    def test_case_2(self):
        A = [4, 1, 3]
        self.assertEqual(0, solution(A))

    def test_case_3(self):
        A = [9, 5, 7, 3, 2, 7, 3, 1, 10, 8]
        self.assertEqual(0, solution(A))

    def test_case_4(self):
        A = [1, 1]
        self.assertEqual(0, solution(A))


if __name__ == "__main__":
    unittest.main()
