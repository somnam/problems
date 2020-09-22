"""
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4

In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

    def solution(X, A)

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:
  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4

the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

        N and X are integers within the range [1..100,000];
        each element of array A is an integer within the range [1..X].
"""

import unittest


def solution(X, A):
    len_A = len(A)
    if not len_A or len_A < X:
        return -1

    positions_required = set(range(1, X + 1))
    positions_available = set()
    for time_point, position in enumerate(A):
        if position not in positions_available:
            positions_available.add(position)
        if positions_available == positions_required:
            return time_point
    return -1


class SolutionTest(unittest.TestCase):
    def test_case_1(self):
        A = [1, 3, 1, 4, 2, 3, 5, 4]
        X = 5
        self.assertEqual(6, solution(X, A))

    def test_case_2(self):
        A = [1, 3, 1, 4, 2, 3, 6, 4]
        X = 5
        self.assertEqual(-1, solution(X, A))

    def test_case_3(self):
        A = [1, 3, 1, 4, 2, 3, 6, 4]
        X = 7
        self.assertEqual(-1, solution(X, A))

    def test_case_4(self):
        A = [1, 3, 1, 4, 2, 3]
        X = 7
        self.assertEqual(-1, solution(X, A))

    def test_case_5(self):
        A = [1, 3, 1, 4, 2, 3]
        X = 5
        self.assertEqual(-1, solution(X, A))


if __name__ == "__main__":
    unittest.main()
