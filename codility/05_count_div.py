"""
Write a function:

    def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

    { i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

        A and B are integers within the range [0..2,000,000,000];
        K is an integer within the range [1..2,000,000,000];
        A ≤ B.
"""
import unittest


def solution(A: int, B: int, K: int):
    if A == B:
        return 0 if A % K else 1

    return (B // K) - ((A - 1) // K)


class SolutionTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(solution(10, 10, 5), 1)

    def test_case_2(self):
        self.assertEqual(solution(10, 10, 4), 0)

    def test_case_3(self):
        self.assertEqual(solution(6, 11, 2), 3)


if __name__ == "__main__":
    unittest.main()
