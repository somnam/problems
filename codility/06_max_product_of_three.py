"""
A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6

contains the following example triplets:

        (0, 1, 2), product is −3 * 1 * 2 = −6
        (1, 2, 4), product is 1 * 2 * 5 = 10
        (2, 4, 5), product is 2 * 5 * 6 = 60

Your goal is to find the maximal product of any triplet.

Write a function:

    def solution(A)

that, given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6

the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [3..100,000];
        each element of array A is an integer within the range [−1,000..1,000].
"""

import unittest


def solution(A: list):
    A.sort()

    len_A = len(A)

    A_left_idx = len_A - 3 if len_A < 6 else 3
    A_right_idx = -3

    A_subset = A[:A_left_idx] + A[A_right_idx:]

    len_A_subset = len(A_subset)

    max_product = None
    for i in range(0, len_A_subset - 2):
        for j in range(i + 1, len_A_subset - 1):
            for k in range(j + 1, len_A_subset):
                product = A_subset[i] * A_subset[j] * A_subset[k]

                if not max_product or product > max_product:
                    max_product = product

    return max_product


class SolutionTests(unittest.TestCase):
    def test_case_1(self):
        A = [-3, 1, 2, -2, 5, 6]

        result = solution(A)

        self.assertEqual(result, 60)

    def test_case_2(self):
        A = [7, 1, 2, -2, 5, 6]

        result = solution(A)

        self.assertEqual(result, 210)

    def test_case_3(self):
        A = [-5, 5, -5, 4]

        result = solution(A)

        self.assertEqual(result, 125)

    def test_case_4(self):
        A = [-4, -6, 3, 4, 5]

        result = solution(A)

        self.assertEqual(result, 120)

    def test_case_5(self):
        A = [-10, -2, -4]

        result = solution(A)

        self.assertEqual(result, -80)


if __name__ == "__main__":
    unittest.main()
