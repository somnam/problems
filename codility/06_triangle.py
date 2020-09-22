"""
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

        A[P] + A[Q] > A[R],
        A[Q] + A[R] > A[P],
        A[R] + A[P] > A[Q].

For example, consider array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

Triplet (0, 2, 4) is triangular.

Write a function:

    def solution(A)

that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:
  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20

the function should return 1, as explained above. Given array A such that:
  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1

the function should return 0.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
"""

import unittest


def solution(A: list):
    len_A = len(A)

    if len_A < 3:
        return 0

    for i in range(0, len_A - 2):
        for j in range(i + 1, len_A - 1):
            for k in range(j + 1, len_A):
                # A[P] + A[Q] > A[R],
                # A[Q] + A[R] > A[P],
                # A[R] + A[P] > A[Q].
                has_triplet = (
                    A[i] + A[j] > A[k]
                    and A[j] + A[k] > A[i]
                    and A[k] + A[i] > A[j]
                )
                if has_triplet:
                    print(A[i], A[j], A[k])
                    return 1

    return 0


class SolutionTests(unittest.TestCase):
    def test_case_1(self):
        A = [10, 2, 5, 1, 8, 20]
        self.assertTrue(solution(A))

    def test_case_2(self):
        A = [10, 50, 5, 1]
        self.assertFalse(solution(A))

    def test_case_3(self):
        A = [1, 1, 2, 3, 5]
        self.assertFalse(solution(A))


if __name__ == "__main__":
    unittest.main()
